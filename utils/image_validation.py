"""
Image validation utility for Reality -> Action AI.
Ensures files meet format, MIME, size, dimension, and decoding integrity checks.
Protects backend and AI services from malformed or malicious payloads.
"""

import io
from typing import Tuple, Optional
from PIL import Image

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_MIME_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/webp",
}
DEFAULT_MAX_BYTES = 10 * 1024 * 1024  # 10 MB
MIN_DIMENSION = 16
MAX_DIMENSION = 8192


class ImageValidationError(Exception):
    """Custom exception raised when image validation fails."""
    pass


def validate_image_file(
    file_bytes: bytes,
    filename: str,
    max_bytes: int = DEFAULT_MAX_BYTES,
) -> Tuple[bool, Optional[str], Optional[dict]]:
    """
    Validates uploaded image bytes against security & integrity criteria.
    
    Returns:
        (is_valid: bool, error_message: Optional[str], metadata: Optional[dict])
    """
    if not file_bytes:
        return False, "No image file provided or file is empty.", None

    # Check file size
    if len(file_bytes) > max_bytes:
        size_mb = len(file_bytes) / (1024 * 1024)
        limit_mb = max_bytes / (1024 * 1024)
        return (
            False,
            f"Image file size ({size_mb:.2f} MB) exceeds maximum allowed size ({limit_mb:.0f} MB).",
            None,
        )

    # Check file extension
    ext = ""
    if "." in filename:
        ext = "." + filename.rsplit(".", 1)[-1].lower()
    
    if ext not in ALLOWED_EXTENSIONS:
        return (
            False,
            f"Unsupported file format '{ext}'. Allowed formats: JPG, JPEG, PNG, WEBP.",
            None,
        )

    # Attempt actual image decoding with Pillow
    try:
        with Image.open(io.BytesIO(file_bytes)) as img:
            # Verify image integrity
            img.verify()

        # Re-open for metadata (verify can close/alter the stream in PIL)
        with Image.open(io.BytesIO(file_bytes)) as img:
            format_name = (img.format or "").upper()
            width, height = img.size

            if format_name not in {"JPEG", "PNG", "WEBP"}:
                return (
                    False,
                    f"Decoded image format '{format_name}' is not supported.",
                    None,
                )

            if width < MIN_DIMENSION or height < MIN_DIMENSION:
                return (
                    False,
                    f"Image resolution ({width}x{height}) is too small. Minimum resolution is {MIN_DIMENSION}x{MIN_DIMENSION}px.",
                    None,
                )

            if width > MAX_DIMENSION or height > MAX_DIMENSION:
                return (
                    False,
                    f"Image resolution ({width}x{height}) is too large. Maximum resolution is {MAX_DIMENSION}x{MAX_DIMENSION}px.",
                    None,
                )

            metadata = {
                "format": format_name,
                "width": width,
                "height": height,
                "mode": img.mode,
                "size_bytes": len(file_bytes),
                "extension": ext,
            }
            return True, None, metadata

    except Exception as e:
        return False, f"Corrupted or invalid image file: {str(e)}", None

"""
Tests for Image Validation Module.
"""

import io
from PIL import Image
from utils.image_validation import validate_image_file, DEFAULT_MAX_BYTES


def create_test_image(format_name="PNG", size=(100, 100), color="blue") -> bytes:
    img = Image.new("RGB", size, color=color)
    buf = io.BytesIO()
    img.save(buf, format=format_name)
    return buf.getvalue()


def test_valid_png_image():
    bytes_data = create_test_image(format_name="PNG", size=(200, 150))
    valid, err, meta = validate_image_file(bytes_data, "test.png")
    assert valid is True
    assert err is None
    assert meta["format"] == "PNG"
    assert meta["width"] == 200
    assert meta["height"] == 150


def test_valid_jpeg_image():
    bytes_data = create_test_image(format_name="JPEG", size=(300, 200))
    valid, err, meta = validate_image_file(bytes_data, "photo.jpg")
    assert valid is True
    assert err is None
    assert meta["format"] == "JPEG"


def test_empty_file():
    valid, err, meta = validate_image_file(b"", "empty.png")
    assert valid is False
    assert "No image file provided" in err


def test_invalid_extension():
    bytes_data = create_test_image(format_name="PNG")
    valid, err, meta = validate_image_file(bytes_data, "malicious.exe")
    assert valid is False
    assert "Unsupported file format" in err


def test_corrupted_image_bytes():
    fake_bytes = b"not_an_image_header_random_junk_1234567890"
    valid, err, meta = validate_image_file(fake_bytes, "corrupt.png")
    assert valid is False
    assert "Corrupted or invalid" in err


def test_exceeds_max_size():
    bytes_data = create_test_image(format_name="PNG")
    # Set limit to 10 bytes to trigger size failure
    valid, err, meta = validate_image_file(bytes_data, "large.png", max_bytes=10)
    assert valid is False
    assert "exceeds maximum allowed size" in err


def test_resolution_too_small():
    tiny_bytes = create_test_image(format_name="PNG", size=(5, 5))
    valid, err, meta = validate_image_file(tiny_bytes, "tiny.png")
    assert valid is False
    assert "too small" in err

"""
Storage service for Reality -> Action AI.
Manages private image uploads to Supabase Storage ('reality-images') with signed URLs.
Includes local fallback for offline/demo operation.
"""

import os
import uuid
import base64
from typing import Optional, Tuple
from utils.config import get_config
from auth import get_supabase_client

BUCKET_NAME = "reality-images"
LOCAL_STORAGE_DIR = "temp_images"


class StorageService:
    def __init__(self):
        self.config = get_config()
        self.client = get_supabase_client()
        os.makedirs(LOCAL_STORAGE_DIR, exist_ok=True)

    @property
    def is_live(self) -> bool:
        return self.client is not None

    def upload_image(
        self,
        file_bytes: bytes,
        user_id: str,
        extension: str = "png",
        content_type: str = "image/png",
    ) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Uploads an image to the private storage bucket.
        Returns: (success: bool, image_path: Optional[str], error_message: Optional[str])
        """
        if not file_bytes:
            return False, None, "No file bytes provided for upload."

        clean_ext = extension.lstrip(".")
        file_id = str(uuid.uuid4())
        storage_path = f"{user_id}/{file_id}.{clean_ext}"

        if not self.is_live:
            # Fallback local persistence
            local_user_dir = os.path.join(LOCAL_STORAGE_DIR, user_id)
            os.makedirs(local_user_dir, exist_ok=True)
            local_file_path = os.path.join(local_user_dir, f"{file_id}.{clean_ext}")
            try:
                with open(local_file_path, "wb") as f:
                    f.write(file_bytes)
                return True, storage_path, None
            except Exception as e:
                return False, None, f"Local storage save failed: {str(e)}"

        try:
            self.client.storage.from_(BUCKET_NAME).upload(
                path=storage_path,
                file=file_bytes,
                file_options={"content-type": content_type, "upsert": "false"},
            )
            return True, storage_path, None
        except Exception as e:
            err = str(e)
            # If bucket doesn't exist yet, try to create or give clear instruction
            return False, None, f"Supabase storage upload error: {err}"

    def get_signed_url(self, image_path: str, expires_in: int = 3600) -> Optional[str]:
        """
        Generates a secure, short-lived signed URL for an image.
        Returns None or data URL if fallback.
        """
        if not image_path:
            return None

        if not self.is_live:
            # Check local file
            parts = image_path.split("/")
            if len(parts) == 2:
                local_path = os.path.join(LOCAL_STORAGE_DIR, parts[0], parts[1])
                if os.path.exists(local_path):
                    try:
                        with open(local_path, "rb") as f:
                            data = f.read()
                        ext = parts[1].split(".")[-1]
                        b64 = base64.b64encode(data).decode("utf-8")
                        return f"data:image/{ext};base64,{b64}"
                    except Exception:
                        return None
            return None

        try:
            res = self.client.storage.from_(BUCKET_NAME).create_signed_url(
                path=image_path,
                expires_in=expires_in,
            )
            if isinstance(res, dict) and "signedURL" in res:
                return res["signedURL"]
            if hasattr(res, "signed_url"):
                return res.signed_url
            if isinstance(res, str):
                return res
            return None
        except Exception:
            return None

    def delete_image(self, image_path: str) -> bool:
        """Removes an image from storage."""
        if not image_path:
            return True

        if not self.is_live:
            parts = image_path.split("/")
            if len(parts) == 2:
                local_path = os.path.join(LOCAL_STORAGE_DIR, parts[0], parts[1])
                if os.path.exists(local_path):
                    try:
                        os.remove(local_path)
                    except Exception:
                        pass
            return True

        try:
            self.client.storage.from_(BUCKET_NAME).remove([image_path])
            return True
        except Exception:
            return False

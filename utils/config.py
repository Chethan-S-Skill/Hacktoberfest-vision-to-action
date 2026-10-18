"""
Configuration utility for Reality -> Action AI.
Loads settings securely from environment variables / .env file.
Prevents leaking secrets and provides diagnostic status.
"""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()


def _is_placeholder(val: Optional[str]) -> bool:
    if not val:
        return True
    val_clean = val.strip().lower()
    placeholders = {
        "your_sarvam_api_key_here",
        "your_supabase_anon_public_key_here",
        "https://your-project-id.supabase.co",
        "none",
        "placeholder",
        "",
    }
    return val_clean in placeholders or "your_" in val_clean or "placeholder" in val_clean


@dataclass(frozen=True)
class AppConfig:
    sarvam_api_key: Optional[str]
    sarvam_base_url: str
    sarvam_model: str
    supabase_url: Optional[str]
    supabase_anon_key: Optional[str]
    max_image_size_mb: int
    demo_mode: bool

    @property
    def is_sarvam_configured(self) -> bool:
        return bool(self.sarvam_api_key and not _is_placeholder(self.sarvam_api_key))

    @property
    def is_supabase_configured(self) -> bool:
        return bool(
            self.supabase_url
            and not _is_placeholder(self.supabase_url)
            and self.supabase_anon_key
            and not _is_placeholder(self.supabase_anon_key)
        )

    def mask_secret(self, secret: Optional[str]) -> str:
        if not secret or _is_placeholder(secret):
            return "Not Configured"
        if len(secret) <= 8:
            return "****"
        return f"{secret[:4]}...{secret[-4:]}"

    def get_diagnostics(self) -> dict:
        """Returns safe telemetry without leaking secrets."""
        return {
            "sarvam_configured": self.is_sarvam_configured,
            "sarvam_model": self.sarvam_model,
            "supabase_configured": self.is_supabase_configured,
            "supabase_url": self.supabase_url if self.is_supabase_configured else "Not Configured",
            "max_image_size_mb": self.max_image_size_mb,
            "demo_mode": self.demo_mode,
        }


def get_config() -> AppConfig:
    sarvam_key = os.getenv("SARVAM_API_KEY", "").strip() or None
    sarvam_base = os.getenv("SARVAM_BASE_URL", "https://api.sarvam.ai").strip()
    sarvam_model = os.getenv("SARVAM_MODEL", "sarvam-gemma-4").strip()

    sb_url = os.getenv("SUPABASE_URL", "").strip() or None
    sb_anon = os.getenv("SUPABASE_ANON_KEY", "").strip() or None

    try:
        max_size = int(os.getenv("MAX_IMAGE_SIZE_MB", "10"))
    except ValueError:
        max_size = 10

    # Auto-enable demo mode if keys are not configured or DEMO_MODE=true
    demo_env = os.getenv("DEMO_MODE", "").strip().lower()
    has_real_keys = (
        sarvam_key and not _is_placeholder(sarvam_key) and
        sb_url and not _is_placeholder(sb_url) and
        sb_anon and not _is_placeholder(sb_anon)
    )

    if demo_env == "true":
        demo_mode = True
    elif demo_env == "false":
        demo_mode = False
    else:
        demo_mode = not has_real_keys

    return AppConfig(
        sarvam_api_key=sarvam_key,
        sarvam_base_url=sarvam_base,
        sarvam_model=sarvam_model,
        supabase_url=sb_url,
        supabase_anon_key=sb_anon,
        max_image_size_mb=max_size,
        demo_mode=demo_mode,
    )

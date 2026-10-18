"""
Tests for Config Utility and Secret Masking.
"""

from utils.config import AppConfig, _is_placeholder


def test_is_placeholder_detection():
    assert _is_placeholder("") is True
    assert _is_placeholder("your_sarvam_api_key_here") is True
    assert _is_placeholder("https://your-project-id.supabase.co") is True
    assert _is_placeholder("sk-real-live-api-key-12345678") is False


def test_secret_masking():
    cfg = AppConfig(
        sarvam_api_key="sarvam_secret_key_1234567890",
        sarvam_base_url="https://api.sarvam.ai",
        sarvam_model="sarvam-gemma-4",
        supabase_url="https://xyz.supabase.co",
        supabase_anon_key="anon_secret_key_9876543210",
        max_image_size_mb=10,
        demo_mode=False,
    )
    masked = cfg.mask_secret(cfg.sarvam_api_key)
    assert masked == "sarv...7890"
    assert "secret_key" not in masked


def test_diagnostics_telemetry():
    cfg = AppConfig(
        sarvam_api_key="live_key_123",
        sarvam_base_url="https://api.sarvam.ai",
        sarvam_model="sarvam-gemma-4",
        supabase_url=None,
        supabase_anon_key=None,
        max_image_size_mb=10,
        demo_mode=True,
    )
    diag = cfg.get_diagnostics()
    assert diag["sarvam_configured"] is True
    assert diag["supabase_configured"] is False
    assert diag["max_image_size_mb"] == 10

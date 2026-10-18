"""
Authentication Service for Reality -> Action AI.
Manages Supabase Auth, session lifecycle, and fallback demo guest mode.
"""

from typing import Optional, Dict, Any, Tuple
from utils.config import get_config

try:
    from supabase import create_client, Client
except ImportError:
    create_client = None
    Client = Any

_supabase_client: Optional[Client] = None


def get_supabase_client() -> Optional[Client]:
    """Initializes and caches the Supabase client."""
    global _supabase_client
    if _supabase_client is not None:
        return _supabase_client

    config = get_config()
    if config.is_supabase_configured and create_client:
        try:
            _supabase_client = create_client(config.supabase_url, config.supabase_anon_key)
            return _supabase_client
        except Exception:
            return None
    return None


class AuthService:
    def __init__(self, force_demo: bool = False):
        self.config = get_config()
        self.force_demo = force_demo
        self.client = None if force_demo else get_supabase_client()

    @property
    def is_live(self) -> bool:
        return self.client is not None and not self.force_demo

    def sign_up(self, email: str, password: str) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
        """Registers a new user with Supabase Auth."""
        if not email or "@" not in email:
            return False, "Please enter a valid email address.", None
        if len(password) < 6:
            return False, "Password must be at least 6 characters long.", None

        if not self.is_live:
            # Demo registration
            user = {
                "id": "demo-user-001",
                "email": email,
                "is_demo": True,
            }
            return True, "Account registered successfully (Demo Mode).", user

        try:
            res = self.client.auth.sign_up({"email": email, "password": password})
            if res.user:
                user_data = {
                    "id": str(res.user.id),
                    "email": res.user.email,
                    "is_demo": False,
                }
                msg = "Registration successful! You can now sign in."
                if res.session is None:
                    msg = "Registration successful! Please check your email inbox to verify your account before logging in."
                return True, msg, user_data
            return False, "Registration could not be completed. Please try again.", None
        except Exception as e:
            err_msg = str(e)
            if "already registered" in err_msg.lower():
                return False, "An account with this email address already exists.", None
            return False, f"Registration failed: {err_msg}", None

    def sign_in(self, email: str, password: str) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
        """Signs in a user with Supabase Auth."""
        if not email or not password:
            return False, "Email and password are required.", None

        if not self.is_live:
            user = {
                "id": "demo-user-001",
                "email": email,
                "is_demo": True,
            }
            return True, "Signed in successfully (Demo Mode).", user

        try:
            res = self.client.auth.sign_in_with_password({"email": email, "password": password})
            if res.user and res.session:
                user_data = {
                    "id": str(res.user.id),
                    "email": res.user.email,
                    "access_token": res.session.access_token,
                    "refresh_token": res.session.refresh_token,
                    "is_demo": False,
                }
                return True, "Signed in successfully.", user_data
            return False, "Invalid email or password.", None
        except Exception as e:
            err_msg = str(e)
            if "invalid login credentials" in err_msg.lower():
                return False, "Invalid email or password. Please verify your credentials.", None
            if "email not confirmed" in err_msg.lower():
                return False, "Email address not confirmed. Please check your inbox for verification link.", None
            return False, f"Login failed: {err_msg}", None

    def sign_out(self) -> Tuple[bool, str]:
        """Signs out the active user session."""
        if self.is_live:
            try:
                self.client.auth.sign_out()
            except Exception:
                pass
        return True, "Signed out successfully."

    def reset_password(self, email: str) -> Tuple[bool, str]:
        """Sends a password recovery email."""
        if not email or "@" not in email:
            return False, "Please enter a valid email address."

        if not self.is_live:
            return True, "Password reset link simulated (Demo Mode)."

        try:
            self.client.auth.reset_password_for_email(email)
            return True, "Password reset instructions sent to your email."
        except Exception as e:
            return False, f"Password reset failed: {str(e)}"

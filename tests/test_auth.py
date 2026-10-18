"""
Tests for Auth Service.
"""

from auth import AuthService


def test_auth_validation_rules():
    auth = AuthService()

    # Invalid email
    ok, msg, user = auth.sign_up("invalid-email", "secret123")
    assert ok is False
    assert "valid email" in msg

    # Short password
    ok, msg, user = auth.sign_up("user@test.com", "123")
    assert ok is False
    assert "at least 6 characters" in msg


def test_demo_auth_flow():
    auth = AuthService()
    ok, msg, user = auth.sign_in("demo@test.com", "validpassword")
    assert ok is True
    assert user is not None
    assert "email" in user
    assert "id" in user

    # Sign out
    out_ok, out_msg = auth.sign_out()
    assert out_ok is True

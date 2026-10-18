"""
Reality -> Action AI: Main Application Entry Point.
Production-grade visual AI assistant bridging image understanding and safe physical execution.
"""

import streamlit as st
from ui.styles import PRO_CSS
from ui.components import render_header
from ui.pages.home import render_home_page
from ui.pages.history import render_history_page
from ui.pages.how_it_works import render_how_it_works_page
from ui.pages.account import render_account_page
from auth import AuthService
from utils.config import get_config

# 1. Page Configuration
st.set_page_config(
    page_title="Reality → Action AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Inject Pro Cyber-Industrial Design System
st.markdown(PRO_CSS, unsafe_allow_html=True)


def init_session():
    """Initializes session state defaults."""
    if "user" not in st.session_state:
        st.session_state["user"] = None
    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "Home / Analyze"


def render_auth_screen(auth_svc: AuthService):
    """Renders authentication screen with Supabase login, signup, and 1-click Judge Demo access."""
    st.markdown(
        """
        <div style="text-align: center; margin: 40px auto 25px auto; max-width: 650px;">
            <div style="
                width: 58px; height: 58px; 
                background: linear-gradient(135deg, #00F0FF 0%, #A855F7 100%); 
                border-radius: 16px; 
                display: inline-flex; align-items: center; justify-content: center;
                box-shadow: 0 0 25px rgba(0, 240, 255, 0.45);
                font-size: 1.8rem; margin-bottom: 12px;
            ">⚡</div>
            <h1 class="hero-title" style="font-size: 2.8rem !important; margin-bottom: 8px !important;">Reality → Action AI</h1>
            <div class="hero-subtitle">
                Transform real-world visual observations into safe, structured physical action protocols.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    auth_col1, auth_col2, auth_col3 = st.columns([1, 2, 1])
    with auth_col2:
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)

        tab_login, tab_signup, tab_demo = st.tabs(["🔐 Sign In", "📝 Create Account", "⚡ Judge Instant Access"])

        with tab_login:
            st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)
            with st.form("signin_form"):
                in_email = st.text_input("Email Address", placeholder="name@domain.com")
                in_pwd = st.text_input("Password", type="password", placeholder="••••••••")
                submit_in = st.form_submit_button("Sign In to Action AI", use_container_width=True)

                if submit_in:
                    ok, msg, user = auth_svc.sign_in(in_email, in_pwd)
                    if ok and user:
                        st.session_state["user"] = user
                        st.success(f"✓ {msg}")
                        st.rerun()
                    else:
                        st.error(f"❌ {msg}")

        with tab_signup:
            st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)
            with st.form("signup_form"):
                up_email = st.text_input("Email Address", placeholder="name@domain.com")
                up_pwd = st.text_input("Create Password (min 6 chars)", type="password", placeholder="••••••••")
                submit_up = st.form_submit_button("Register Account", use_container_width=True)

                if submit_up:
                    ok, msg, user = auth_svc.sign_up(up_email, up_pwd)
                    if ok:
                        st.success(f"✓ {msg}")
                        if user and user.get("is_demo"):
                            st.session_state["user"] = user
                            st.rerun()
                    else:
                        st.error(f"❌ {msg}")

        with tab_demo:
            st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 0.9rem; color: #CBD5E1; line-height: 1.6; margin-bottom: 16px;">
                    Evaluating for a hackathon or presentation? Jump straight into the full interactive application without waiting for email verification.
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("🚀 Launch Instant Judge Showcase Mode", use_container_width=True):
                st.session_state["user"] = {
                    "id": "judge-evaluator-001",
                    "email": "judge@hackathon.internal",
                    "is_demo": True,
                }
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


def main():
    init_session()
    auth_svc = AuthService()
    user = st.session_state["user"]

    if not user:
        render_auth_screen(auth_svc)
        return

    # Render Persistent Header
    render_header(user)

    # Sidebar Navigation
    with st.sidebar:
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 18px;">
                <span style="font-size: 1.2rem;">⚡</span>
                <span style="font-weight: 800; font-size: 1.15rem; color: #F8FAFC;">ACTION AI</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        nav_options = [
            "🏠 Home / Analyze",
            "📋 Audit History",
            "🏛️ How It Works",
            "👤 Account & Telemetry",
        ]

        active_nav = st.radio(
            "Navigation",
            nav_options,
            index=0,
            label_visibility="collapsed",
        )

        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        st.markdown("---")

        # Telemetry Quick-Widget
        config = get_config()
        st.markdown(
            f"""
            <div style="font-size: 0.75rem; color: #64748B; text-transform: uppercase; margin-bottom: 6px;">Engine Status</div>
            <div style="font-size: 0.85rem; color: {'#34D399' if config.is_sarvam_configured else '#FBBF24'}; font-weight: 600; margin-bottom: 4px;">
                {'● Sarvam AI Live' if config.is_sarvam_configured else '● Demo Sandbox Mode'}
            </div>
            <div style="font-size: 0.75rem; color: #94A3B8;">Model: {config.sarvam_model}</div>
            <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 2px;">Storage: reality-images (RLS)</div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        if st.button("🚪 Sign Out", use_container_width=True):
            auth_svc.sign_out()
            st.session_state["user"] = None
            st.session_state["active_result"] = None
            st.rerun()

    # Route to Selected Page
    if "Home" in active_nav:
        render_home_page(user)
    elif "History" in active_nav:
        render_history_page(user)
    elif "How It Works" in active_nav:
        render_how_it_works_page()
    elif "Account" in active_nav:
        render_account_page(user)


if __name__ == "__main__":
    main()

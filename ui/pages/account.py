"""
Account & Settings Page for Reality -> Action AI.
Displays session info, system telemetry diagnostics, password recovery, and sign-out controls.
"""

import streamlit as st
from auth import AuthService
from utils.config import get_config


def render_account_page(current_user: dict):
    auth_svc = AuthService()
    config = get_config()

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 class="hero-title" style="font-size: 2.2rem !important;">Account & System Telemetry</h2>
            <div class="hero-subtitle">
                Manage your authenticated identity, view configuration status, and update security credentials.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 👤 User Profile")
        email = current_user.get("email", "Not available")
        user_id = current_user.get("id", "N/A")
        is_demo = current_user.get("is_demo", False)

        st.markdown(
            f"""
            <div class="pro-card">
                <div style="margin-bottom: 12px;">
                    <span style="font-size: 0.8rem; color: #64748B; text-transform: uppercase;">Authenticated Email</span>
                    <div style="font-size: 1.1rem; font-weight: 600; color: #E2E8F0;">{email}</div>
                </div>
                <div style="margin-bottom: 12px;">
                    <span style="font-size: 0.8rem; color: #64748B; text-transform: uppercase;">User Session ID</span>
                    <div style="font-size: 0.95rem; font-family: 'JetBrains Mono', monospace; color: #38BDF8;">{user_id}</div>
                </div>
                <div style="margin-bottom: 16px;">
                    <span style="font-size: 0.8rem; color: #64748B; text-transform: uppercase;">Session Type</span>
                    <div>
                        {'<span class="badge-caution">SHOWCASE DEMO SESSION</span>' if is_demo else '<span class="badge-low">SUPABASE SECURE SESSION</span>'}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 🔒 Password Management")
        with st.form("pwd_reset_form"):
            reset_email = st.text_input("Account Email for Password Reset", value=email)
            reset_btn = st.form_submit_button("Send Password Recovery Link", use_container_width=True)
            if reset_btn:
                ok, msg = auth_svc.reset_password(reset_email)
                if ok:
                    st.success(f"✓ {msg}")
                else:
                    st.error(f"❌ {msg}")

    with col2:
        st.markdown("### ⚙️ System Configuration")
        diag = config.get_diagnostics()

        st.markdown(
            f"""
            <div class="radar-card">
                <div style="margin-bottom: 14px; font-weight: 700; color: #00F0FF; font-size: 0.9rem; letter-spacing: 0.05em;">
                    ENVIRONMENT TELEMETRY (SAFE DIAGNOSTICS)
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px;">
                    <span style="color: #94A3B8;">Sarvam AI Engine:</span>
                    <span style="color: {'#34D399' if diag['sarvam_configured'] else '#FBBF24'}; font-weight: 600;">
                        {'ONLINE (Configured)' if diag['sarvam_configured'] else 'OFFLINE (Demo Mode Active)'}
                    </span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px;">
                    <span style="color: #94A3B8;">Gemma 4 Vision Model:</span>
                    <span style="color: #E2E8F0; font-family: 'JetBrains Mono', monospace;">{diag['sarvam_model']}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px;">
                    <span style="color: #94A3B8;">Supabase Auth & RLS:</span>
                    <span style="color: {'#34D399' if diag['supabase_configured'] else '#FBBF24'}; font-weight: 600;">
                        {'CONNECTED' if diag['supabase_configured'] else 'STANDALONE PERSISTENCE'}
                    </span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px;">
                    <span style="color: #94A3B8;">Private Storage Bucket:</span>
                    <span style="color: #38BDF8; font-family: 'JetBrains Mono', monospace;">reality-images</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span style="color: #94A3B8;">Payload Size Limit:</span>
                    <span style="color: #E2E8F0;">{diag['max_image_size_mb']} MB</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        if st.button("🚪 Sign Out of Session", use_container_width=True):
            auth_svc.sign_out()
            st.session_state["user"] = None
            st.session_state["active_result"] = None
            st.success("Signed out successfully.")
            st.rerun()

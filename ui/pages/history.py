"""
History Page for Reality -> Action AI.
Displays saved user analyses, signed image previews, search/filtering,
full inspection inspection protocol review, and secure deletion.
"""

import streamlit as st
from database import DatabaseService
from storage import StorageService
from ui.components import (
    render_radar,
    render_observations,
    render_blindspots,
    render_safety_banner,
    render_interactive_checklist,
    render_threat_badge,
    generate_field_report_markdown,
)


def render_history_page(current_user: dict):
    db_svc = DatabaseService()
    storage_svc = StorageService()
    user_id = current_user.get("id", "demo-user")

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 class="hero-title" style="font-size: 2.2rem !important;">Audit History & Saved Analyses</h2>
            <div class="hero-subtitle">
                Review previous visual analyses, inspect executed action protocols, and retrieve signed field reports.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Search & Filter
    search_col, filter_col = st.columns([3, 1])
    with search_col:
        search_query = st.text_input("🔍 Search analyses by keyword, component, or question...", "")
    with filter_col:
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.rerun()

    # Retrieve from Database
    records = db_svc.get_user_history(user_id=user_id, limit=50, search_query=search_query)

    if not records:
        st.markdown(
            """
            <div class="pro-card" style="text-align: center; padding: 40px 20px;">
                <div style="font-size: 2.5rem; margin-bottom: 12px;">📂</div>
                <div style="font-size: 1.1rem; font-weight: 600; color: #E2E8F0;">No saved analyses found</div>
                <div style="color: #94A3B8; font-size: 0.9rem; margin-top: 6px;">
                    Upload an image on the Home dashboard or select an instant judge preset to generate your first action protocol.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.markdown(f"<span style='color: #94A3B8; font-size: 0.9rem;'>Found <b>{len(records)}</b> saved records for your account</span>", unsafe_allow_html=True)
    st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

    # Render Record Cards / Accordion
    for i, r in enumerate(records):
        rec_id = r.get("id")
        created_at = r.get("created_at", "")[:19].replace("T", " ")
        question = r.get("question", "Untitled Analysis")
        threat = r.get("threat_level", "LOW")
        ai_resp = r.get("ai_response", {})
        img_path = r.get("image_path")
        badge_html = render_threat_badge(threat)

        with st.expander(f"📋 {question[:65]}... ({created_at})", expanded=(i == 0)):
            col_info, col_del = st.columns([5, 1])
            with col_info:
                st.markdown(
                    f"""
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                        <div>{badge_html}</div>
                        <div style="font-size: 0.85rem; color: #94A3B8;">Created: {created_at} UTC</div>
                        <div style="font-size: 0.85rem; color: #64748B;">ID: {rec_id[:8]}...</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col_del:
                if st.button("🗑️ Delete", key=f"del_{rec_id}", use_container_width=True):
                    ok, err = db_svc.delete_analysis(rec_id, user_id)
                    if ok:
                        st.success("Record deleted successfully.")
                        st.rerun()
                    else:
                        st.error(f"Delete failed: {err}")

            # Show image if available via signed URL
            if img_path:
                signed_url = storage_svc.get_signed_url(img_path)
                if signed_url:
                    st.image(signed_url, caption="Secured Visual Evidence (Signed URL)", width=350)

            # Telemetry Radar
            conf = ai_resp.get("confidence_score", 85)
            render_radar(confidence_score=conf, threat_level=threat, model_name=r.get("model_name", "sarvam-gemma-4"))

            # Safety Banner
            render_safety_banner(ai_resp.get("safety_notes", []), threat)

            # Observations & Interpretation
            o_col1, o_col2 = st.columns([1, 1])
            with o_col1:
                render_observations(ai_resp.get("visual_observations", []))
            with o_col2:
                st.markdown("### 💡 Technical Interpretation")
                st.markdown(
                    f"""
                    <div class="pro-card" style="padding: 16px; font-size: 0.95rem; line-height: 1.6; color: #E2E8F0;">
                        {ai_resp.get('interpretation', 'N/A')}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Interactive Checklist
            render_interactive_checklist(ai_resp.get("next_steps", []), checklist_key_prefix=f"hist_step_{rec_id[:6]}")

            # Blind spots
            render_blindspots(ai_resp.get("uncertainty", []))

            # Download report for this record
            rep_md = generate_field_report_markdown(question, ai_resp, created_at)
            st.download_button(
                label="📄 Export Field Report (Markdown)",
                data=rep_md,
                file_name=f"report_{rec_id[:8]}.md",
                mime="text/markdown",
                key=f"rep_{rec_id}",
            )

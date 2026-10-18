"""
Home / Analysis Page for Reality -> Action AI.
Provides image upload, validation, preset triggers, live visual reasoning,
Epistemic Radar, Full AI Voice Assistant, Interactive Execution Checklist, and Field Report export.
"""

import io
from datetime import datetime, timezone
import streamlit as st
from PIL import Image

from utils.image_validation import validate_image_file
from ai_engine import AIEngine, DEMO_PRESETS
from storage import StorageService
from database import DatabaseService
from ui.components import (
    render_radar,
    render_observations,
    render_blindspots,
    render_safety_banner,
    render_interactive_checklist,
    render_voice_assistant,
    generate_field_report_markdown,
)


def render_home_page(current_user: dict):
    ai_engine = AIEngine()
    storage_svc = StorageService()
    db_svc = DatabaseService()

    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h2 class="hero-title">Visual Reality → Action Protocol</h2>
            <div class="hero-subtitle">
                Upload real-world equipment, circuits, flowcharts, or diagrams.
                Get structured, safe, step-by-step guidance powered by Sarvam AI & Gemma 4.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1-Click Judge Showcase Demo Presets
    with st.expander("⚡ Instant Judge Presets (1-Click Evaluation Scenarios)", expanded=False):
        st.markdown(
            "<span style='color: #FFFFFF; font-size: 0.95rem; font-weight: 600;'>Click any scenario below to automatically load the visual inquiry:</span>",
            unsafe_allow_html=True,
        )
        p_cols = st.columns(4)
        for i, (key, preset) in enumerate(DEMO_PRESETS.items()):
            with p_cols[i % 4]:
                if st.button(preset["title"], key=f"btn_preset_{key}", use_container_width=True):
                    st.session_state["active_preset"] = key
                    st.session_state["preset_data"] = preset
                    st.session_state["inquiry_input"] = preset["question"]
                    st.rerun()

    # Check active preset
    active_preset_key = st.session_state.get("active_preset")
    active_preset = st.session_state.get("preset_data") if active_preset_key else None

    # Main Input Columns
    col_upload, col_query = st.columns([1, 1], gap="medium")

    uploaded_bytes = None
    uploaded_ext = "png"
    uploaded_name = "image.png"

    with col_upload:
        st.markdown("<h4 style='color: #FFFFFF; font-weight: 800;'>1. Upload Visual Evidence</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Drag & drop photo or diagram (PNG, JPG, WEBP - Max 10MB)",
            type=["png", "jpg", "jpeg", "webp"],
            key="file_uploader",
        )

        if uploaded_file is not None:
            uploaded_bytes = uploaded_file.getvalue()
            uploaded_name = uploaded_file.name
            uploaded_ext = uploaded_name.split(".")[-1].lower()

            # Image validation
            is_valid, err_msg, meta = validate_image_file(uploaded_bytes, uploaded_name)
            if not is_valid:
                st.error(f"❌ Validation Error: {err_msg}")
                uploaded_bytes = None
            else:
                st.success(f"✓ Validated: {meta['format']} ({meta['width']}x{meta['height']}px - {meta['size_bytes']//1024} KB)")
                try:
                    img = Image.open(io.BytesIO(uploaded_bytes))
                    st.image(img, use_container_width=True, caption=f"Target: {uploaded_name}")
                except Exception:
                    pass
        elif active_preset:
            st.info(f"Loaded Scenario: {active_preset['title']}\n\n*{active_preset['description']}*")
            dummy_img = Image.new("RGB", (600, 400), color=(14, 21, 37))
            buf = io.BytesIO()
            dummy_img.save(buf, format="PNG")
            uploaded_bytes = buf.getvalue()
            uploaded_name = f"{active_preset_key}.png"
            uploaded_ext = "png"
            st.image(dummy_img, use_container_width=True, caption=f"Preset Scenario: {active_preset['title']}")

    with col_query:
        st.markdown("<h4 style='color: #FFFFFF; font-weight: 800;'>2. Inquiry / Operational Objective</h4>", unsafe_allow_html=True)
        
        # Initialize default inquiry in session state
        if "inquiry_input" not in st.session_state:
            st.session_state["inquiry_input"] = active_preset["question"] if active_preset else ""

        # Quick Prompt Buttons (Rendered BEFORE the text area so state can be updated safely)
        st.markdown("<span style='font-size: 0.85rem; color: #FFFFFF; font-weight: 700;'>Quick Prompts:</span>", unsafe_allow_html=True)
        pill_cols = st.columns(3)
        if pill_cols[0].button("🔍 Trace Fault", key="btn_trace_fault", use_container_width=True):
            st.session_state["inquiry_input"] = "Trace the point of failure and tell me what pins to probe with a multimeter."
            st.rerun()
        if pill_cols[1].button("🔄 Logic Flow", key="btn_logic_flow", use_container_width=True):
            st.session_state["inquiry_input"] = "Explain the decision pathways in this diagram and what happens in failover."
            st.rerun()
        if pill_cols[2].button("⚡ Safety Audit", key="btn_safety_audit", use_container_width=True):
            st.session_state["inquiry_input"] = "Perform a safety risk inspection and list required precautions before touching."
            st.rerun()

        # The text area
        user_question = st.text_area(
            "What do you need to solve, inspect, or verify?",
            value=st.session_state.get("inquiry_input", ""),
            placeholder="e.g. What burned on this circuit board and how do I replace it safely?",
            height=130,
            key="user_inquiry_text",
        )

        st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)
        analyze_btn = st.button("⚡ Analyze & Generate Action Protocol", use_container_width=True)

    # Execution Trigger
    if analyze_btn:
        if not uploaded_bytes:
            st.warning("⚠️ Please upload an image or choose one of the instant judge presets above.")
            return
        if not user_question.strip():
            st.warning("⚠️ Please enter a question or operational objective.")
            return

        with st.spinner("🤖 Sarvam AI & Gemma 4 analyzing visual evidence..."):
            if active_preset and not ai_engine.config.is_sarvam_configured:
                res = {
                    "success": True,
                    "data": active_preset["response"],
                    "error": None,
                    "is_mock": True,
                }
            else:
                res = ai_engine.analyze_image(uploaded_bytes, user_question, uploaded_ext)

        if not res["success"]:
            st.error(f"❌ Analysis Notice: {res['error']}")
            return

        ai_data = res["data"]
        threat_level = ai_data.get("threat_level", "LOW")

        # Save to Storage & Database
        user_id = current_user.get("id", "demo-user")
        upload_ok, img_path, storage_err = storage_svc.upload_image(
            file_bytes=uploaded_bytes,
            user_id=user_id,
            extension=uploaded_ext,
            content_type=f"image/{uploaded_ext}",
        )

        db_ok, record_id, db_err = db_svc.save_analysis(
            user_id=user_id,
            question=user_question,
            image_path=img_path if upload_ok else None,
            ai_response=ai_data,
            threat_level=threat_level,
            model_name="sarvam-gemma-4",
        )

        st.session_state["active_result"] = {
            "ai_data": ai_data,
            "question": user_question,
            "threat_level": threat_level,
            "image_path": img_path,
            "record_id": record_id,
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "is_mock": res.get("is_mock", False),
        }

    # Render Active Analysis Results Area
    active_result = st.session_state.get("active_result")
    if active_result:
        st.markdown("<hr style='border: 1px solid rgba(0,240,255,0.3); margin: 30px 0;'>", unsafe_allow_html=True)
        
        ai_data = active_result["ai_data"]
        threat = active_result["threat_level"]
        conf = ai_data.get("confidence_score", 88)

        # 1. AI Voice Assistant Panel (Mic Speech Input + Spoken Audio Briefing)
        render_voice_assistant(active_result["question"], ai_data)

        # 2. Epistemic Radar & Confidence Score
        render_radar(confidence_score=conf, threat_level=threat, model_name="sarvam-gemma-4")

        # 3. Mandatory Safety Checkpoint Gate
        render_safety_banner(ai_data.get("safety_notes", []), threat)

        # 4. Two-column breakdown: Observations & Technical Interpretation
        res_col1, res_col2 = st.columns([1, 1], gap="medium")
        with res_col1:
            render_observations(ai_data.get("visual_observations", []))
        with res_col2:
            st.markdown("### 💡 Technical Interpretation")
            st.markdown(
                f"""
                <div class="pro-card" style="padding: 20px; font-size: 1.05rem; line-height: 1.65; color: #FFFFFF; font-weight: 500;">
                    {ai_data.get('interpretation', 'Analysis completed.')}
                </div>
                """,
                unsafe_allow_html=True,
            )

        # 5. Interactive Step-by-Step Action Protocol (Execution Mode)
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        render_interactive_checklist(ai_data.get("next_steps", []), checklist_key_prefix="act_step")

        # 6. Visual Uncertainties & Blind Spots
        render_blindspots(ai_data.get("uncertainty", []))

        # 7. Follow-up Diagnostic Inquiries
        follow_ups = ai_data.get("follow_up_questions", [])
        if follow_ups:
            st.markdown("### ❓ Follow-up Inquiries to Verify")
            for q in follow_ups:
                st.markdown(f"- <span style='font-size: 1rem; color: #FFFFFF; font-weight: 600;'>🔎 {q}</span>", unsafe_allow_html=True)

        # 8. Action Bar: Field Report Export & New Analysis
        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        act_col1, act_col2 = st.columns([1, 1])
        with act_col1:
            report_md = generate_field_report_markdown(
                active_result["question"],
                ai_data,
                active_result["timestamp"],
            )
            st.download_button(
                label="📄 Export Field Inspection Report (Markdown)",
                data=report_md,
                file_name=f"inspection_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown",
                use_container_width=True,
            )
        with act_col2:
            if st.button("🔄 Start New Analysis", use_container_width=True):
                st.session_state["active_result"] = None
                st.session_state["active_preset"] = None
                st.session_state["preset_data"] = None
                st.session_state["inquiry_input"] = ""
                st.rerun()

"""
Reusable UI Components for Reality -> Action AI.
Renders Epistemic Radar, Threat Badges, Interactive Checklists,
Safety Gates, Field Report Exporters, and Judge Preset Selectors.
"""

import streamlit as st
from typing import List, Dict, Any, Optional
from ui.styles import render_tts_audio_script


def render_header(current_user: Optional[Dict[str, Any]] = None):
    """Renders top branding bar with system status and user state."""
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <div style="
                    width: 38px; height: 38px; 
                    background: linear-gradient(135deg, #00F0FF 0%, #A855F7 100%); 
                    border-radius: 10px; 
                    display: flex; align-items: center; justify-content: center;
                    box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
                    font-size: 1.2rem;
                ">⚡</div>
                <div>
                    <h1 class="hero-title" style="margin: 0; font-size: 1.8rem !important;">Reality → Action AI</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        if current_user:
            email = current_user.get("email", "Authenticated User")
            is_demo = current_user.get("is_demo", False)
            mode_badge = (
                '<span style="background: rgba(168,85,247,0.2); color: #C084FC; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem; border: 1px solid rgba(168,85,247,0.4);">SHOWCASE DEMO</span>'
                if is_demo
                else '<span style="background: rgba(16,185,129,0.2); color: #34D399; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem; border: 1px solid rgba(16,185,129,0.4);">SUPABASE AUTH</span>'
            )
            st.markdown(
                f"""
                <div style="text-align: right; padding-top: 10px;">
                    <div style="font-size: 0.85rem; color: #94A3B8;">{email} {mode_badge}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_threat_badge(threat_level: str) -> str:
    """Returns HTML for threat badge."""
    level = (threat_level or "LOW").upper()
    if level == "CRITICAL":
        return '<span class="badge-critical">🔴 CRITICAL HAZARD</span>'
    elif level == "CAUTION":
        return '<span class="badge-caution">🟡 CAUTION REQUIRED</span>'
    return '<span class="badge-low">🟢 LOW RISK</span>'


def render_radar(confidence_score: int, threat_level: str, model_name: str = "sarvam-gemma-4"):
    """Renders the Epistemic Radar with confidence gauge & threat metrics."""
    threat_badge_html = render_threat_badge(threat_level)
    
    st.markdown(
        f"""
        <div class="radar-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: #00F0FF; font-weight: 700; font-size: 0.9rem; letter-spacing: 0.05em;">EPISTEMIC RADAR & TELEMETRY</span>
                </div>
                <div>{threat_badge_html}</div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px;">
                <div class="metric-box">
                    <span class="metric-title">Visual Confidence</span>
                    <span class="metric-value">{confidence_score}%</span>
                </div>
                <div class="metric-box">
                    <span class="metric-title">Reasoning Model</span>
                    <span class="metric-value" style="font-size: 1rem; color: #E2E8F0; margin-top: 6px;">{model_name}</span>
                </div>
                <div class="metric-box">
                    <span class="metric-title">Verification Gate</span>
                    <span class="metric-value" style="font-size: 1.1rem; color: #34D399; margin-top: 4px;">PASS</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_observations(observations: List[str]):
    """Renders structured visual observations as tag cards."""
    st.markdown("### 🔍 What I Can Definitively See")
    obs_html = '<div style="margin-bottom: 16px;">'
    for obs in observations:
        obs_html += f'<div class="obs-tag">👁️ {obs}</div>'
    obs_html += "</div>"
    st.markdown(obs_html, unsafe_allow_html=True)


def render_blindspots(uncertainties: List[str]):
    """Renders epistemic uncertainties and blind-spot callouts."""
    if not uncertainties:
        return
    st.markdown("### ⚠️ Blind Spots & Visual Uncertainties")
    items_html = "".join([f"<li style='margin-bottom: 6px;'>{u}</li>" for u in uncertainties])
    st.markdown(
        f"""
        <div class="blindspot-box">
            <div style="color: #FBBF24; font-weight: 700; margin-bottom: 6px; font-size: 0.95rem;">
                VISUAL LIMITATIONS & OBSCURED DETAILS
            </div>
            <div style="color: #CBD5E1; font-size: 0.9rem;">
                <ul style="padding-left: 20px; margin: 0;">
                    {items_html}
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_safety_banner(safety_notes: List[str], threat_level: str):
    """Renders safety precautions and high-risk gate."""
    if not safety_notes:
        return
    st.markdown("### 🛡️ Safety Considerations & Precautions")
    notes_html = "".join([f"<li style='margin-bottom: 8px;'>{n}</li>" for n in safety_notes])
    box_class = "safety-alert-box" if threat_level.upper() in ["CRITICAL", "CAUTION"] else "blindspot-box"
    title_color = "#F87171" if threat_level.upper() == "CRITICAL" else "#FBBF24"
    st.markdown(
        f"""
        <div class="{box_class}">
            <div style="color: {title_color}; font-weight: 800; margin-bottom: 8px; font-size: 0.95rem; letter-spacing: 0.03em;">
                NON-NEGOTIABLE SAFETY PROTOCOLS
            </div>
            <div style="color: #F1F5F9; font-size: 0.92rem;">
                <ul style="padding-left: 20px; margin: 0;">
                    {notes_html}
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_interactive_checklist(steps: List[str], checklist_key_prefix: str = "step"):
    """
    Renders action steps as an interactive checklist with real-time completion tracking.
    Also renders the Hands-Free Audio narration trigger.
    """
    st.markdown("### 🛠️ Step-by-Step Action Protocol (Execution Mode)")
    
    # Audio narration trigger
    all_steps_text = ". ".join(steps)
    st.markdown(render_tts_audio_script(all_steps_text), unsafe_allow_html=True)

    completed_count = 0
    total_steps = len(steps)

    for i, step in enumerate(steps):
        key = f"{checklist_key_prefix}_{i}"
        is_done = st.session_state.get(key, False)
        if is_done:
            completed_count += 1

        col_check, col_text = st.columns([1, 15])
        with col_check:
            st.checkbox("", key=key, label_visibility="collapsed")
        with col_text:
            step_style = "text-decoration: line-through; opacity: 0.6;" if is_done else ""
            st.markdown(
                f"""
                <div class="step-container">
                    <div class="step-num">{i + 1}</div>
                    <div class="step-text" style="{step_style}">{step}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Progress Bar
    if total_steps > 0:
        progress_val = completed_count / total_steps
        st.progress(progress_val)
        st.markdown(
            f"<div style='font-size: 0.85rem; color: #38BDF8; font-weight: 600; text-align: right;'>Protocol Progress: {completed_count}/{total_steps} Steps Executed ({int(progress_val * 100)}%)</div>",
            unsafe_allow_html=True,
        )


def generate_field_report_markdown(
    question: str,
    ai_data: Dict[str, Any],
    timestamp: str,
) -> str:
    """Compiles complete analysis into a standardized Markdown field inspection report."""
    threat = ai_data.get("threat_level", "LOW")
    conf = ai_data.get("confidence_score", 85)
    obs = "\n".join([f"- {o}" for o in ai_data.get("visual_observations", [])])
    steps = "\n".join([f"{i+1}. {s}" for i, s in enumerate(ai_data.get("next_steps", []))])
    safety = "\n".join([f"- ⚠️ {s}" for s in ai_data.get("safety_notes", [])])
    uncertain = "\n".join([f"- ❓ {u}" for u in ai_data.get("uncertainty", [])])

    return f"""# REALITY → ACTION AI: FIELD INSPECTION REPORT
**Timestamp:** {timestamp}
**Threat Assessment:** {threat}
**Visual Confidence Score:** {conf}%
**Inquiry / Objective:** {question}

---

## 1. Objective Visual Observations
{obs}

## 2. Technical Interpretation
{ai_data.get('interpretation', 'N/A')}

## 3. Mandatory Safety Directives
{safety}

## 4. Operational Step-by-Step Action Protocol
{steps}

## 5. Epistemic Uncertainties & Visual Blind Spots
{uncertain}

---
*Report generated automatically by Reality → Action AI. Exercise verified engineering judgment before touching energized, pressurized, or mechanical equipment.*
"""

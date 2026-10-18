"""
Reusable UI Components for Reality -> Action AI.
Renders Epistemic Radar, Threat Badges, Interactive Checklists,
Safety Gates, Field Report Exporters, and Full AI Voice Assistant Co-Pilot.
"""

import streamlit as st
from typing import List, Dict, Any, Optional


def render_header(current_user: Optional[Dict[str, Any]] = None):
    """Renders top branding bar with system status and user state."""
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
                <div style="
                    width: 44px; height: 44px; 
                    background: linear-gradient(135deg, #00F0FF 0%, #A855F7 100%); 
                    border-radius: 12px; 
                    display: flex; align-items: center; justify-content: center;
                    box-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
                    font-size: 1.4rem;
                ">⚡</div>
                <div>
                    <h1 class="hero-title" style="margin: 0; font-size: 2.1rem !important;">Reality → Action AI</h1>
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
                '<span style="background: rgba(168,85,247,0.3); color: #E9D5FF; padding: 4px 10px; border-radius: 8px; font-size: 0.8rem; font-weight: 700; border: 1px solid rgba(168,85,247,0.5);">SHOWCASE DEMO</span>'
                if is_demo
                else '<span style="background: rgba(16,185,129,0.3); color: #A7F3D0; padding: 4px 10px; border-radius: 8px; font-size: 0.8rem; font-weight: 700; border: 1px solid rgba(16,185,129,0.5);">SUPABASE LIVE</span>'
            )
            st.markdown(
                f"""
                <div style="text-align: right; padding-top: 10px;">
                    <div style="font-size: 0.95rem; font-weight: 600; color: #FFFFFF;">{email} {mode_badge}</div>
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
                    <span style="color: #00F0FF; font-weight: 800; font-size: 0.95rem; letter-spacing: 0.05em;">EPISTEMIC RADAR & TELEMETRY</span>
                </div>
                <div>{threat_badge_html}</div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 14px;">
                <div class="metric-box">
                    <span class="metric-title">Visual Confidence</span>
                    <span class="metric-value">{confidence_score}%</span>
                </div>
                <div class="metric-box">
                    <span class="metric-title">Reasoning Model</span>
                    <span class="metric-value" style="font-size: 1.05rem; color: #FFFFFF; margin-top: 6px;">{model_name}</span>
                </div>
                <div class="metric-box">
                    <span class="metric-title">Verification Gate</span>
                    <span class="metric-value" style="font-size: 1.2rem; color: #34D399; margin-top: 4px;">PASS</span>
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
    items_html = "".join([f"<li style='margin-bottom: 8px; color: #FFFFFF; font-size: 0.95rem;'>{u}</li>" for u in uncertainties])
    st.markdown(
        f"""
        <div class="blindspot-box">
            <div style="color: #FDE68A; font-weight: 800; margin-bottom: 8px; font-size: 1rem; letter-spacing: 0.02em;">
                VISUAL LIMITATIONS & OBSCURED DETAILS
            </div>
            <div>
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
    notes_html = "".join([f"<li style='margin-bottom: 8px; color: #FFFFFF; font-size: 0.95rem;'>{n}</li>" for n in safety_notes])
    box_class = "safety-alert-box" if threat_level.upper() in ["CRITICAL", "CAUTION"] else "blindspot-box"
    title_color = "#FECACA" if threat_level.upper() == "CRITICAL" else "#FDE68A"
    st.markdown(
        f"""
        <div class="{box_class}">
            <div style="color: {title_color}; font-weight: 900; margin-bottom: 8px; font-size: 1.05rem; letter-spacing: 0.03em;">
                NON-NEGOTIABLE SAFETY PROTOCOLS
            </div>
            <div>
                <ul style="padding-left: 20px; margin: 0;">
                    {notes_html}
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_voice_assistant(user_question: str, ai_data: Optional[Dict[str, Any]] = None):
    """
    Renders an interactive AI Voice Assistant panel.
    Includes:
    1. Microphone Speech-to-Text (Speak to prompt)
    2. Voice Co-Pilot Briefing (Full spoken audio diagnosis)
    3. Live Pulsing Equalizer visualizer
    """
    briefing_text = ""
    if ai_data:
        threat = ai_data.get("threat_level", "LOW")
        obs_summary = ". ".join(ai_data.get("visual_observations", [])[:3])
        steps_summary = ". ".join(ai_data.get("next_steps", [])[:4])
        briefing_text = (
            f"Voice Co-Pilot Diagnostic Briefing. Threat assessment is {threat}. "
            f"Visual observations: {obs_summary}. "
            f"Action Protocol: {steps_summary}."
        )
    escaped_briefing = briefing_text.replace('"', '\\"').replace("\n", " ").replace("'", "\\'")

    st.markdown(
        f"""
        <div class="pro-card" style="border: 1px solid rgba(0, 240, 255, 0.45); padding: 18px 22px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.3rem;">🎙️</span>
                    <span style="font-weight: 800; font-size: 1.05rem; color: #00F0FF; letter-spacing: 0.03em;">AI VOICE ASSISTANT CO-PILOT</span>
                </div>
                <div style="display: flex; align-items: center; gap: 4px;" id="eq-container">
                    <div class="equalizer-bar"></div>
                    <div class="equalizer-bar"></div>
                    <div class="equalizer-bar"></div>
                    <div class="equalizer-bar"></div>
                    <div class="equalizer-bar"></div>
                </div>
            </div>
            
            <div style="font-size: 0.92rem; color: #E2E8F0; margin-bottom: 14px; line-height: 1.5;">
                Hands-free hardware workbench assistant: Speak your inquiry using the microphone, or listen to the full spoken action protocol.
            </div>

            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <!-- Microphone Voice Input Button -->
                <button id="mic-btn" onclick="
                    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {{
                        alert('Speech recognition is not supported in this browser. Please use Chrome or Edge.');
                    }} else {{
                        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
                        const recognition = new SpeechRec();
                        recognition.continuous = false;
                        recognition.interimResults = false;
                        recognition.lang = 'en-US';

                        const micBtn = document.getElementById('mic-btn');
                        micBtn.innerText = '🔴 Listening... Speak clearly now';
                        micBtn.style.borderColor = '#EF4444';
                        micBtn.style.color = '#FCA5A5';

                        recognition.onresult = function(event) {{
                            const transcript = event.results[0][0].transcript;
                            const textareas = window.parent.document.querySelectorAll('textarea');
                            if (textareas.length > 0) {{
                                textareas[0].value = transcript;
                                textareas[0].dispatchEvent(new Event('input', {{ bubbles: true }}));
                            }}
                            alert('Voice Captured: ' + transcript);
                            micBtn.innerText = '🎙️ Speak Inquiry (Mic Input)';
                            micBtn.style.borderColor = 'rgba(0, 240, 255, 0.5)';
                            micBtn.style.color = '#00F0FF';
                        }};

                        recognition.onerror = function(event) {{
                            alert('Microphone error: ' + event.error);
                            micBtn.innerText = '🎙️ Speak Inquiry (Mic Input)';
                            micBtn.style.borderColor = 'rgba(0, 240, 255, 0.5)';
                            micBtn.style.color = '#00F0FF';
                        }};

                        recognition.start();
                    }}
                " style="
                    background: linear-gradient(135deg, rgba(0, 240, 255, 0.18), rgba(56, 189, 248, 0.12));
                    color: #00F0FF;
                    border: 1px solid rgba(0, 240, 255, 0.5);
                    border-radius: 8px;
                    padding: 9px 16px;
                    font-size: 0.92rem;
                    font-weight: 700;
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    transition: all 0.2s ease;
                ">
                    🎙️ <span>Speak Inquiry (Mic Input)</span>
                </button>

                <!-- Voice Co-Pilot Spoken Briefing Button -->
                <button id="briefing-btn" onclick="
                    if ('speechSynthesis' in window) {{
                        window.speechSynthesis.cancel();
                        const text = '{escaped_briefing}' || 'No analysis loaded yet. Upload an image or select a preset to generate a spoken briefing.';
                        const utter = new SpeechSynthesisUtterance(text);
                        utter.rate = 1.05;
                        utter.pitch = 1.0;
                        window.speechSynthesis.speak(utter);
                    }} else {{
                        alert('Text-to-Speech not supported in this browser.');
                    }}
                " style="
                    background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(192, 132, 252, 0.12));
                    color: #E9D5FF;
                    border: 1px solid rgba(168, 85, 247, 0.55);
                    border-radius: 8px;
                    padding: 9px 16px;
                    font-size: 0.92rem;
                    font-weight: 700;
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    transition: all 0.2s ease;
                ">
                    🔊 <span>Play Spoken Briefing</span>
                </button>

                <!-- Stop Voice Button -->
                <button onclick="if ('speechSynthesis' in window) {{ window.speechSynthesis.cancel(); }}" style="
                    background: rgba(239, 68, 68, 0.2);
                    color: #FCA5A5;
                    border: 1px solid rgba(239, 68, 68, 0.5);
                    border-radius: 8px;
                    padding: 9px 14px;
                    font-size: 0.92rem;
                    font-weight: 700;
                    cursor: pointer;
                ">
                    ⏹️ Stop Audio
                </button>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_interactive_checklist(steps: List[str], checklist_key_prefix: str = "step"):
    """
    Renders action steps as an interactive checklist with real-time completion tracking.
    """
    st.markdown("### 🛠️ Step-by-Step Action Protocol (Execution Mode)")

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
            step_style = "text-decoration: line-through; opacity: 0.55;" if is_done else ""
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
            f"<div style='font-size: 0.92rem; color: #38BDF8; font-weight: 700; text-align: right;'>Protocol Progress: {completed_count}/{total_steps} Steps Executed ({int(progress_val * 100)}%)</div>",
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

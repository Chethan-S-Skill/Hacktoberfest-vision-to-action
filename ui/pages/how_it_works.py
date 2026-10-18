"""
How It Works & Safety Guidelines for Reality -> Action AI.
Explains the 5-pillar architecture, epistemic framework, and real-world safety policies.
"""

import streamlit as st


def render_how_it_works_page():
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h2 class="hero-title" style="font-size: 2.2rem !important;">System Architecture & Safety Protocols</h2>
            <div class="hero-subtitle">
                How Reality → Action AI bridges visual intelligence and safe physical execution.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 5 Pillars Grid
    st.markdown("### 🏛️ The 5 Pillars of Action AI")
    
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown(
            """
            <div class="pro-card">
                <div style="font-size: 1.2rem; font-weight: 700; color: #00F0FF; margin-bottom: 8px;">
                    1. Epistemic Separation of Facts
                </div>
                <div style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.6;">
                    Most vision systems hallucinate obscured details. Reality → Action AI enforces a strict boundary between 
                    <b>verifiable visual observations</b> and <b>contextual hypotheses</b>, surfacing blind spots before any action is taken.
                </div>
            </div>
            <div class="pro-card">
                <div style="font-size: 1.2rem; font-weight: 700; color: #38BDF8; margin-bottom: 8px;">
                    2. Physical Safety Guardrails
                </div>
                <div style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.6;">
                    Equipped with a hazard detection triage that detects high voltage, pressurized hydraulics, rotating machinery, and chemical risks. 
                    Enforces non-negotiable safety checkpoints and warns against hazardous blind repairs.
                </div>
            </div>
            <div class="pro-card">
                <div style="font-size: 1.2rem; font-weight: 700; color: #A855F7; margin-bottom: 8px;">
                    3. Interactive Execution Mode
                </div>
                <div style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.6;">
                    Transforms static text recommendations into dynamic, checkable tasks with real-time completion tracking and hands-free 
                    <b>Web Speech Audio narration</b> for workbench technicians and students holding multimeter probes.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="pro-card">
                <div style="font-size: 1.2rem; font-weight: 700; color: #34D399; margin-bottom: 8px;">
                    4. Sarvam AI & Gemma 4 Vision Engine
                </div>
                <div style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.6;">
                    Utilizes multimodal reasoning optimized for circuit topology, mechanical equipment, and schematic diagrams with structured JSON schema outputs.
                </div>
            </div>
            <div class="pro-card">
                <div style="font-size: 1.2rem; font-weight: 700; color: #F59E0B; margin-bottom: 8px;">
                    5. Enterprise Privacy & Row Level Security
                </div>
                <div style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.6;">
                    Integrated with Supabase Auth, PostgreSQL RLS policies, and private bucket storage. Images are accessible solely through short-lived signed URLs, guaranteeing zero cross-user data leakage.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    st.markdown("### ⚠️ Physical Safety Directives")
    st.markdown(
        """
        <div class="safety-alert-box">
            <h4 style="color: #F87171; margin-top: 0; font-size: 1.05rem;">CRITICAL OPERATIONAL RULES:</h4>
            <ul style="color: #F1F5F9; font-size: 0.92rem; line-height: 1.6;">
                <li><b>Never touch energized equipment:</b> Always verify zero potential using a calibrated multimeter or test lamp before touching electrical conductors.</li>
                <li><b>Never open pressurized lines:</b> Ensure accumulators are dumped and pressure gauges read zero bar before loosening hydraulic or pneumatic fittings.</li>
                <li><b>No automated code execution:</b> Model suggestions must never be piped directly into shell commands or hardware actuators without human-in-the-loop verification.</li>
                <li><b>No medical diagnostics:</b> This application provides engineering and technical guidance; it does not replace medical or certified trade professionals.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

"""
Design System and Custom CSS Styles for Reality -> Action AI.
Implements maximum text contrast, ultra-legible typography,
cyber-industrial glassmorphism, glowing telemetry, and voice assistant animations.
"""

PRO_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap');

/* Global Root Colors & Variables */
:root {
    --bg-main: #060911;
    --bg-card: rgba(13, 20, 36, 0.92);
    --bg-card-hover: rgba(20, 32, 58, 0.96);
    --border-card: rgba(56, 189, 248, 0.28);
    --border-glow: rgba(0, 240, 255, 0.5);
    
    --accent-cyan: #00F0FF;
    --accent-blue: #38BDF8;
    --accent-violet: #A855F7;
    --accent-emerald: #10B981;
    --accent-amber: #FBBF24;
    --accent-red: #F87171;
    
    --text-primary: #FFFFFF;
    --text-secondary: #E2E8F0;
    --text-muted: #CBD5E1;
}

/* Background Atmosphere */
.stApp {
    background-color: var(--bg-main) !important;
    background-image: 
        radial-gradient(circle at 10% 10%, rgba(168, 85, 247, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 90% 90%, rgba(0, 240, 255, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.08) 0%, transparent 75%) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: #FFFFFF !important;
}

/* Force Absolute Text Contrast Across All Markdown & Widgets */
p, span, div, li, td, th {
    color: #F1F5F9 !important;
}

/* Modern High-Contrast Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em !important;
    color: #FFFFFF !important;
}

/* Hero Title with Electric Gradient */
.hero-title {
    font-size: 2.75rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 60%, #C084FC 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    margin-bottom: 0.25rem !important;
    letter-spacing: -0.03em !important;
    display: inline-block;
}

.hero-subtitle {
    font-size: 1.15rem !important;
    color: #E2E8F0 !important;
    margin-bottom: 1.5rem !important;
    font-weight: 500 !important;
    line-height: 1.6 !important;
}

/* Ultra-Readable Form Labels */
label, 
label p, 
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.01em !important;
}

/* Text Input & Text Area Fixes */
input[type="text"], 
input[type="password"], 
textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background-color: #0B132B !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(0, 240, 255, 0.4) !important;
    border-radius: 10px !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    padding: 12px 14px !important;
}

input::placeholder, 
textarea::placeholder {
    color: #94A3B8 !important;
    opacity: 1 !important;
}

input:focus, 
textarea:focus {
    border-color: #00F0FF !important;
    box-shadow: 0 0 12px rgba(0, 240, 255, 0.45) !important;
}

/* High-Contrast Tab Buttons */
button[data-baseweb="tab"] {
    background-color: rgba(14, 21, 37, 0.7) !important;
    color: #E2E8F0 !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 10px 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-bottom: none !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(180deg, rgba(0, 240, 255, 0.15) 0%, rgba(14, 21, 37, 0.95) 100%) !important;
    color: #00F0FF !important;
    border: 1px solid #00F0FF !important;
    border-bottom: 2px solid #00F0FF !important;
    box-shadow: 0 -4px 12px rgba(0, 240, 255, 0.25) !important;
}

button[data-baseweb="tab"] p {
    color: inherit !important;
    font-weight: inherit !important;
    font-size: inherit !important;
}

/* Expander Overhaul */
div[data-testid="stExpander"] {
    background: rgba(14, 21, 37, 0.85) !important;
    border: 1px solid rgba(56, 189, 248, 0.35) !important;
    border-radius: 12px !important;
    margin-bottom: 18px !important;
}

div[data-testid="stExpander"] summary {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    padding: 14px 18px !important;
}

div[data-testid="stExpander"] summary p,
div[data-testid="stExpander"] summary span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

div[data-testid="stExpander"] summary:hover {
    color: #00F0FF !important;
}

/* File Uploader Fixes */
[data-testid="stFileUploader"] {
    background: rgba(14, 21, 37, 0.75) !important;
    border: 2px dashed rgba(0, 240, 255, 0.45) !important;
    border-radius: 14px !important;
    padding: 20px !important;
}

[data-testid="stFileUploader"] section {
    background: transparent !important;
}

[data-testid="stFileUploader"] span, 
[data-testid="stFileUploader"] small, 
[data-testid="stFileUploader"] button {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* Glassmorphism Cards */
.pro-card {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-card) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7), 0 0 1px 1px rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    margin-bottom: 20px !important;
}

.pro-card:hover {
    border-color: rgba(0, 240, 255, 0.5) !important;
    box-shadow: 0 14px 40px -10px rgba(0, 240, 255, 0.2), 0 0 18px rgba(56, 189, 248, 0.25) !important;
    transform: translateY(-2px) !important;
}

/* Radar & Telemetry Card */
.radar-card {
    background: linear-gradient(135deg, rgba(14, 21, 37, 0.95) 0%, rgba(20, 32, 58, 0.9) 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.4) !important;
    border-radius: 16px !important;
    padding: 22px !important;
    margin-bottom: 22px !important;
    position: relative !important;
    overflow: hidden !important;
}

.radar-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00F0FF, #A855F7) !important;
}

/* Threat Badges */
.badge-low {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(16, 185, 129, 0.25) !important;
    color: #6EE7B7 !important;
    border: 1px solid rgba(16, 185, 129, 0.6) !important;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.9rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.badge-caution {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245, 158, 11, 0.25) !important;
    color: #FDE68A !important;
    border: 1px solid rgba(245, 158, 11, 0.6) !important;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.9rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.badge-critical {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(239, 68, 68, 0.3) !important;
    color: #FECACA !important;
    border: 1px solid rgba(239, 68, 68, 0.7) !important;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.9rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    animation: pulseGlow 1.8s infinite;
}

@keyframes pulseGlow {
    0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.5); }
    70% { box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
    100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

/* Metric Display Unit */
.metric-box {
    display: flex;
    flex-direction: column;
    padding: 14px 18px;
    background: rgba(10, 16, 32, 0.85) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 12px;
}

.metric-title {
    font-size: 0.8rem !important;
    color: #94A3B8 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 700 !important;
    margin-bottom: 4px;
}

.metric-value {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.6rem !important;
    font-weight: 900 !important;
    color: #00F0FF !important;
}

/* Interactive Action Step Cards */
.step-container {
    background: rgba(14, 22, 42, 0.85) !important;
    border: 1px solid rgba(56, 189, 248, 0.28) !important;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    gap: 16px;
    transition: all 0.25s ease;
}

.step-container:hover {
    border-color: rgba(0, 240, 255, 0.6) !important;
    background: rgba(22, 34, 62, 0.95) !important;
    box-shadow: 0 4px 16px rgba(0, 240, 255, 0.15) !important;
}

.step-num {
    background: linear-gradient(135deg, #00F0FF, #3B82F6) !important;
    color: #060911 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 900 !important;
    font-size: 1rem !important;
    width: 32px;
    height: 32px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
}

.step-text {
    font-size: 1.02rem !important;
    color: #FFFFFF !important;
    font-weight: 500 !important;
    line-height: 1.6 !important;
    flex-grow: 1;
}

/* Observation Pill Tags */
.obs-tag {
    display: inline-block;
    background: rgba(14, 165, 233, 0.18) !important;
    border: 1px solid rgba(56, 189, 248, 0.45) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 0.92rem !important;
    margin: 4px 6px 4px 0;
    line-height: 1.5;
}

/* Uncertainty Warning Box */
.blindspot-box {
    background: rgba(245, 158, 11, 0.12) !important;
    border: 1px solid rgba(245, 158, 11, 0.4) !important;
    border-left: 5px solid #F59E0B !important;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin: 16px 0;
}

/* Safety Critical Alert Box */
.safety-alert-box {
    background: rgba(239, 68, 68, 0.15) !important;
    border: 1px solid rgba(239, 68, 68, 0.5) !important;
    border-left: 6px solid #EF4444 !important;
    border-radius: 8px;
    padding: 18px 22px;
    margin: 18px 0;
}

/* High-Contrast Action Buttons */
.stButton>button {
    background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
    padding: 12px 26px !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 16px 0 rgba(37, 99, 235, 0.45) !important;
    transition: all 0.25s ease !important;
}

.stButton>button p,
.stButton>button span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: inherit !important;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #1D4ED8 0%, #6D28D9 100%) !important;
    box-shadow: 0 6px 24px 0 rgba(0, 240, 255, 0.5) !important;
    border-color: #00F0FF !important;
    transform: translateY(-2px) !important;
}

/* Sidebar Styling & Contrast */
section[data-testid="stSidebar"] {
    background-color: #060911 !important;
    border-right: 1px solid rgba(56, 189, 248, 0.2) !important;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
section[data-testid="stSidebar"] span {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding: 10px 14px !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(0, 240, 255, 0.1) !important;
}

/* Voice Assistant Equalizer Animation */
.equalizer-bar {
    display: inline-block;
    width: 4px;
    height: 18px;
    background: #00F0FF;
    border-radius: 2px;
    margin: 0 2px;
    animation: eqWave 1.2s infinite ease-in-out;
}

.equalizer-bar:nth-child(2) { animation-delay: 0.2s; height: 26px; background: #38BDF8; }
.equalizer-bar:nth-child(3) { animation-delay: 0.4s; height: 14px; background: #A855F7; }
.equalizer-bar:nth-child(4) { animation-delay: 0.6s; height: 22px; background: #C084FC; }
.equalizer-bar:nth-child(5) { animation-delay: 0.8s; height: 16px; background: #00F0FF; }

@keyframes eqWave {
    0%, 100% { transform: scaleY(0.4); }
    50% { transform: scaleY(1.2); }
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #060911;
}
::-webkit-scrollbar-thumb {
    background: rgba(56, 189, 248, 0.35);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: #00F0FF;
}
</style>
"""

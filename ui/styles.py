"""
Design System and Custom CSS Styles for Reality -> Action AI.
Implements a state-of-the-art cyber-industrial aesthetic with deep space navy background,
electric blue & violet neon gradients, glassmorphism, glowing telemetry cards, and typography.
"""

PRO_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* Global Root Colors & Variables */
:root {
    --bg-main: #070A10;
    --bg-card: rgba(14, 21, 37, 0.75);
    --bg-card-hover: rgba(20, 30, 54, 0.85);
    --border-card: rgba(56, 189, 248, 0.15);
    --border-glow: rgba(0, 240, 255, 0.4);
    
    --accent-cyan: #00F0FF;
    --accent-blue: #38BDF8;
    --accent-violet: #A855F7;
    --accent-emerald: #10B981;
    --accent-amber: #F59E0B;
    --accent-red: #EF4444;
    
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
}

/* Background Atmosphere */
.stApp {
    background-color: var(--bg-main) !important;
    background-image: 
        radial-gradient(circle at 15% 15%, rgba(168, 85, 247, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(0, 240, 255, 0.10) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.05) 0%, transparent 70%) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-primary) !important;
}

/* Modern Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
}

/* Hero Title with Electric Gradient */
.hero-title {
    font-size: 2.75rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 50%, #A855F7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.25rem !important;
    letter-spacing: -0.03em;
    display: inline-block;
}

.hero-subtitle {
    font-size: 1.15rem;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    font-weight: 400;
    line-height: 1.6;
}

/* Glassmorphism Cards */
.pro-card {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5), 0 0 1px 1px rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    margin-bottom: 20px;
}

.pro-card:hover {
    border-color: rgba(56, 189, 248, 0.35);
    box-shadow: 0 14px 40px -10px rgba(0, 240, 255, 0.12), 0 0 15px rgba(56, 189, 248, 0.15);
    transform: translateY(-2px);
}

/* Radar & Telemetry Card */
.radar-card {
    background: linear-gradient(135deg, rgba(14, 21, 37, 0.9) 0%, rgba(20, 30, 54, 0.8) 100%);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
}

.radar-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #00F0FF, #A855F7);
}

/* Threat Badges */
.badge-low {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(16, 185, 129, 0.15);
    color: #34D399;
    border: 1px solid rgba(16, 185, 129, 0.35);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.badge-caution {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245, 158, 11, 0.15);
    color: #FBBF24;
    border: 1px solid rgba(245, 158, 11, 0.35);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.badge-critical {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(239, 68, 68, 0.2);
    color: #F87171;
    border: 1px solid rgba(239, 68, 68, 0.45);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    animation: pulseGlow 2s infinite;
}

@keyframes pulseGlow {
    0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4); }
    70% { box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); }
    100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

/* Metric Display Unit */
.metric-box {
    display: flex;
    flex-direction: column;
    padding: 14px 18px;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
}

.metric-title {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
    margin-bottom: 4px;
}

.metric-value {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--accent-cyan);
}

/* Interactive Action Step Cards */
.step-container {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(56, 189, 248, 0.18);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    gap: 16px;
    transition: all 0.25s ease;
}

.step-container:hover {
    border-color: rgba(0, 240, 255, 0.4);
    background: rgba(20, 30, 54, 0.75);
}

.step-num {
    background: linear-gradient(135deg, #00F0FF, #3B82F6);
    color: #080C14;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 800;
    font-size: 0.9rem;
    width: 28px;
    height: 28px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
}

.step-text {
    font-size: 0.95rem;
    color: #F1F5F9;
    line-height: 1.55;
    flex-grow: 1;
}

/* Observation Pill Tags */
.obs-tag {
    display: inline-block;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.25);
    color: #BAE6FD;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 0.85rem;
    margin: 4px 6px 4px 0;
}

/* Uncertainty Warning Box */
.blindspot-box {
    background: rgba(245, 158, 11, 0.08);
    border-left: 4px solid #F59E0B;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin: 14px 0;
}

/* Safety Critical Alert Box */
.safety-alert-box {
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.35);
    border-left: 5px solid #EF4444;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 16px 0;
}

/* Custom Styled Buttons */
.stButton>button {
    background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.39) !important;
    transition: all 0.25s ease !important;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #1D4ED8 0%, #6D28D9 100%) !important;
    box-shadow: 0 6px 20px 0 rgba(0, 240, 255, 0.45) !important;
    transform: translateY(-1px) !important;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #080C14;
}
::-webkit-scrollbar-thumb {
    background: rgba(56, 189, 248, 0.25);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 240, 255, 0.45);
}
</style>
"""


def render_tts_audio_script(text_to_read: str) -> str:
    """
    Generates inline HTML/JS that uses browser SpeechSynthesis (Web Speech API)
    allowing users to click and listen to instructions completely hands-free!
    """
    escaped_text = text_to_read.replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
    return f"""
    <div style="margin: 14px 0;">
        <button id="tts-btn" onclick="
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                const utter = new SpeechSynthesisUtterance('{escaped_text}');
                utter.rate = 1.0;
                utter.pitch = 1.0;
                window.speechSynthesis.speak(utter);
            }} else {{
                alert('Text-to-Speech not supported in this browser.');
            }}
        " style="
            background: linear-gradient(135deg, rgba(0, 240, 255, 0.15), rgba(168, 85, 247, 0.15));
            color: #00F0FF;
            border: 1px solid rgba(0, 240, 255, 0.4);
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
        ">
            🎧 <span>Listen to Action Steps (Hands-Free Bench Mode)</span>
        </button>
        <button onclick="window.speechSynthesis.cancel();" style="
            background: rgba(239, 68, 68, 0.15);
            color: #F87171;
            border: 1px solid rgba(239, 68, 68, 0.35);
            border-radius: 8px;
            padding: 8px 14px;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            margin-left: 8px;
        ">
            ⏹️ Stop
        </button>
    </div>
    """

"""
Design System and Multi-Theme CSS Engine for Reality -> Action AI.
Provides:
1. Cyber Dark Navy (Default cybernetic aesthetic)
2. Clean Light Mode (High-contrast bright daylight mode, 100% text legibility)
3. OLED High-Contrast Black (Pitch black with stark white and neon borders)
"""

SHARED_FONTS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap');
"""

# Default export for backwards compatibility
DARK_THEME_CSS = """
<style>
""" + SHARED_FONTS + """
:root {
    --bg-main: #060911;
    --bg-card: rgba(13, 20, 36, 0.94);
    --border-card: rgba(56, 189, 248, 0.3);
    --text-primary: #FFFFFF;
}

.stApp {
    background-color: #060911 !important;
    background-image: 
        radial-gradient(circle at 10% 10%, rgba(168, 85, 247, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 90% 90%, rgba(0, 240, 255, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.08) 0%, transparent 75%) !important;
    font-family: 'Inter', sans-serif !important;
    color: #FFFFFF !important;
}

p, span, div, li, td, th {
    color: #F1F5F9 !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
}

.hero-title {
    font-size: 2.75rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 60%, #C084FC 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    margin-bottom: 0.25rem !important;
    display: inline-block;
}

.hero-subtitle {
    font-size: 1.15rem !important;
    color: #E2E8F0 !important;
    margin-bottom: 1.5rem !important;
    font-weight: 500 !important;
}

label, label p, [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
}

input[type="text"], input[type="password"], textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea {
    background-color: #0B132B !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(0, 240, 255, 0.4) !important;
    border-radius: 10px !important;
    font-size: 1rem !important;
}

input::placeholder, textarea::placeholder {
    color: #94A3B8 !important;
    opacity: 1 !important;
}

button[data-baseweb="tab"] {
    background-color: rgba(14, 21, 37, 0.7) !important;
    color: #E2E8F0 !important;
    font-weight: 700 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(180deg, rgba(0, 240, 255, 0.15) 0%, rgba(14, 21, 37, 0.95) 100%) !important;
    color: #00F0FF !important;
    border: 1px solid #00F0FF !important;
    border-bottom: 2px solid #00F0FF !important;
}

button[data-baseweb="tab"] p {
    color: inherit !important;
    font-weight: inherit !important;
}

div[data-testid="stExpander"] {
    background: rgba(14, 21, 37, 0.85) !important;
    border: 1px solid rgba(56, 189, 248, 0.35) !important;
    border-radius: 12px !important;
}

div[data-testid="stExpander"] summary, div[data-testid="stExpander"] summary p, div[data-testid="stExpander"] summary span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

[data-testid="stFileUploader"] {
    background: rgba(14, 21, 37, 0.75) !important;
    border: 2px dashed rgba(0, 240, 255, 0.45) !important;
    border-radius: 14px !important;
}

[data-testid="stFileUploader"] span, [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] button {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

.pro-card {
    background: rgba(13, 20, 36, 0.94) !important;
    border: 1px solid rgba(56, 189, 248, 0.28) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7) !important;
}

.radar-card {
    background: linear-gradient(135deg, rgba(14, 21, 37, 0.95) 0%, rgba(20, 32, 58, 0.9) 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.4) !important;
    border-radius: 16px !important;
    padding: 22px !important;
    position: relative !important;
}

.radar-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #00F0FF, #A855F7) !important;
}

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
    font-weight: 700 !important;
}

.metric-value {
    font-size: 1.6rem !important;
    font-weight: 900 !important;
    color: #00F0FF !important;
}

.step-container {
    background: rgba(14, 22, 42, 0.85) !important;
    border: 1px solid rgba(56, 189, 248, 0.28) !important;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    gap: 16px;
}

.step-num {
    background: linear-gradient(135deg, #00F0FF, #3B82F6) !important;
    color: #060911 !important;
    font-weight: 900 !important;
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}

.step-text {
    font-size: 1.02rem !important;
    color: #FFFFFF !important;
    font-weight: 500 !important;
}

.obs-tag {
    display: inline-block;
    background: rgba(14, 165, 233, 0.18) !important;
    border: 1px solid rgba(56, 189, 248, 0.45) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    padding: 8px 14px;
    border-radius: 8px;
    margin: 4px 6px 4px 0;
}

.blindspot-box {
    background: rgba(245, 158, 11, 0.15) !important;
    border: 1px solid rgba(245, 158, 11, 0.4) !important;
    border-left: 5px solid #F59E0B !important;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin: 16px 0;
}

.safety-alert-box {
    background: rgba(239, 68, 68, 0.18) !important;
    border: 1px solid rgba(239, 68, 68, 0.5) !important;
    border-left: 6px solid #EF4444 !important;
    border-radius: 8px;
    padding: 18px 22px;
    margin: 18px 0;
}

.badge-low {
    background: rgba(16, 185, 129, 0.25) !important;
    color: #6EE7B7 !important;
    border: 1px solid rgba(16, 185, 129, 0.6) !important;
    padding: 6px 14px; border-radius: 9999px; font-weight: 800; font-size: 0.9rem !important;
}

.badge-caution {
    background: rgba(245, 158, 11, 0.25) !important;
    color: #FDE68A !important;
    border: 1px solid rgba(245, 158, 11, 0.6) !important;
    padding: 6px 14px; border-radius: 9999px; font-weight: 800; font-size: 0.9rem !important;
}

.badge-critical {
    background: rgba(239, 68, 68, 0.3) !important;
    color: #FECACA !important;
    border: 1px solid rgba(239, 68, 68, 0.7) !important;
    padding: 6px 14px; border-radius: 9999px; font-weight: 800; font-size: 0.9rem !important;
}

.stButton>button {
    background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%) !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
}

.stButton>button p, .stButton>button span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

section[data-testid="stSidebar"] {
    background-color: #060911 !important;
    border-right: 1px solid rgba(56, 189, 248, 0.2) !important;
}

section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
    color: #FFFFFF !important;
}

.equalizer-bar {
    display: inline-block; width: 4px; height: 18px; background: #00F0FF;
    border-radius: 2px; margin: 0 2px; animation: eqWave 1.2s infinite ease-in-out;
}
.equalizer-bar:nth-child(2) { animation-delay: 0.2s; height: 26px; background: #38BDF8; }
.equalizer-bar:nth-child(3) { animation-delay: 0.4s; height: 14px; background: #A855F7; }
.equalizer-bar:nth-child(4) { animation-delay: 0.6s; height: 22px; background: #C084FC; }
.equalizer-bar:nth-child(5) { animation-delay: 0.8s; height: 16px; background: #00F0FF; }

@keyframes eqWave {
    0%, 100% { transform: scaleY(0.4); }
    50% { transform: scaleY(1.2); }
}
</style>
"""

LIGHT_THEME_CSS = """
<style>
""" + SHARED_FONTS + """
:root {
    --bg-main: #F8FAFC;
    --text-primary: #0F172A;
}

.stApp {
    background-color: #F8FAFC !important;
    background-image: 
        radial-gradient(circle at 10% 10%, rgba(224, 231, 255, 0.6) 0%, transparent 50%),
        radial-gradient(circle at 90% 90%, rgba(224, 242, 254, 0.6) 0%, transparent 50%) !important;
    font-family: 'Inter', sans-serif !important;
    color: #0F172A !important;
}

p, span, div, li, td, th {
    color: #0F172A !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 800 !important;
    color: #0F172A !important;
}

.hero-title {
    font-size: 2.75rem !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, #0F172A 0%, #1D4ED8 60%, #7C3AED 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    margin-bottom: 0.25rem !important;
    display: inline-block;
}

.hero-subtitle {
    font-size: 1.15rem !important;
    color: #334155 !important;
    margin-bottom: 1.5rem !important;
    font-weight: 600 !important;
}

label, label p, [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] span {
    color: #0F172A !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
}

input[type="text"], input[type="password"], textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
    border: 2px solid #CBD5E1 !important;
    border-radius: 10px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
}

input::placeholder, textarea::placeholder {
    color: #64748B !important;
    opacity: 1 !important;
}

button[data-baseweb="tab"] {
    background-color: #E2E8F0 !important;
    color: #1E293B !important;
    font-weight: 800 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: #FFFFFF !important;
    color: #1D4ED8 !important;
    border: 2px solid #1D4ED8 !important;
    border-bottom: 3px solid #1D4ED8 !important;
}

button[data-baseweb="tab"] p {
    color: inherit !important;
    font-weight: inherit !important;
}

div[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 2px solid #CBD5E1 !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
}

div[data-testid="stExpander"] summary, div[data-testid="stExpander"] summary p, div[data-testid="stExpander"] summary span {
    color: #0F172A !important;
    font-weight: 800 !important;
}

[data-testid="stFileUploader"] {
    background: #FFFFFF !important;
    border: 2px dashed #3B82F6 !important;
    border-radius: 14px !important;
}

[data-testid="stFileUploader"] span, [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] button {
    color: #0F172A !important;
    font-weight: 700 !important;
}

.pro-card {
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06) !important;
}

.radar-card {
    background: #FFFFFF !important;
    border: 2px solid #38BDF8 !important;
    border-radius: 16px !important;
    padding: 22px !important;
    box-shadow: 0 8px 24px rgba(56, 189, 248, 0.12) !important;
    position: relative !important;
}

.radar-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #0284C7, #7C3AED) !important;
}

.metric-box {
    display: flex;
    flex-direction: column;
    padding: 14px 18px;
    background: #F1F5F9 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px;
}

.metric-title {
    font-size: 0.82rem !important;
    color: #475569 !important;
    font-weight: 800 !important;
}

.metric-value {
    font-size: 1.6rem !important;
    font-weight: 900 !important;
    color: #0369A1 !important;
}

.step-container {
    background: #F8FAFC !important;
    border: 1.5px solid #CBD5E1 !important;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    gap: 16px;
}

.step-num {
    background: linear-gradient(135deg, #1D4ED8, #7C3AED) !important;
    color: #FFFFFF !important;
    font-weight: 900 !important;
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}

.step-text {
    font-size: 1.05rem !important;
    color: #0F172A !important;
    font-weight: 600 !important;
}

.obs-tag {
    display: inline-block;
    background: #E0F2FE !important;
    border: 1.5px solid #7DD3FC !important;
    color: #0369A1 !important;
    font-weight: 700 !important;
    padding: 8px 14px;
    border-radius: 8px;
    margin: 4px 6px 4px 0;
}

.blindspot-box {
    background: #FFFBEB !important;
    border: 1.5px solid #FCD34D !important;
    border-left: 6px solid #D97706 !important;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin: 16px 0;
}

.blindspot-box ul li {
    color: #92400E !important;
    font-weight: 600 !important;
}

.safety-alert-box {
    background: #FEF2F2 !important;
    border: 1.5px solid #FCA5A5 !important;
    border-left: 6px solid #DC2626 !important;
    border-radius: 8px;
    padding: 18px 22px;
    margin: 18px 0;
}

.safety-alert-box ul li {
    color: #991B1B !important;
    font-weight: 600 !important;
}

.badge-low {
    background: #D1FAE5 !important;
    color: #065F46 !important;
    border: 1.5px solid #34D399 !important;
    padding: 6px 14px; border-radius: 9999px; font-weight: 800; font-size: 0.9rem !important;
}

.badge-caution {
    background: #FEF3C7 !important;
    color: #92400E !important;
    border: 1.5px solid #FBBF24 !important;
    padding: 6px 14px; border-radius: 9999px; font-weight: 800; font-size: 0.9rem !important;
}

.badge-critical {
    background: #FEE2E2 !important;
    color: #991B1B !important;
    border: 1.5px solid #F87171 !important;
    padding: 6px 14px; border-radius: 9999px; font-weight: 800; font-size: 0.9rem !important;
}

.stButton>button {
    background: linear-gradient(135deg, #1D4ED8 0%, #6D28D9 100%) !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
}

.stButton>button p, .stButton>button span {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1.5px solid #E2E8F0 !important;
}

section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
    color: #0F172A !important;
    font-weight: 600 !important;
}

.equalizer-bar {
    display: inline-block; width: 4px; height: 18px; background: #0284C7;
    border-radius: 2px; margin: 0 2px; animation: eqWave 1.2s infinite ease-in-out;
}
.equalizer-bar:nth-child(2) { animation-delay: 0.2s; height: 26px; background: #2563EB; }
.equalizer-bar:nth-child(3) { animation-delay: 0.4s; height: 14px; background: #7C3AED; }
.equalizer-bar:nth-child(4) { animation-delay: 0.6s; height: 22px; background: #9333EA; }
.equalizer-bar:nth-child(5) { animation-delay: 0.8s; height: 16px; background: #0284C7; }

@keyframes eqWave {
    0%, 100% { transform: scaleY(0.4); }
    50% { transform: scaleY(1.2); }
}
</style>
"""

OLED_THEME_CSS = """
<style>
""" + SHARED_FONTS + """
.stApp {
    background-color: #000000 !important;
    font-family: 'Inter', sans-serif !important;
    color: #FFFFFF !important;
}

p, span, div, li, td, th {
    color: #FFFFFF !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 900 !important;
    color: #FFFFFF !important;
}

.hero-title {
    font-size: 2.75rem !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #00F0FF 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    display: inline-block;
}

label, label p, [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] span {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

input[type="text"], input[type="password"], textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea {
    background-color: #0A0A0A !important;
    color: #FFFFFF !important;
    border: 2px solid #00F0FF !important;
}

.pro-card {
    background: #080808 !important;
    border: 1.5px solid #262626 !important;
    border-radius: 14px !important;
}

.radar-card {
    background: #080808 !important;
    border: 2px solid #00F0FF !important;
    border-radius: 14px !important;
}

.metric-box {
    background: #000000 !important;
    border: 1.5px solid #333333 !important;
}

.step-container {
    background: #080808 !important;
    border: 1.5px solid #333333 !important;
}

.step-text {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] {
    background-color: #000000 !important;
    border-right: 1.5px solid #262626 !important;
}
</style>
"""


def get_theme_css(theme_name: str) -> str:
    """Returns the CSS payload corresponding to the active theme."""
    clean = (theme_name or "").lower()
    if "light" in clean or "day" in clean or "clean" in clean:
        return LIGHT_THEME_CSS
    elif "oled" in clean or "black" in clean:
        return OLED_THEME_CSS
    return DARK_THEME_CSS

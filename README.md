# Reality → Action AI ⚡
> **Autonomous Visual Perception to Executable Physical Action Protocols**

Reality → Action AI bridges the gap between passive visual perception and safe, hands-on physical execution. Designed for students, technicians, makers, and engineers, it analyzes images of electronic circuits, industrial machinery, flowcharts, or everyday technical problems and transforms visual evidence into structured, safety-conscious step-by-step guidance.

---

## 🌟 What Makes Reality → Action AI Unique?

1. **Epistemic Humility (Facts vs. Assumptions):** Unlike standard vision models that hallucinate obscured details, Action AI strictly isolates *definitive visual observations* from *inferred hypotheses* and surfaces blind spots.
2. **Interactive "Execution Mode" & Hands-Free Audio:** Turns static text into a live checklist with real-time progress tracking, accompanied by **browser Text-to-Speech narration** so technicians holding probes or tools can listen hands-free.
3. **Dynamic Safety Matrix & Gate:** Categorizes risks into color-coded threat badges (`LOW`, `CAUTION`, `CRITICAL`) with safety checkpoints before high-voltage, pressurized, or mechanical actions.
4. **1-Click Field Inspection Report:** Exports visual assets, metadata, telemetry, and action steps into downloadable Markdown/PDF reports.
5. **Instant Judge Showcase Presets:** Pre-configured scenarios (Overheated MOSFET, Industrial Flowchart, Hydraulic Leak, Appliance Error) ready to demonstrate with a single click.

---

## 🛠️ Architecture & Technology Stack

- **Runtime:** Python 3.11+
- **Frontend:** Streamlit with custom Cyber-Industrial Glassmorphism design system (`ui/styles.py`)
- **AI Vision Engine:** Sarvam AI API utilizing image-capable Gemma 4 model (`ai_engine.py`)
- **Authentication:** Supabase Auth with email/password, password reset, and session persistence (`auth.py`)
- **Database:** Supabase PostgreSQL with Row Level Security (RLS) policies (`database.py`)
- **Storage:** Private Supabase Storage bucket (`reality-images`) with time-limited signed URLs (`storage.py`)
- **Image Validation:** Pillow (format, MIME, size, dimension, and byte decoding verification)
- **Testing:** `pytest` test suite with 100% pass rate

---

## 🚀 Quickstart Guide for Windows (PowerShell)

### 1. Clone & Navigate to the Project
```powershell
cd "c:\Users\Chethan S\OneDrive\Documents\Desktop\Action AI"
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` or edit `.env` directly:
```powershell
cp .env.example .env
```
Open `.env` in any text editor and fill in your credentials:
```env
SARVAM_API_KEY=your_sarvam_api_key_here
SARVAM_BASE_URL=https://api.sarvam.ai
SARVAM_MODEL=sarvam-gemma-4

SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your_supabase_anon_public_key_here

DEMO_MODE=true
MAX_IMAGE_SIZE_MB=10
```
> **Note:** If API keys are left blank, the application automatically runs in **Showcase Sandbox Mode**, providing full functionality and realistic evaluation scenarios for judging.

---

## 🗄️ Supabase Database & Storage Setup

1. Log into your [Supabase Dashboard](https://supabase.com).
2. Create a new project.
3. Open the **SQL Editor** from the left navigation.
4. Open the migration file: `supabase/migrations/20261018_initial_schema.sql`.
5. Copy its entire content, paste it into the Supabase SQL Editor, and click **Run**.
   - This automatically creates the `analysis_history` table, indexes, RLS policies, and the private `reality-images` storage bucket.

---

## 🧪 Running Automated Tests

Run the complete test suite:
```powershell
python -m pytest
```
All 18 tests will execute:
- Image validation (extensions, corrupted files, dimensions, byte limits)
- AI engine schema parsing, presets, and defensive text handling
- Database CRUD and user-level RLS isolation
- Auth validation rules and session lifecycle
- Secret masking and configuration telemetry

---

## ⚡ Running the Application

Launch the Streamlit app locally:
```powershell
python -m streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🌐 Deploying to Streamlit Community Cloud

1. Push your repository to GitHub:
   ```powershell
   git add .
   git commit -m "feat: complete Reality -> Action AI application"
   git branch -M main
   git remote add origin https://github.com/your-username/reality-action-ai.git
   git push -u origin main
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io/) and click **New App**.
3. Select your repository, branch (`main`), and main file (`app.py`).
4. Click **Advanced Settings** -> **Secrets**, and paste your keys from `.env`:
   ```toml
   SARVAM_API_KEY = "your_key"
   SARVAM_BASE_URL = "https://api.sarvam.ai"
   SARVAM_MODEL = "sarvam-gemma-4"
   SUPABASE_URL = "https://xyz.supabase.co"
   SUPABASE_ANON_KEY = "your_key"
   DEMO_MODE = "false"
   ```
5. Click **Deploy**! Your app will be live on a public HTTPS URL.

---

## 🔒 Security Checklist
- [x] Zero API keys committed to Git (`.gitignore` protects `.env` and `.streamlit/secrets.toml`).
- [x] Supabase service-role keys are never used in frontend code.
- [x] All database queries are filtered by `auth.uid() = user_id` via PostgreSQL Row Level Security.
- [x] Storage bucket `reality-images` is strictly private and accessed via time-limited signed URLs.
- [x] Dynamic safety gates prevent hazardous real-world action suggestions.

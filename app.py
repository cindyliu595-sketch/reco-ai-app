"""Reco — AI Career Intelligence · Home Page"""
import streamlit as st
from utils.styles import CUSTOM_CSS
from utils.state import init_state, get_profile

st.set_page_config(
    page_title="Reco — AI Career Intelligence",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
init_state()
profile = get_profile()

# ── Sidebar brand ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="reco-brand">Reco<span>.</span></div>', unsafe_allow_html=True)
    st.caption("AI Career Intelligence")
    st.divider()

    if profile.is_complete():
        pct = profile.completion_pct()
        st.markdown(f"**{profile.name}**")
        st.caption(profile.current_role or "No current role set")
        st.progress(pct / 100, text=f"Profile {pct}% complete")
    else:
        st.info("Complete your profile to get started →")

    st.divider()
    st.caption("v0.1.0 · Built with Claude claude-sonnet-4-6")

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Land the right role, faster.</h1>
  <p>Reco connects your career profile with live job data, salary benchmarks,<br>
     and AI analysis — so every application is targeted and informed.</p>
</div>
""", unsafe_allow_html=True)

# ── Quick stats (if profile exists) ──────────────────────────────────────────
from utils.state import get_jobs, get_saved_jobs, get_analyses

jobs      = get_jobs()
saved     = get_saved_jobs()
analyses  = get_analyses()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Profile complete",  f"{profile.completion_pct()}%")
col2.metric("Jobs discovered",   len(jobs))
col3.metric("Saved jobs",        len(saved))
col4.metric("Roles analyzed",    len(analyses))

st.divider()

# ── Feature cards ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">What Reco does for you</div>', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
features = [
    ("🙋", "Build Your Profile", "Tell Reco your skills, experience, and career goals once."),
    ("🔍", "Discover Live Jobs",  "Pull real postings from Greenhouse & Lever — no stale listings."),
    ("🎯", "AI Fit Analysis",     "Get a match score, strengths, gaps, and 'apply or skip' advice."),
    ("📝", "Tailor Your Resume",  "Upload your resume and get a job-specific version in seconds."),
    ("📊", "Salary Insights",     "See BLS wage data and compare your expectations to the market."),
]
for col, (icon, title, desc) in zip([c1, c2, c3, c4, c5], features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
          <div class="feature-icon">{icon}</div>
          <div class="feature-title">{title}</div>
          <div class="feature-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ── How it works ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">How it works</div>', unsafe_allow_html=True)

left, right = st.columns([2, 1])
with left:
    steps = [
        ("1", "Set up your profile", "Add your skills, experience, target roles, and salary range."),
        ("2", "Search live job boards", "Choose companies and keywords — Reco pulls real job data."),
        ("3", "Get AI fit scores",      "Claude analyzes each posting against your profile."),
        ("4", "Apply with confidence",  "Use the tailored resume and cover letter Reco generates."),
    ]
    for num, title, desc in steps:
        st.markdown(f"""
        <div style="display:flex;gap:16px;margin-bottom:20px;align-items:flex-start;">
          <div style="min-width:32px;height:32px;border-radius:50%;background:#7C3AED;
                      color:white;display:flex;align-items:center;justify-content:center;
                      font-weight:700;font-size:.9rem;">{num}</div>
          <div>
            <div style="font-weight:600;color:#111827;margin-bottom:2px;">{title}</div>
            <div style="font-size:.875rem;color:#6B7280;">{desc}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="card" style="background:#F5F3FF;border-color:#DDD6FE;">
      <div style="font-weight:700;color:#5B21B6;margin-bottom:12px;">📌 Quick Start</div>
      <ol style="color:#4B5563;font-size:.9rem;padding-left:16px;line-height:2;">
        <li>Go to <b>Profile</b> in the sidebar</li>
        <li>Fill in your skills & target roles</li>
        <li>Head to <b>Jobs</b> and search</li>
        <li>Run <b>Fit Analysis</b> on saved jobs</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.divider()
_, center, _ = st.columns([1, 2, 1])
with center:
    if not profile.is_complete():
        st.page_link("pages/1_🙋_Profile.py", label="→ Set up your profile", icon="🙋")
    else:
        st.page_link("pages/2_🔍_Jobs.py", label="→ Search live jobs", icon="🔍")

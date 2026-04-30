CUSTOM_CSS = """
<style>
/* ── Global ────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit default menu & footer */
#MainMenu, footer { visibility: hidden; }

/* ── Top nav brand ─────────────────────────────── */
.reco-brand {
    font-size: 1.6rem;
    font-weight: 700;
    color: #7C3AED;
    letter-spacing: -0.5px;
}
.reco-brand span { color: #EC4899; }

/* ── Hero section ──────────────────────────────── */
.hero {
    background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
    border-radius: 16px;
    padding: 48px 40px;
    color: white;
    margin-bottom: 32px;
}
.hero h1 { font-size: 2.4rem; font-weight: 700; margin: 0 0 12px; }
.hero p  { font-size: 1.1rem; opacity: 0.9; margin: 0; }

/* ── Cards ─────────────────────────────────────── */
.card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
    transition: box-shadow .2s, border-color .2s;
}
.card:hover {
    border-color: #7C3AED;
    box-shadow: 0 4px 20px rgba(124,58,237,.12);
}
.card-title { font-size: 1rem; font-weight: 600; color: #111827; margin: 0 0 4px; }
.card-sub   { font-size: .85rem; color: #6B7280; margin: 0 0 12px; }

/* ── Feature cards on home ─────────────────────── */
.feature-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 28px 24px;
    text-align: center;
    height: 100%;
}
.feature-icon { font-size: 2rem; margin-bottom: 12px; }
.feature-title { font-size: 1rem; font-weight: 600; color: #111827; margin-bottom: 8px; }
.feature-desc  { font-size: .875rem; color: #6B7280; line-height: 1.6; }

/* ── Skill tags ────────────────────────────────── */
.skill-tag {
    display: inline-block;
    background: #EDE9FE;
    color: #5B21B6;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: .8rem;
    font-weight: 500;
    margin: 3px;
}
.skill-tag-gap {
    background: #FEF3C7;
    color: #92400E;
}

/* ── Match score badge ─────────────────────────── */
.score-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    font-size: 1.1rem;
    font-weight: 700;
    color: white;
}
.score-high   { background: #10B981; }
.score-mid    { background: #F59E0B; }
.score-low    { background: #EF4444; }

/* ── Recommendation pill ───────────────────────── */
.pill-apply   { background:#D1FAE5; color:#065F46; border-radius:20px; padding:4px 14px; font-size:.8rem; font-weight:600; }
.pill-consider{ background:#FEF3C7; color:#92400E; border-radius:20px; padding:4px 14px; font-size:.8rem; font-weight:600; }
.pill-skip    { background:#FEE2E2; color:#991B1B; border-radius:20px; padding:4px 14px; font-size:.8rem; font-weight:600; }

/* ── Section divider ───────────────────────────── */
.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid #EDE9FE;
}

/* ── Progress bar override ─────────────────────── */
div[data-testid="stProgressBar"] > div {
    background-color: #7C3AED !important;
}

/* ── Job card specifics ────────────────────────── */
.job-company { font-size: .8rem; color: #7C3AED; font-weight: 600; text-transform: uppercase; letter-spacing: .5px; }
.job-meta    { font-size: .82rem; color: #6B7280; margin-top: 4px; }

/* ── Step indicator ────────────────────────────── */
.step-indicator {
    display: flex;
    gap: 8px;
    margin-bottom: 24px;
}
.step-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: #D1D5DB;
}
.step-dot.active { background: #7C3AED; }
.step-dot.done   { background: #10B981; }

/* ── Alert box ─────────────────────────────────── */
.alert-info {
    background: #EFF6FF;
    border-left: 4px solid #3B82F6;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    font-size: .9rem;
    color: #1E40AF;
    margin: 12px 0;
}

/* ── Sidebar ───────────────────────────────────── */
[data-testid="stSidebar"] {
    background: #FAFAFA;
    border-right: 1px solid #E5E7EB;
}
</style>
"""


def skill_tags_html(skills: list[str], gap: bool = False) -> str:
    cls = "skill-tag skill-tag-gap" if gap else "skill-tag"
    return "".join(f'<span class="{cls}">{s}</span>' for s in skills)


def score_badge_html(score: int) -> str:
    if score >= 70:
        cls = "score-high"
    elif score >= 45:
        cls = "score-mid"
    else:
        cls = "score-low"
    return f'<div class="score-badge {cls}">{score}</div>'


def pill_html(recommendation: str) -> str:
    rec = recommendation.lower()
    if rec == "apply":
        return '<span class="pill-apply">✓ Apply</span>'
    elif rec == "consider":
        return '<span class="pill-consider">~ Consider</span>'
    else:
        return '<span class="pill-skip">✗ Skip</span>'

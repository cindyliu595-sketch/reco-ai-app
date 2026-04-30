"""Session-state helpers — single source of truth for all cross-page data."""
import streamlit as st
from dataclasses import asdict


# ── keys ────────────────────────────────────────────────────────────────────
PROFILE_KEY   = "reco_profile"
JOBS_KEY      = "reco_jobs"          # fetched job listings
SAVED_KEY     = "reco_saved_jobs"    # user-bookmarked jobs
ANALYSIS_KEY  = "reco_analyses"      # {job_id: analysis_dict}
RESUME_KEY    = "reco_resume_text"   # raw extracted text


def init_state():
    from core.profile import UserProfile
    if PROFILE_KEY not in st.session_state:
        st.session_state[PROFILE_KEY] = UserProfile()
    if JOBS_KEY not in st.session_state:
        st.session_state[JOBS_KEY] = []
    if SAVED_KEY not in st.session_state:
        st.session_state[SAVED_KEY] = []
    if ANALYSIS_KEY not in st.session_state:
        st.session_state[ANALYSIS_KEY] = {}
    if RESUME_KEY not in st.session_state:
        st.session_state[RESUME_KEY] = ""


def get_profile():
    init_state()
    return st.session_state[PROFILE_KEY]


def set_profile(profile):
    st.session_state[PROFILE_KEY] = profile


def get_jobs() -> list:
    init_state()
    return st.session_state[JOBS_KEY]


def set_jobs(jobs: list):
    st.session_state[JOBS_KEY] = jobs


def get_saved_jobs() -> list:
    init_state()
    return st.session_state[SAVED_KEY]


def save_job(job: dict):
    saved = get_saved_jobs()
    job_id = job.get("id", job.get("title", ""))
    if not any(j.get("id", j.get("title", "")) == job_id for j in saved):
        saved.append(job)
        st.session_state[SAVED_KEY] = saved


def remove_saved_job(job_id: str):
    saved = get_saved_jobs()
    st.session_state[SAVED_KEY] = [
        j for j in saved if j.get("id", j.get("title", "")) != job_id
    ]


def get_analyses() -> dict:
    init_state()
    return st.session_state[ANALYSIS_KEY]


def set_analysis(job_id: str, analysis: dict):
    analyses = get_analyses()
    analyses[job_id] = analysis
    st.session_state[ANALYSIS_KEY] = analyses


def get_resume_text() -> str:
    init_state()
    return st.session_state[RESUME_KEY]


def set_resume_text(text: str):
    st.session_state[RESUME_KEY] = text

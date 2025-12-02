import streamlit as st
import json
from pathlib import Path

DATA_FILE = Path("data/works.json")

# Load works
with open(DATA_FILE, "r", encoding="utf-8") as f:
    works = json.load(f)

st.set_page_config(page_title="AO3 Demo", page_icon="📚")
st.title("📚 AO3 Demo (Mock Project)")
st.write("This is a simple Streamlit demo imitating AO3 using local sample data.")

# Sidebar list of works
st.sidebar.header("Works")
work_titles = {w["title"]: w for w in works}
selected_title = st.sidebar.selectbox("Select a work", list(work_titles.keys()))

work = work_titles[selected_title]

# Display work info
st.header(work["title"])
st.subheader(f"By {work['author']}")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Rating:**", work["rating"])
with col2:
    st.write("**Warnings:**")
    for w in work["warnings"]:
        st.write("•", w)
with col3:
    st.write("**Fandoms:**")
    for f in work["fandoms"]:
        st.write("•", f)

st.write("### Tags")
st.write(", ".join(work["tags"]))

st.write("### Summary")
st.info(work["summary"])

# Chapters
chapter_titles = [c["title"] for c in work["chapters"]]
selected_chapter = st.selectbox("Read Chapter:", chapter_titles)

chapter = next(c for c in work["chapters"] if c["title"] == selected_chapter)

st.subheader(chapter["title"])
st.write(chapter["content"])

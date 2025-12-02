import streamlit as st

# ---------------------------
# Mock AO3-style data
# ---------------------------

WORKS = [
    {
        "title": "The Hero Who Stayed",
        "author": "DreamWriter",
        "rating": "Teen",
        "tags": ["Adventure", "Friendship"],
        "summary": "A short story about a hero who chose a different path.",
        "chapters": [
            {
                "title": "Chapter 1: Arrival",
                "content": "The village was quiet when the hero arrived..."
            },
            {
                "title": "Chapter 2: The Choice",
                "content": "Standing at the crossroads, the hero made a choice..."
            }
        ]
    },
    {
        "title": "Starlight Letters",
        "author": "Skyline",
        "rating": "General",
        "tags": ["Romance", "Sci-Fi"],
        "summary": "Two travelers exchange messages across galaxies.",
        "chapters": [
            {
                "title": "Message I",
                "content": "Hello from the Nebula outpost..."
            }
        ]
    }
]

# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="AO3 Demo", page_icon="📚")
st.title("📚 AO3 Demo (Mock Data)")

# Sidebar – list of works
work_titles = [w["title"] for w in WORKS]
selected_work_title = st.sidebar.selectbox("Choose a Work", work_titles)

# Find work
work = next(w for w in WORKS if w["title"] == selected_work_title)

# Display work information
st.header(work["title"])
st.subheader(f"By {work['author']}")

st.markdown(f"**Rating:** {work['rating']}")
st.markdown("**Tags:** " + ", ".join(work["tags"]))

st.write("### Summary")
st.info(work["summary"])

# Chapters
chapter_titles = [c["title"] for c in work["chapters"]]
selected_chapter_title = st.selectbox("Read Chapter:", chapter_titles)

chapter = next(c for c in work["chapters"] if c["title"] == selected_chapter_title)

st.subheader(chapter["title"])
st.write(chapter["content"])

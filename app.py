import streamlit as st
import ollama
import urllib.parse

st.set_page_config(page_title="AI Smart Study Planner", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main {padding-top:1rem;}
.stMetric {background-color:#f5f7fa;padding:15px;border-radius:10px;}
</style>
""", unsafe_allow_html=True)

def create_youtube_search_link(query):
    encoded = urllib.parse.quote(query)
    return f"https://www.youtube.com/results?search_query={encoded}"

st.title("AI Smart Study Planner")
st.write("Generate cognitive-science-backed study plans using a local Ollama model.")
st.markdown("---")

def get_available_models():
    try:
        models = ollama.list()

        names = []

        for model in models["models"]:
            names.append(model["model"])

        return names

    except:
        return ["llama3"]

with st.sidebar:
    st.header("Study Configuration")

    subject = st.text_input("Subject / Topic", placeholder="e.g. Data Structures & Algorithms")

    days = st.slider("Study Duration (Days)", 1, 180, 14)

    hours_per_day = st.slider("Daily Study Hours", 1, 12, 2)

    current_level = st.selectbox(
        "Current Knowledge Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    available_models = get_available_models()

    model_name = st.selectbox(
        "AI Model",
        available_models
    )

    generate = st.button("Generate Study Plan", use_container_width=True)

if not generate:
    c1, c2 = st.columns(2)
    c1.metric("Model", model_name)
    c2.metric("Mode", "Local")
    st.info("Configure your study plan from the sidebar and click Generate.")
    st.stop()

if not subject:
    st.warning("Please enter a subject.")
    st.stop()

prompt = f"""
You are an elite academic coach.

Create a study plan for:

Subject: {subject}
Duration: {days} days
Daily Hours: {hours_per_day}
Level: {current_level}

Return EXACTLY in this format:

## STUDY TABLE

| Day | Focus Topic | Core Milestone Activity | Active Recall Checkpoint Question |
|-----|-------------|-------------------------|-----------------------------------|

## PHASES

### Foundation Phase (Days X-Y)
Explanation

### Deep Dive Phase (Days A-B)
Explanation

### Practice Phase (Days C-D)
Explanation

## SUCCESS_TIPS

1. Tip
2. Tip
3. Tip
4. Tip
5. Tip

## RESOURCES

### can be Books or websites anything that is relevant to the subject

## YOUTUBE_COURSES

Recommend exactly 5 YouTube courses/playlists.

For each provide:

- Course Name
- Instructor/Channel Name
- YouTube Search Query

Example:

1. Striver A2Z DSA Course
   Channel: take U forward
   Search Query: Striver A2Z DSA Course

2. Data Structures Full Course
   Channel: freeCodeCamp
   Search Query: Data Structures Full Course freeCodeCamp

Rules:
- Generate exactly ONE markdown table.
- Do not repeat table headers.
- Generate exactly {days} rows.
"""

with st.spinner("🧠 Generating study roadmap..."):
    try:
        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )

        output = response["message"]["content"]

        study_idx = output.find("## STUDY TABLE")
        phase_idx = output.find("## PHASES")
        tips_idx = output.find("## SUCCESS_TIPS")
        resource_idx = output.find("## RESOURCES")
        youtube_idx = output.find("## YOUTUBE_COURSES")

        if min(study_idx,phase_idx,tips_idx,resource_idx,youtube_idx) == -1:
            st.error("Model did not follow expected format.")
            st.markdown(output)
            st.stop()

        table_text = output[study_idx:phase_idx]
        phases_text = output[phase_idx:tips_idx]
        tips_text = output[tips_idx:resource_idx]
        resources_text = output[resource_idx:youtube_idx]
        youtube_text = output[youtube_idx:]

        total_hours = days * hours_per_day

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Subject", subject)
        m2.metric("Duration", f"{days} Days")
        m3.metric("Daily Hours", hours_per_day)
        m4.metric("Total Hours", total_hours)

        st.markdown("---")

        foundation_end = max(2, days // 3)
        deep_end = (2 * days) // 3

        st.subheader("Learning Journey")
        st.markdown(f"""
- **Foundation:** Days 1-{foundation_end}
- **Deep Dive:** Days {foundation_end+1}-{deep_end}
- **Practice:** Days {deep_end+1}-{days}
""")

        st.progress(min(total_hours / 100, 1.0))

        st.download_button(
            "Download Study Plan",
            data=output,
            file_name="study_plan.md",
            mime="text/markdown"
        )

        tab1, tab2, tab3 = st.tabs(
            ["Study Plan", "Strategy & Resources", "Video Courses"]
        )

        with tab1:
            st.subheader("Study Timetable")
            st.markdown(table_text)

        with tab2:
            st.subheader("Phase Breakdown")
            with st.expander("Study Strategy", expanded=True):
                st.markdown(phases_text)

            with st.expander("Success Tips", expanded=True):
                st.markdown(tips_text)

            st.subheader("Resources")
            st.markdown(resources_text)

        with tab3:

            st.subheader("Recommended YouTube Courses")

            lines = youtube_text.split("\n")

            current_course = {}
            courses = []

            for line in lines:

                line = line.strip()

                if not line:
                    continue

                if line[0].isdigit() and "." in line:
                    if current_course:
                        courses.append(current_course)

                    current_course = {
                        "course": line.split(".", 1)[1].strip()
                    }

                elif line.startswith("Channel:"):
                    current_course["channel"] = (
                        line.replace("Channel:", "").strip()
                    )

                elif line.startswith("Search Query:"):
                    current_course["query"] = (
                        line.replace("Search Query:", "").strip()
                    )

            if current_course:
                courses.append(current_course)

            for course in courses:

                with st.container():

                    st.markdown(
                        f"### {course.get('course', '')}"
                    )

                    st.caption(
                        f"Channel: {course.get('channel', '')}"
                    )

                    if "query" in course:

                        st.link_button(
                            "Open on YouTube",
                            create_youtube_search_link(
                                course["query"]
                            )
                        )

                    st.markdown("---")

    except Exception as e:
        st.error(f"Error: {e}")

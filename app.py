import streamlit as st
import ollama

st.set_page_config(page_title="Smart Study-Plan Generator", layout="wide")

st.title("Smart Study-Plan Generator")
st.write("Generate a structured, cognitive-science-backed study calendar using local AI.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input(
        "Subject / Topic",
        placeholder="e.g., Data Structures & Algorithms"
    )

    days = st.number_input(
        "Number of Days",
        min_value=1,
        max_value=365,
        value=14
    )

with col2:
    hours_per_day = st.number_input(
        "Daily Study Hours",
        min_value=1,
        max_value=24,
        value=2
    )

    current_level = st.selectbox(
        "Current Knowledge Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

if st.button("Build My Optimized Study Plan", type="primary"):

    prompt = f"""
You are an elite academic coach.

Create a study plan for:

Subject: {subject}
Duration: {days} days
Daily Hours: {hours_per_day}
Level: {current_level}

IMPORTANT:

Return EXACTLY in this format:

## STUDY_TABLE

| Day | Focus Topic | Core Milestone Activity | Active Recall Checkpoint Question |
|-----|-------------|-------------------------|-----------------------------------|
| ... |

## PHASES

### Foundation Phase (Days X-Y)
Explanation

### Deep Dive Phase (Days A-B)
Explanation

### Practice Phase (Days C-D)
Explanation

The day ranges must correspond to the study timetable above.
Distribute the total timeline logically across the phases.

## RESOURCES

1. Resource
2. Resource
3. Resource

Rules:
- Generate exactly ONE markdown table.
- Do NOT repeat table headers.
- Do NOT create multiple tables.
- The table must contain exactly {days} rows.
"""

    with st.spinner("Generating study plan..."):

        try:
            response = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            output = response["message"]["content"]

            study_idx = output.find("## STUDY TABLE")
            phase_idx = output.find("## PHASES")
            resource_idx = output.find("## RESOURCES")

            if (
                study_idx == -1
                or phase_idx == -1
                or resource_idx == -1
            ):
                st.error(
                    "Model did not follow the expected format. Showing raw output."
                )
                st.markdown(output)

            else:
                table_text = output[study_idx:phase_idx]
                phases_text = output[phase_idx:resource_idx]
                resources_text = output[resource_idx:]

                st.success("Your Personalized Study Plan is Ready!")

                tab1, tab2 = st.tabs(
                    [
                        "📅 Study Timetable & Calendar",
                        "💡 Strategy & Resources"
                    ]
                )

                with tab1:
                    st.subheader(
                        "Your Personalized Chronological Roadmap"
                    )

                    st.markdown(table_text)

                with tab2:
                    st.subheader(
                        "Implementation Strategy"
                    )
                    st.markdown(phases_text)

                    st.subheader(
                        "Recommended Learning Resources"
                    )
                    st.markdown(resources_text)

        except Exception as e:
            st.error(f"Error: {e}")
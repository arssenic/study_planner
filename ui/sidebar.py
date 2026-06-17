import streamlit as st

def render_sidebar(models):
    with st.sidebar:
        st.header("Study Configuration")
        subject = st.text_input(
            "Subject / Topic"
        )
        days = st.slider(
            "Study Duration (Days)",
            1,
            180,
            14
        )
        hours = st.slider(
            "Daily Study Hours",
            1,
            12,
            2
        )
        level = st.selectbox(
            "Current Knowledge Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )
        model_name = st.selectbox(
            "AI Model",
            models
        )
        generate = st.button(
            "Generate Study Plan",
            use_container_width=True
        )
    return (
        subject,
        days,
        hours,
        level,
        model_name,
        generate
    )
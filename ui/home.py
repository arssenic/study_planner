import streamlit as st


def render_home(model_name):
    """
    Render the initial landing page before
    the study plan is generated.
    """

    c1, c2 = st.columns(2)

    c1.metric(
        "Model",
        model_name
    )

    c2.metric(
        "Mode",
        "Local"
    )

    st.info(
        "Configure your study plan from the sidebar and click "
        "'Generate Study Plan'."
    )

    st.markdown("---")

    st.subheader("How It Works")

    st.markdown("""
    1. Select a subject.

    2. Choose study duration.

    3. Set daily study hours.

    4. Pick your current skill level.

    5. Select an AI model.

    6. Generate your personalized study roadmap.
    """)
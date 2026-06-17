import streamlit as st

from assets.styles import load_css

from prompts.study_prompt import (
    generate_prompt
)

from services.ollama_service import (
    get_available_models,
    generate_study_plan
)

from utils.parser import (
    parse_output
)

from ui.sidebar import (
    render_sidebar
)

from ui.home import (
    render_home
)

from ui.dashboard import (
    render_dashboard
)

from ui.tabs import (
    render_tabs
)

st.set_page_config(
    page_title="AI Smart Study Planner",
    layout="wide"
)

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

st.title(
    "AI Smart Study Planner"
)

st.write(
    "Generate cognitive-science-backed study plans using a local Ollama model."
)

st.markdown("---")

available_models = (
    get_available_models()
)

(
    subject,
    days,
    hours_per_day,
    current_level,
    model_name,
    generate
) = render_sidebar(
    available_models
)

if not generate:

    render_home(
        model_name
    )

    st.stop()

if not subject:

    st.warning(
        "Please enter a subject."
    )

    st.stop()

prompt = generate_prompt(
    subject,
    days,
    hours_per_day,
    current_level
)

with st.spinner(
    "🧠 Generating study roadmap..."
):

    try:
        output = generate_study_plan(
            model_name,
            prompt
        )

        parsed_data = parse_output(
            output
        )

        if parsed_data is None:

            st.error(
                "Model did not follow expected format."
            )

            st.markdown(
                output
            )

            st.stop()

        render_dashboard(
            subject,
            days,
            hours_per_day,
            output
        )

        render_tabs(
            parsed_data
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )
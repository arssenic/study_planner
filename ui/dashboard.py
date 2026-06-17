import streamlit as st

from utils.calculations import (
    calculate_phase_ranges,
    calculate_total_hours
)


def render_dashboard(
    subject,
    days,
    hours_per_day,
    output
):

    total_hours = calculate_total_hours(
        days,
        hours_per_day
    )

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "Subject",
        subject
    )

    m2.metric(
        "Duration",
        f"{days} Days"
    )

    m3.metric(
        "Daily Hours",
        hours_per_day
    )

    m4.metric(
        "Total Hours",
        total_hours
    )

    st.markdown("---")

    phase_ranges = calculate_phase_ranges(days)

    st.subheader("Learning Journey")

    st.markdown(
        f"""
- **Foundation:** Days {phase_ranges['foundation_start']}-{phase_ranges['foundation_end']}

- **Deep Dive:** Days {phase_ranges['deep_dive_start']}-{phase_ranges['deep_dive_end']}

- **Practice:** Days {phase_ranges['practice_start']}-{phase_ranges['practice_end']}
"""
    )

    st.download_button(
        "Download Study Plan",
        data=output,
        file_name="study_plan.md",
        mime="text/markdown"
    )
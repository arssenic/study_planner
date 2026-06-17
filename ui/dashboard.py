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

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            f"""
### Foundation

**Days {phase_ranges['foundation_start']} - {phase_ranges['foundation_end']}**

Build core concepts and establish strong fundamentals before moving to advanced topics.
"""
        )

    with c2:
        st.warning(
            f"""
### Deep Dive

**Days {phase_ranges['deep_dive_start']} - {phase_ranges['deep_dive_end']}**

Focus on mastering complex concepts, solving problems, and strengthening understanding.
"""
        )

    with c3:
        st.success(
            f"""
### Practice

**Days {phase_ranges['practice_start']} - {phase_ranges['practice_end']}**

Revision, active recall, mock assessments, and long-term retention.
"""
        )

    st.markdown("---")

    st.download_button(
        "Download Study Plan",
        data=output,
        file_name="study_plan.md",
        mime="text/markdown"
    )
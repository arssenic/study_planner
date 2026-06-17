import streamlit as st

from utils.youtube_utils import (
    create_youtube_search_link,
    parse_youtube_courses
)


def render_tabs(parsed_data):

    table_text = parsed_data["table"]
    phases_text = parsed_data["phases"]
    tips_text = parsed_data["tips"]
    resources_text = parsed_data["resources"]
    youtube_text = parsed_data["youtube"]

    tab1, tab2, tab3 = st.tabs(
        [
            "Study Plan",
            "Strategy & Resources",
            "Video Courses"
        ]
    )

    with tab1:

        st.subheader("Study Timetable")

        st.markdown(table_text)

    with tab2:

        st.subheader("Phase Breakdown")

        with st.expander(
            "Study Strategy",
            expanded=True
        ):
            st.markdown(phases_text)

        with st.expander(
            "Success Tips",
            expanded=True
        ):
            st.markdown(tips_text)

        st.subheader("Resources")

        st.markdown(resources_text)

    with tab3:

        st.subheader(
            "Recommended YouTube Courses"
        )

        courses = parse_youtube_courses(
            youtube_text
        )

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
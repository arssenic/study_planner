import streamlit as st
import ollama

st.set_page_config(page_title="Smart Study-Plan Generator", layout="centered")

st.title("Smart Study-Plan Generator")
st.write("Generate a structured, cognitive-science-backed study calendar using local AI.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input("Subject / Topic", placeholder="e.g., Data Structures & Algorithms")
    timeframe = st.text_input("Timeframe Remaining", placeholder="e.g., 14 days")

with col2:
    hours_per_day = st.text_input("Daily Time Budget", placeholder="e.g., 2 hours")
    current_level = st.selectbox(
        "Current Knowledge Level", 
        ["Beginner (No prior exposure)", "Intermediate (Know fundamentals)", "Advanced (Looking for deep review)"]
    )

if st.button("Build My Optimized Study Plan", type="primary"):
    if not subject or not timeframe or not hours_per_day:
        st.warning("Please fill out all input fields before generating.")
    else:
        prompt = f"""
        You are an elite academic coach specializing in accelerated learning frameworks. 
        Generate a highly optimized, day-by-day study schedule based on these constraints:
        
        - Subject: {subject}
        - Timeframe available: {timeframe}
        - Daily Study Budget: {hours_per_day}
        - Student Starting Point: {current_level}
        
        Structuring Guidelines:
        1. Break the timeline down into strategic chronological phases (e.g., Foundation, Deep Dive, Rigorous Practice, Final Review).
        2. For EVERY SINGLE DAY within the timeframe, provide a markdown subheader containing:
           - The core technical topic to master.
           - A concrete, actionable milestone/task (e.g., 'Solve 3 tree traversal problems').
           - A 10-minute 'Active Recall' question or flashcard prompt to test retention at the end of the day.
        3. End the output with a section recommending 3 highly rated free general types of online resources matching this topic.
        
        Output the entire response in beautifully formatted, clean Markdown with distinct bold sections.
        """
        
        with st.spinner("Local LLM is processing and structuring your timeline..."):
            try:
                response = ollama.chat(
                    model='llama3', 
                    messages=[{'role': 'user', 'content': prompt}]
                )
                
                study_plan = response['message']['content']
                st.success("Your Personalized Study Plan is Ready!")
                st.markdown(study_plan)
                
            except Exception as e:
                st.error(f"Failed to communicate with local Ollama instance. Is your server running? Error: {e}")
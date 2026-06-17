# AI Smart Study Planner

An AI-powered study planning application built with **Streamlit** and **Ollama** that generates personalized study roadmaps, learning strategies, resource recommendations, and curated YouTube course suggestions based on a user's goals and available study time.

---

## Project Structure

```text
study_planner/
│
├── app.py
│
├── assets/
│   └── styles.py
│
├── prompts/
│   └── study_prompt.py
│
├── services/
│   └── ollama_service.py
│
├── utils/
│   ├── parser.py
│   ├── youtube_utils.py
│   └── calculations.py
│
├── ui/
│   ├── sidebar.py
│   ├── home.py
│   ├── dashboard.py
│   └── tabs.py
│
├── requirements.txt
│
└── README.md
```

---

## Tech Stack

### Frontend

- Streamlit

### AI Models

- Ollama
- Llama 3
- Qwen 3
- Mistral
- Gemma
- Any locally installed Ollama model

### Backend

- Python

---

## How It Works

1. User enters:
   - Subject
   - Study Duration
   - Daily Study Hours
   - Current Knowledge Level

2. User selects an Ollama model.

3. The application dynamically generates a structured prompt.

4. The selected local LLM creates:
   - Study Timetable
   - Learning Phases
   - Success Tips
   - Resource Recommendations
   - YouTube Course Recommendations

5. The response is parsed and displayed in a structured dashboard.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/study_planner.git
cd study_planner
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama from:

https://ollama.com/download

---

## Pull a Model

Example:

```bash
ollama pull llama3
```

or

```bash
ollama pull qwen3
```

Verify installation:

```bash
ollama list
```

---

## Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

import ollama

def get_available_models():
    try:
        models = ollama.list()

        names = []

        for model in models["models"]:
            names.append(model["model"])

        return names

    except:
        return ["llama3"]


def generate_study_plan(model_name, prompt):

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
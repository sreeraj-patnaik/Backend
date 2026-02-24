import requests
import os


def call_llm(prompt):

    response = requests.post(
        "YOUR_LLM_API_URL",
        headers={
            "Authorization": f"Bearer {os.getenv('API_KEY')}"
        },
        json={
            "prompt": prompt
        }
    )

    return response.json()
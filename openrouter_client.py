import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("OPENROUTER_MODEL")

if not api_key:
 raise RuntimeError(
"OPENROUTER_API_KEY is missing from your .env file."
)

if not model:
 raise RuntimeError(
"OPENROUTER_MODEL is missing from your .env file."
)

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key=api_key,
)

def ask_ai(prompt: str) -> str:
 """Send a prompt to the configured OpenRouter model."""

 response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI research assistant specializing in "
                    "WorldQuant BRAIN alpha research and Fast Expression. "
                    "Analyze evidence carefully. Never invent simulation "
                    "metrics or claim an expression is profitable without "
                    "actual simulation results."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=1200,
    )

 return response.choices[0].message.content or ""


if __name__ == "__main__":
    answer = ask_ai(
        "Explain in three bullet points how Sharpe, Fitness, and drawdown "
        "help evaluate a quantitative trading alpha. Do not invent "
        "performance data."
    )
print(answer)

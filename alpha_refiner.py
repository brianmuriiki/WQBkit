import json

from alpha_experiment_tracker import record_experiment
from openrouter_client import ask_ai
from wqbkit.app.database.schemas import FactorData

def refine_alpha(
expression: str,
region: str,
universe: str,
neutralization: str,
decay: int,
sharpe: float,
fitness: float,
drawdown: float,
twoyearsharpe: float,
generation: int = 0,
factor_id: int | None = None,
) -> list[str]:
    
"""Generate alpha refinement proposals using actual simulation metrics."""

prompt = f"""
```

You are a WorldQuant BRAIN Fast Expression research assistant.

Analyze this alpha candidate.

Expression: {expression}
Region: {region}
Universe: {universe}
Neutralization: {neutralization}
Decay: {decay}

Actual simulation metrics:
Sharpe: {sharpe}
Fitness: {fitness}
Drawdown: {drawdown}
Two-year Sharpe: {twoyearsharpe}

Tasks:

1. Diagnose potential weaknesses.
2. Propose at most 3 targeted refinements.
3. Use plausible WorldQuant BRAIN Fast Expression syntax.
4. Explain the hypothesis behind each proposal.
5. Never invent simulation results.
6. Keep the original expression unchanged for comparison.

Return ONLY valid JSON using this format:
{{
"diagnosis": "Brief diagnosis",
"proposals": [
{{
"expression": "Proposed Fast Expression",
"hypothesis": "Reason for the change"
}}
]
}}
"""


response = ask_ai(prompt)

try:
    data = json.loads(response)
except (json.JSONDecodeError, TypeError):
    print("The AI response was not valid JSON:")
    print(response)
    return []

if not isinstance(data, dict):
    print("Invalid response: expected a JSON object.")
    return []

print("\nAI Diagnosis:")
print(data.get("diagnosis", "No diagnosis provided"))

proposals = data.get("proposals", [])

if not isinstance(proposals, list):
    print("Invalid proposals format.")
    return []

recorded = []

for index, proposal in enumerate(proposals[:3], start=1):
    if not isinstance(proposal, dict):
        continue

    proposed_expression = proposal.get("expression")
    hypothesis = proposal.get("hypothesis", "")

    if not isinstance(proposed_expression, str):
        continue

    proposed_expression = proposed_expression.strip()

    if not proposed_expression:
        continue

    if proposed_expression == expression.strip():
        print("Skipping unchanged expression.")
        continue

    candidate = FactorData(
        factor_id=None,
        pre="",
        expression=proposed_expression,
        neutralization=neutralization,
        region=region,
        universe=universe,
        decay=decay,
        task_id=None,
        priority=1,
        generation=generation + 1,
        tag=f"ai_refinement_{index}",
    )

    record_experiment(
        candidate=candidate,
        hypothesis=str(hypothesis),
        parent_expression=expression,
    )

    recorded.append(proposed_expression)

print(f"\nRecorded {len(recorded)} proposed refinements.")
print("These proposals have not been validated or simulated.")

return recorded


if __name__ == "__main__":
    print("AI Alpha Refiner")
    print("Module loaded successfully.")
    print("No AI request or BRAIN simulation was performed.")

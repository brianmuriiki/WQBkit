
import json
from datetime import datetime, timezone
from pathlib import Path

from wqbkit.app.database.schemas import FactorData, SimulationData

RESULTS_DIR = Path(**file**).parent / "results"
HISTORY_FILE = RESULTS_DIR / "experiment_history.jsonl"

def record_experiment(
candidate: FactorData,
hypothesis: str,
parent_expression: str | None = None,
result: SimulationData | None = None,
) -> None:
"""Record an alpha candidate and its optional simulation result."""

```
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

record = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "factor_id": candidate.factor_id,
    "expression": candidate.pre + candidate.expression,
    "parent_expression": parent_expression,
    "hypothesis": hypothesis,
    "settings": {
        "region": candidate.region,
        "universe": candidate.universe,
        "neutralization": candidate.neutralization,
        "decay": candidate.decay,
    },
    "generation": candidate.generation,
    "tag": candidate.tag,
    "simulation": None,
}

if result is not None:
    record["simulation"] = {
        "alpha_id": result.alpha_id,
        "sharpe": result.sharpe,
        "fitness": result.fitness,
        "drawdown": result.drawdown,
        "twoyearsharpe": result.twoyearsharpe,
        "fail_num": result.fail_num,
        "score": result.score,
    }

with HISTORY_FILE.open("a", encoding="utf-8") as file:
    file.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"Recorded experiment: {candidate.factor_id}")
print(f"History file: {HISTORY_FILE}")
```

if __name__ == "__main__":
    print("WQBKit Alpha Experiment Tracker")
    print("Tracker loaded successfully.")
print("No BRAIN simulations or API requests were performed.")
PY
python ~/wqbkit-alpha/alpha_experiment_tracker.py

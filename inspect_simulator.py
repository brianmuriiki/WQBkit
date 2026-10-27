import inspect

from wqbkit.modules.regular_alpha.alpha_simulator.alpha_simulator import (
AlphaSimulator,
)

print("=" * 65)
print("WQBKit AlphaSimulator")
print("=" * 65)

print("\nModule:", AlphaSimulator.__module__)

try:
  print("Constructor:", inspect.signature(AlphaSimulator))
except (TypeError, ValueError):
 print("Constructor signature unavailable")

for name, method in inspect.getmembers(
AlphaSimulator,
predicate=inspect.isfunction,
):
  try:
    signature = inspect.signature(method)
  except (TypeError, ValueError):
    signature = "(signature unavailable)"

  print(f"\n{name}{signature}")

  if name in {"__init__", "simulate", "run", "login"}:
    try:
      print(inspect.getsource(method)[:2500])
    except (OSError, TypeError):
      pass


print("\nInspection complete.")

import inspect

from wqbkit.modules.regular_alpha.alpha_simulator.alpha_simulator import (
AlphaSimulator,
)

methods_to_inspect = [
"score_alpha_comprehensive",
"generate_alpha",
"combine_alpha",
"single_simulate",
"multi_simulate",
"get_simulation_result",
"get_today_simulations_count",
]

for method_name in methods_to_inspect:method = getattr(AlphaSimulator, method_name)


print("\n" + "=" * 70)
print(f"METHOD: {method_name}")
print("SIGNATURE:", inspect.signature(method))

try:
    print("\nIMPLEMENTATION:")
    print(inspect.getsource(method)[:4500])
except (OSError, TypeError) as error:
    print("Source unavailable:", error)


print("\nInspection complete.")

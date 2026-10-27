import inspect

from wqbkit.modules.regular_alpha.alpha_machine.alpha_generator import (
AlphaGenerator,
)

generator = AlphaGenerator()

methods = [
"zero_order_factory",
"first_order_factory",
"second_order_factory",
"third_order_factory",
]

print("=" * 65)
print("WQBKit ADVANCED ALPHA RESEARCH")
print("=" * 65)

for method_name in methods:method = getattr(generator, method_name)


print(f"\n{'=' * 65}")
print(f"METHOD: {method_name}")
print(f"Signature: {inspect.signature(method)}")

try:
    source = inspect.getsource(method)
    print("\nImplementation:")
    print(source[:3500])
except (OSError, TypeError) as error:
    print(f"Could not inspect implementation: {error}")


print("\nInspection complete.")

import inspect

from wqbkit.modules.regular_alpha.alpha_machine.alpha_generator import AlphaGenerator
from wqbkit.modules.regular_alpha.alpha_simulator.alpha_simulator import AlphaSimulator
from wqbkit.modules.correlation.alpha_calc_corr import AlphaCalcCorr

classes = [AlphaGenerator, AlphaSimulator, AlphaCalcCorr]

for cls in classes:
 print("\n" + "=" * 65)
print("CLASS:", cls.__name__)
print("MODULE:", cls.__module__)


try:
    print("CONSTRUCTOR:", inspect.signature(cls))
except (TypeError, ValueError):
    print("CONSTRUCTOR: unavailable")

for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
    try:
        signature = inspect.signature(method)
    except (TypeError, ValueError):
        signature = "(signature unavailable)"

    print(f"  {name}{signature}")



from alpha.mathlib import geometry
import sys

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search:
# 1. current folder
# 2. folders in PYTHONPATH env var
# 3. installation folder (sys.prefix)
print("sys.prefix: {}".format(sys.prefix))
print("sys.executable: {}".format(sys.executable))
print()
for path in sys.path:
    print(path)

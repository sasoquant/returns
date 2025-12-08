from calculations import return_value

p0 = 100.00
p1 = 115.00
r = return_value(p0, p1)

print(f"start price = {p0}")
print(f"end price = {p1}")
print(f"return = {r}")
print(f"return % = {r * 100}%")

print("\n\n")
print("=" * 50)
print("Gain")
print("=" * 50)

p0 = 100
p1 = 120
r = return_value(p0, p1)

print(f"start price = {p0}")
print(f"end price = {p1}")
print(f"return = {r}")
print(f"return % = {r * 100}%")

print("\n\n")
print("=" * 50)
print("Loss")
print("=" * 50)

p0 = 100
p1 = 85
r = return_value(p0, p1)

print(f"start price = {p0}")
print(f"end price = {p1}")
print(f"return = {r}")
print(f"return % = {r * 100}%")

print("\n\n")
print("=" * 50)
print("Flat")
print("=" * 50)

p0 = 100
p1 = 100
r = return_value(p0, p1)

print(f"start price = {p0}")
print(f"end price = {p1}")
print(f"return = {r}")
print(f"return % = {r * 100}%")

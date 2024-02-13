universe = set(int(x) for x in input().split(", "))
n = int(input())
sets = []
for _ in range(n):
    sets.append(set(int(x) for x in input().split(", ")))
used_sets = []

while universe:
    max_set = max(sets, key=lambda x: len(universe.intersection(x)))
    sets.remove(max_set)
    used_sets.append(max_set)
    universe -= set(max_set)

print(f"Sets to take ({len(used_sets)}):")
[print("{ " + ', '.join(str(x) for x in sorted(s)) + " }") for s in used_sets]

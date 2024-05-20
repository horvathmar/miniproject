print("Téglatest számítások ----------------------------------------------------\n")
me: str = input("Adja meg a mértékegységet: ")

edges: list[float] = []
for i in range(0, 3):
    edge = float(input(f"Téglatest {i+1}. élének a hossza: "))
    edges.append(edge)

print("\n")
Vtegla: float = round(edges[0] * edges[1] * edges[2], 2)
Ategla: float = round(2 * (edges[0] * edges[1] + edges[0] * edges[2] + edges[1] * edges[2]), 2)

print(f"Téglatest térfogata: {Vtegla} {me}3")
print(f"Téglatest felszíne: {Ategla} {me}2")
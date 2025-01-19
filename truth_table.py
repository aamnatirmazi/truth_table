from tabulate import tabulate
truth_table_headers = ['P', 'Q', 'R', 'P -> R', 'Q -> R', '(P -> R) ^ (Q -> R)', 'P v Q', 'P v Q -> R', '(P -> R) ^ (Q -> R) <-> P v Q -> R']

# (P --> Q) or (Q --> R) <-> ( P and Q --> R) ?
def truth_table(p, q, r):
    P = 1 if p else 0
    Q = 1 if q else 0
    R = 1 if r else 0
    # A: P -> R
    A = 1 if (not p or r) else 0
    # B: Q -> R
    B = 1 if (not q or r) else 0
    # C: (P -> R) ^ (Q -> R) => A and B
    C = 1 if A and B else 0
    # D: P v Q  => P or Q
    D = 1 if (p or q) else 0
    # E = P v Q -> R => not D or R
    E = 1 if (not D or r) else 0
    # F => (P -> R) ^ (Q -> R) <-> P v Q -> R => C == E
    F = 1 if C == E else 0

    return P, Q, R, A, B, C, D, E, F
grid = []
for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
	        grid.append(truth_table(p, q, r))

print(tabulate(grid, headers = truth_table_headers, tablefmt="grid"))

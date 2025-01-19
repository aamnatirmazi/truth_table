from tabulate import tabulate
truth_table_headers = ['P', 'Q', 'R', 'P -> R', 'Q -> R', '(P -> R) ^ (Q -> R)', 'P v Q', 'P v Q -> R', '(P -> R) ^ (Q -> R) <-> P v Q -> R']

# (P --> Q) or (Q --> R) <-> ( P and Q --> R) ?
def truth_table(p, q, r):
    P = 'T' if p else 'F'
    Q = 'T' if q else 'F'
    R = 'T' if r else 'F'
    # A: P -> R
    A = 'T' if (not p or r) else 'F'
    # B: Q -> R
    B = 'T' if (not q or r) else 'F'
    # C: (P -> R) ^ (Q -> R) => A and B
    C = 'T' if A and B else 'F'
    # D: P v Q  => P or Q
    D = 'T' if (p or q) else 'F'
    # E = P v Q -> R => not D or R
    E = 'T' if (not D or r) else 'F'
    # F => (P -> R) ^ (Q -> R) <-> P v Q -> R => C == E
    F = 'T' if C == E else 'F'

    return P, Q, R, A, B, C, D, E, F
grid = []
for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
	        grid.append(truth_table(p, q, r))
print(tabulate(grid, headers = truth_table_headers, tablefmt="grid"))

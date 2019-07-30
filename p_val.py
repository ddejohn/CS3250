# Devon DeJohn
# MTH-3210
# HW13

from scipy.special import erf


SQ2 = 2**0.5


def phi(z):
    return round(0.5*(1 + erf(z/SQ2)), ndigits=4)


def p_gt(T):
    return round(1 - phi(T), ndigits=4)


def p_lt(T):
    return round(phi(T), ndigits=4)


def p_neq(T):
    return round(2*(1 - phi(abs(T))), ndigits=4)


def p_val(H, alpha, T):
    p = {
        "gt": p_gt,
        "lt": p_lt,
        "neq": p_neq,
    }[H](T)

    if p > 0.1:
        conc = f"DEFINITE ACCEPTANCE"
    elif p < 0.01:
        conc = f"DEFINITE REJECTION"
    elif p >= alpha:
        conc = f"BORDERLINE ACCEPTANCE"
    elif p < alpha:
        conc = f"BORDERLINE REJECTION"

    return {
        "T": T,
        "area": phi(T), 
        "alpha": alpha,
        "p-value": p,
        "conclusion": conc,
    }


tests = [
    ["gt", 0.02, 1.56],
    ["lt", 0.08, -1.84],
    ["neq", 0.10, -1.35],
    ["gt", 0.05, 3.14],
    ["lt", 0.07, -1.06],
    ["neq", 0.04, 2.22]
]

print()
for index, test in enumerate(tests):
    H, alpha, T = test
    result = p_val(H, alpha, T)
    print(f"\n{index+1}:")
    for key, val in result.items():
        print(f"    {key}: {val}")
print()

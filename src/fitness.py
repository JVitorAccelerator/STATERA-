import copy
from src.config import SELIC_MENSAL

def beneficio_divida(divida, amort):
    r = divida["juros_anual"] / 12
    saldo_novo = max(0, divida["saldo"] * (1 + r) - amort)
    return divida["saldo"] - saldo_novo

def fitness(p, renda, gastos_min, dividas):
    if sum(p.values()) > renda:
        return -1e9

    dividas_sim = copy.deepcopy(dividas)
    beneficio = 0

    for _ in range(12):
        for i, d in enumerate(dividas_sim):
            amort = p[f"amort_divida_{i}"]
            beneficio += beneficio_divida(d, amort)
            d["saldo"] = max(0, d["saldo"] * (1 + d["juros_anual"] / 12) - amort)

    selic_total = 0
    for _ in range(12):
        selic_total = selic_total * (1 + SELIC_MENSAL) + p["selic"]

    lucro_selic = selic_total - 12 * p["selic"]

    penal = sum(
        max(0, gastos_min[k] - p[k]) * 5
        for k in gastos_min
    )

    return beneficio + lucro_selic - penal

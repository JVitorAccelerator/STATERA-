from src.config import SELIC_MENSAL

def simular_12_meses(solucao, dividas):
    dividas = [d.copy() for d in dividas]
    patrimonio = 0

    for mes in range(12):
        patrimonio = patrimonio * (1 + SELIC_MENSAL) + solucao["selic"]

        for i, d in enumerate(dividas):
            amort = solucao[f"amort_divida_{i}"]
            d["saldo"] = max(
                0,
                d["saldo"] * (1 + d["juros_anual"] / 12) - amort
            )

    return dividas, patrimonio

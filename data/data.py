import sys

def input_familia():
    renda = float(input("Renda mensal da família: "))
    sys.stdout.flush()

    gastos = {
        "comida": float(input("Gasto com comida: ")),
        "agua": float(input("Gasto com água: ")),
        "luz": float(input("Gasto com luz: ")),
        "aluguel": float(input("Gasto com aluguel: ")),
        "manutencao": float(input("Gasto com manutenção: ")),
        "transporte": float(input("Gasto com transporte: ")),
        "lazer": float(input("Gasto com lazer: ")),
        "outros": float(input("Outros gastos: "))
    }

    n = int(input("Quantidade de dívidas: "))

    dividas = []
    for i in range(n):
        print(f"\nDívida {i+1}", flush=True)
        dividas.append({
            "saldo": float(input("Saldo: ")),
            "juros_anual": float(input("Juros anual (ex: 0.12): ")),
            "parcela_minima": float(input("Parcela mínima: "))
        })

    return renda, gastos, dividas

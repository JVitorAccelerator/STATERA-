from data.data import input_familia
from src.pso import executar_pso
from src.simulation import simular_12_meses
from src import config

def main():
    renda, gastos, dividas = input_familia()

    gbest, score = executar_pso(
        renda, gastos, dividas,
        {
            "N": config.NUM_PARTICULAS,
            "ITER": config.NUM_ITERACOES,
            "W": config.W,
            "C1": config.C1,
            "C2": config.C2
        }
    )

    dividas_finais, patrimonio = simular_12_meses(gbest, dividas)

    print("\n MELHOR DISTRIBUIÇÃO")
    for k, v in gbest.items():
        print(f"{k:15s}: R$ {v:.2f}")

    print("\n SITUAÇÃO APÓS 12 MESES")
    for i, d in enumerate(dividas_finais):
        print(f"Dívida {i+1} saldo final: R$ {d['saldo']:.2f}")

    print(f"\n Patrimônio em SELIC: R$ {patrimonio:.2f}")
    print(f"Fitness final: {score:.2f}")

if __name__ == "__main__":
    main()

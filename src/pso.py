import random
import copy
from src.fitness import fitness

def gerar_particula(categorias, minimos, renda):
    p = {k: minimos.get(k, 0) for k in categorias}
    restante = renda - sum(p.values())

    for k in categorias:
        if restante <= 0:
            break
        delta = random.uniform(0, restante)
        p[k] += delta
        restante -= delta

    return p

def limitar(p, renda):
    excesso = sum(p.values()) - renda
    if excesso > 0:
        p["selic"] = max(0, p["selic"] - excesso)
    return p

def executar_pso(renda, gastos, dividas, config):
    categorias = list(gastos.keys())
    categorias += [f"amort_divida_{i}" for i in range(len(dividas))]
    categorias.append("selic")

    minimos = gastos.copy()
    for i, d in enumerate(dividas):
        minimos[f"amort_divida_{i}"] = d["parcela_minima"]
    minimos["selic"] = 0

    particulas = [gerar_particula(categorias, minimos, renda)
                  for _ in range(config["N"])]

    velocidades = [{k: 0 for k in categorias} for _ in particulas]

    pbest = copy.deepcopy(particulas)
    pbest_score = [
        fitness(p, renda, gastos, dividas) for p in particulas
    ]

    gbest = pbest[pbest_score.index(max(pbest_score))]
    gbest_score = max(pbest_score)

    for _ in range(config["ITER"]):
        for i in range(len(particulas)):
            for k in categorias:
                r1, r2 = random.random(), random.random()
                velocidades[i][k] = (
                    config["W"] * velocidades[i][k]
                    + config["C1"] * r1 * (pbest[i][k] - particulas[i][k])
                    + config["C2"] * r2 * (gbest[k] - particulas[i][k])
                )
                particulas[i][k] += velocidades[i][k]

            particulas[i] = limitar(particulas[i], renda)
            score = fitness(particulas[i], renda, gastos, dividas)

            if score > pbest_score[i]:
                pbest[i] = copy.deepcopy(particulas[i])
                pbest_score[i] = score

                if score > gbest_score:
                    gbest = copy.deepcopy(particulas[i])
                    gbest_score = score

    return gbest, gbest_score

## 📁 Estrutura do Projeto

### `main.py`
Arquivo principal do projeto.  
Responsável por chamar e executar todas as funções necessárias para o processo de otimização utilizando **Particle Swarm Optimization (PSO)**.

### `data.py`
Arquivo responsável por lidar com os dados do usuário, como **renda total** e **gastos**.  
Na mesma pasta, o arquivo `banco_dados_familias_pso.csv` contém dados previamente gerados para **simular situações reais**.

### `config.py`
Arquivo de configuração do projeto.  
Define parâmetros do algoritmo, como:
- Número de partículas  
- Fatores de velocidade das partículas  
- Número de iterações  

### `fitness.py`
Implementa as **funções de avaliação (fitness)**.  
Essas funções medem os benefícios gerados por cada partícula, permitindo a comparação entre soluções e a escolha da melhor alternativa.

### `pso.py`
Contém a implementação central do **Particle Swarm Optimization**.  
Inclui funções para:
- Geração das partículas  
- Limitação das soluções para opções financeiramente viáveis  
- Execução do algoritmo PSO  

### `simulation.py`
Responsável por simular os resultados ao longo do tempo.  
Simula o que aconteceria caso o usuário seguisse a **melhor solução encontrada** pelo PSO durante um período de **12 meses**.

---

## ▶️ Instruções de Execução

1. Certifique-se de ter o **Python 3.9 ou superior** instalado.
2. Clone o repositório:
   ```bash
   git clone https://github.com/JVitorAccelerator/STATERA-
3. Vá para a pasta principal:
   ```bash
   cd STATERA-
4. Execute a main.py:
   ```bash
   python main.y

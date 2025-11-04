Aqui está seu **README** reescrito e formatado para o GitHub — direto, limpo e com boa hierarquia visual:

---

# 🧮 Comunicação Ponto a Ponto em MPI — Ping-Pong

## 📘 Descrição

Este projeto implementa uma simulação de **comunicação ponto a ponto (Point-to-Point)** utilizando **MPI (Message Passing Interface)** por meio da biblioteca **mpi4py**.

O objetivo é medir o **tempo de transmissão e recepção** de mensagens entre dois processos — o clássico experimento **Ping-Pong** — e calcular a **taxa de transferência (MB/s)** para diferentes tamanhos de mensagens.

Os resultados são exportados em **CSV**, permitindo análise posterior em planilhas ou ferramentas de visualização.

---

## ⚙️ Tecnologias Utilizadas

* 🐍 **Python 3.x**
* 🔁 **mpi4py** — Interface Python para MPI
* 💡 **NumPy** — Geração eficiente de arrays de doubles aleatórios
* 📄 **CSV (módulo nativo)** — Exportação dos resultados

---

## 📦 Instalação

Antes de executar o programa, é necessário ter o **MPI** instalado no sistema (ex: *OpenMPI*) e a biblioteca **mpi4py** configurada no Python.

### 🔧 Passos no macOS / Linux:

```bash
# Instale o OpenMPI
brew install open-mpi           # macOS
# ou
sudo apt-get install openmpi-bin openmpi-common openmpi-doc libopenmpi-dev  # Linux (Ubuntu/Debian)

# Instale as dependências Python
pip install mpi4py numpy
```

---

## ▶️ Execução

Execute o programa com **dois processos**, simulando o envio e retorno da mensagem (ping-pong):

```bash
mpirun -np 2 python3 mpi.py
```

📌 O parâmetro `-np 2` é **obrigatório**, pois o código foi desenvolvido para dois processos (um envia e o outro responde).

---

## 📊 Funcionamento

1. Para cada iteração, o programa gera um array de tamanho `n = 2^exp` (de 1 até 2¹⁹ doubles).
2. **Processo 0** envia o array para o **Processo 1** (`Send()`).
3. **Processo 1** recebe o array (`Recv()`) e devolve-o (`Send()`).
4. **Processo 0** mede o tempo total (ida + volta) com `MPI.Wtime()`.
5. O código calcula:

   * ⏱️ **Tempo total (s)**
   * 📦 **Volume transferido (n * 8 bytes * 2)**
   * ⚡ **Taxa de transferência (MB/s)**
6. Todos os resultados são salvos em **Resultados.csv**.

---

## 📁 Estrutura do Projeto

```
📂 Projeto-MPI-PingPong
│
├── mpi.py             # Código principal do experimento
├── Resultados.csv     # Saída gerada automaticamente após execução
└── README.md          # Este arquivo de documentação
```

---

## 🧾 Exemplo de Saída no Terminal

```
Processo 0 enviou os dados!
Processo 1 recebeu os dados
Processo 1 devolveu os dados!
Processo 0 recebeu os dados!
1 doubles | tempo: 1.030000e-04s | taxa 0.15 MB/s
...
Resultados salvos em 'Resultados.csv'!
```

---

## 📑 Exemplo de Saída no Arquivo CSV

| operação  | n (doubles) | tempo (s)    | taxa (MB/s) |
| --------- | ----------- | ------------ | ----------- |
| Send/Recv | 1           | 1.030000e-04 | 0.15        |
| Send/Recv | 2           | 2.900000e-05 | 1.05        |
| Send/Recv | 4           | 1.700000e-05 | 3.59        |
| ...       | ...         | ...          | ...         |

---

## 🧠 Conceito Envolvido

O experimento implementa o padrão **Ping-Pong**, uma técnica clássica de **benchmark** em sistemas distribuídos.

Mede o desempenho da comunicação entre dois processos em termos de:

* 🕓 **Latência:** tempo gasto para enviar e receber uma mensagem.
* 🚀 **Largura de banda:** taxa de transferência de dados (MB/s).

Essas métricas são fundamentais para avaliar o desempenho de **clusters**, **redes interconectadas** e **aplicações paralelas**.

---

## 💬 Observações

* O programa **não sincroniza** a ordem das mensagens no terminal, pois o MPI executa processos concorrentemente.
* Evita qualquer sincronização artificial (`comm.Barrier()`), que alteraria as medições.
* Apenas o **Processo 0** grava os resultados no CSV.
* Desenvolvido com fins **didáticos** para estudo de comunicação ponto a ponto em MPI.

---

## 👨‍💻 Autor

**Leonardo Farias**
📚 *Disciplina:* Sistemas Distribuídos
🏛️ *Projeto:* Comunicação Ponto a Ponto com MPI (Ping-Pong)

---

Quer que eu formate a versão final como `README.md` (com Markdown real e emojis prontos pra copiar/colar no GitHub)?

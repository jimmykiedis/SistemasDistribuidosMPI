🧮 Comunicação Ponto a Ponto em MPI — Ping-Pong
  📘 Descrição
    Este projeto implementa uma simulação de comunicação ponto a ponto (Point-to-Point) utilizando MPI (Message Passing Interface) com a biblioteca mpi4py.
    O objetivo é medir o tempo de transmissão e recepção de mensagens entre dois processos (Processo 0 e Processo 1) — o clássico experimento Ping-Pong — e calcular a taxa de transferência (MB/s) para diferentes tamanhos de mensagem.
    O código também exporta os resultados em formato CSV, permitindo análise posterior em planilhas ou ferramentas de visualização.

  ⚙️ Tecnologias Utilizadas
    Python 3.x
    mpi4py — Interface Python para MPI
    NumPy — Para geração eficiente de arrays de doubles aleatórios
    CSV (módulo nativo) — Para exportar os resultados em planilha

  📦 Instalação
  Antes de executar o programa, é necessário ter o MPI instalado no sistema (ex: OpenMPI) e a biblioteca mpi4py configurada no Python.
    🔧 Passos no macOS / Linux:
      # Instale o OpenMPI (se ainda não tiver)
      brew install open-mpi           # macOS
      # ou
      sudo apt-get install openmpi-bin openmpi-common openmpi-doc libopenmpi-dev  # Linux (Ubuntu/Debian)
      # Instale o mpi4py
      pip install mpi4py numpy

  ▶️ Execução
    O programa deve ser executado com dois processos, simulando o envio e retorno (ping-pong) da mensagem.
    No terminal, dentro da pasta do projeto, execute:
      mpirun -np 2 python3 mpi.py
    📌 O parâmetro -np 2 é obrigatório, pois o código foi desenvolvido especificamente para dois processos (um envia e o outro responde).

  📊 Funcionamento
    O programa gera, para cada iteração, um array de tamanho n = 2^exp (de 1 até 2^19 doubles).
    O Processo 0 envia esse array para o Processo 1 usando Send().
    O Processo 1 recebe o array (Recv()), e devolve-o ao Processo 0 (Send() novamente).
    O Processo 0 mede o tempo total da operação (ida + volta) usando MPI.Wtime().
    O código calcula:
    O tempo total (tempo (s))
    O volume de dados transferidos (n * 8 bytes * 2)
    A taxa de transferência (MB/s)
    Todos os resultados são salvos em Resultados.csv.

  📁 Estrutura do Projeto
    📂 Projeto-MPI-PingPong
      │
      ├── mpi.py                # Código principal do experimento
      ├── Resultados.csv        # Saída gerada automaticamente após execução
      └── README.md             # Este arquivo de documentação

  🧾 Exemplo de Saída no Terminal
    Processo 0 enviou os dados!
    Processo 1 recebeu os dados
    Processo 1 devolveu os dados!
    processo 0 Recebeu os dados!
           1 doubles | tempo: 1.030000e-04s | taxa 0.15 MB/s
    ...
    Resutlados Salvos em 'Resultados.csv do repositório desse programa!'
    
  📑 Exemplo de Saída no Arquivo CSV
    | operação  | n (doubles) | tempo (s)    | taxa (MB/s) |
    | --------- | ----------- | ------------ | ----------- |
    | Send/Recv | 1           | 1.030000e-04 | 0.15        |
    | Send/Recv | 2           | 2.900000e-05 | 1.05        |
    | Send/Recv | 4           | 1.700000e-05 | 3.59        |
    | ...       | ...         | ...          | ...         |

  🧠 Conceito Envolvido
    Este experimento implementa o padrão Ping-Pong, uma técnica clássica de benchmark em sistemas distribuídos.
    O foco é medir o desempenho da comunicação entre dois processos em termos de:
    Latência: tempo gasto para enviar e receber uma mensagem.
    Largura de banda: taxa de transferência de dados (MB/s).
    Essas métricas são essenciais para avaliar o desempenho de clusters, redes interconectadas e aplicações paralelas.

  💬 Observações
    O programa não sincroniza a ordem das mensagens no terminal, pois o MPI executa os processos de forma concorrente.
    Isso é intencional, pois qualquer sincronização artificial (ex: comm.Barrier() extra) alteraria os tempos medidos.
    Apenas o Processo 0 grava os resultados no CSV.
    O script foi desenvolvido com fins didáticos para estudo de comunicação ponto a ponto em MPI.

  👨‍💻 Autor
    Leonardo Farias
    📚 Disciplina: Sistemas Distribuídos
    🏛️ Projeto: Comunicação Ponto a Ponto com MPI (Ping-Pong)

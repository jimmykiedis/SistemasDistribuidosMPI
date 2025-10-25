🧮 Comunicação Ponto a Ponto em MPI — Ping-Pong
  Este projeto implementa uma simulação de comunicação ponto a ponto utilizando a biblioteca MPI (Message Passing Interface) com o módulo mpi4py em Python. O objetivo é medir o tempo de transmissão e recepção de mensagens entre dois processos, o Processo 0 e o Processo 1, no clássico experimento conhecido como “Ping-Pong”. A partir disso, calcula-se também a taxa de transferência em megabytes por segundo (MB/s) para diferentes tamanhos de mensagem.
  O código foi desenvolvido de forma didática, com comentários explicativos em cada etapa, e realiza a exportação dos resultados em um arquivo CSV, permitindo análise posterior em planilhas ou ferramentas de visualização.
⚙️ Tecnologias utilizadas
  O programa foi desenvolvido em Python 3 e faz uso das bibliotecas mpi4py (para comunicação entre processos MPI), NumPy (para geração eficiente de arrays de números aleatórios do tipo double) e o módulo nativo csv (para exportação dos resultados).
📦 Instalação
  Para executar o programa, é necessário ter o MPI instalado no sistema, como o OpenMPI, e a biblioteca mpi4py configurada no ambiente Python. Em sistemas baseados em macOS, pode-se instalar o OpenMPI utilizando o Homebrew. Já em sistemas Linux, é possível instalar via apt-get. Após isso, basta instalar as dependências Python mpi4py e numpy usando o pip.
▶️ Execução
  O programa deve ser executado com dois processos, simulando o envio e retorno da mensagem. Isso é feito a partir do terminal, dentro da pasta onde o código está localizado. É importante ressaltar que o parâmetro “-np 2” é obrigatório, pois o código foi projetado especificamente para dois processos: um responsável pelo envio e outro pela recepção e devolução dos dados.
📊 Funcionamento
  O funcionamento segue as seguintes etapas. Primeiro, o programa gera um array de tamanho n = 2 elevado a exp, variando exponencialmente de 1 até 2¹⁹ doubles. Em seguida, o Processo 0 envia o array para o Processo 1 utilizando o método Send. O Processo 1 recebe os dados com Recv, e então devolve o mesmo array de volta ao Processo 0, completando assim o ciclo de envio e recepção.
  O Processo 0 mede o tempo total da operação, somando o tempo de ida e volta, por meio do método MPI.Wtime(). A partir desses valores, o código calcula o tempo total, o volume total de dados transferidos (considerando que cada double ocupa 8 bytes e que há envio e retorno) e a taxa de transferência em megabytes por segundo. Por fim, todos os resultados são armazenados em uma lista de dicionários e exportados automaticamente para um arquivo CSV denominado “Resultados.csv”.
📁 Estrutura do projeto
  O projeto é composto basicamente por três arquivos: o script principal (mpi.py), o arquivo de resultados (Resultados.csv), gerado automaticamente após a execução, e o arquivo de documentação (README.md).
🧾 Exemplo de saída no terminal
  Durante a execução, o terminal exibirá mensagens informativas sobre o envio e recebimento dos dados, seguidas dos resultados de tempo e taxa de transferência para cada tamanho de mensagem. É importante destacar que as mensagens podem aparecer fora de ordem no terminal, devido à execução paralela dos processos MPI. Essa desorganização é natural e não afeta a precisão das medições.
📑 Saída em arquivo CSV
  O arquivo gerado “Resultados.csv” conterá uma tabela com as colunas: operação, n (doubles), tempo (s) e taxa (MB/s). Cada linha representa uma medição correspondente a um tamanho de array diferente, com a operação “Send/Recv” indicando o tipo de comunicação realizada.
🧠 Conceito envolvido
  O experimento segue o padrão clássico de benchmark “Ping-Pong”, amplamente utilizado para avaliar o desempenho de sistemas distribuídos. Esse modelo mede tanto a latência (o tempo necessário para enviar e receber uma mensagem) quanto a largura de banda (a taxa de transferência de dados). Tais métricas são essenciais para compreender o comportamento e a eficiência de clusters, redes interconectadas e aplicações paralelas que dependem de comunicação entre processos.
💬 Observações
  O programa não impõe sincronização adicional para forçar a ordem das mensagens no terminal, pois isso alteraria os resultados dos tempos medidos. Apenas o Processo 0 é responsável por calcular os tempos e gravar as informações no arquivo CSV. O código foi desenvolvido com fins acadêmicos e didáticos, servindo como um exemplo prático de comunicação ponto a ponto utilizando MPI em Python.
👨‍💻 Autor
Projeto desenvolvido por Leonardo Farias, como parte das atividades da disciplina de Sistemas Distribuídos.

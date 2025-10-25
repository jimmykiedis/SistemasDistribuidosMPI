from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
n = 10                                  #nosso array vai começar com 10

if rank == 0:
    data = np.random.random(n)          #vamos criar um array de n doubles aleatórios

    inicio = MPI.Wtime()
    comm.Send(data, dest=1)             #enviando para o processo 1
    comm.Recv(data, source=1)           #recebendo os dados de volta do processo 1
    fim = MPI.Wtime()

    tempo = fim - inicio
    print(f"[P0] tamanho {n} doubles | tempo total: {tempo:.6f} s")

elif rank == 1:
    message = np.empty(n, dtype='d')   #vamos criar um espaço vazio para guardados os dados recebidos
    comm.Recv(message, source=0)         #agora vamos receber os dados
    comm.Send(message, dest=0)           #vamos retornar ele ao p0
    print("processo 1 devolveu os dados!")



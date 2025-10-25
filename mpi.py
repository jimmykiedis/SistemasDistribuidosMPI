from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
n = 10                                  #nosso array vai começar com 10

if rank == 0:
    data = np.random.ramdom(10)         #vamos criar um array de 10 doubles aleatórios
    comm.send(data, dest=1)             #enviando para o processo 1
    comm.recv(data, source=1)           #recebendo os dados de volta do processo 1
    print("Processo 0 recebeu de volta!")
elif rank == 1:
    message = np.empity(10, dtype='d')   #vamos criar um espaço vazio para guardados os dados recebidos
    comm.recv(message, source=0)         #agora vamos receber os dados
    comm.send(message, dest=0)           #vamos retornar ele ao p0
    print("processo 1 devolveu os dados!")


inicio = MPI.Wtime()
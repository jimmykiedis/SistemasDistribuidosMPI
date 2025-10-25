from mpi4py import MPI
import numpy as np
import csv

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
resultados = []                             #vamos criar uma tupla para armezenar os dados do relatório

if size != 2:
    if rank == 0:
        print("Este programa requer exatamente 2 processos (-np 2)!")
    exit()

for exp in range (20):                  #vamos preparar a exponenciacao
    n = 2**exp                          #vamos deixar o valor de n dinamicamente com um laço de repetição
    
    if rank == 0:
        data = np.random.random(n)          #vamos criar um array de n doubles aleatórios com o numpy por que é mais rápido
        comm.Barrier()                      #precisei aprender a usar isso aqui para poder medir corretamente o tempo, já que as vezes o P1 fica preso fazendo algo mais lento
        inicio = MPI.Wtime()
        comm.Send(data, dest=1)             #enviando para o processo 1
        print("Processo 0 enviou os dados!")
        comm.Recv(data, source=1)           #recebendo os dados de volta do processo 1
        print("processo 0 Recebeu os dados!")
        fim = MPI.Wtime()                   #criamos o cue do inicio e o cue do fim, depois é só fazer uma subtração e teremos o tempo gasto nesse trecho

        tempo = fim - inicio
        
        bytes_total = 2 * n * 8             #aqui estamos calculando qual o tamanho a mensagem terá a depender do tanto de doubles que vamos enviar, isso já contando com a ida e volta
        mb = bytes_total / (1024**2)        #calculo básico do tamanho em megabytes
        taxa = mb / tempo

        resultados.append({                 #vamos criar o discionario para depois poder exportar
            "n (doubles)": n,
            "tempo (s)": f"{tempo:.6e}",    #vamos deixar formato na saida também
            "taxa (MB/s)": f"{taxa:.2f}"
            }
        )

        print(f"{n:10d} doubles | tempo: {tempo:.6e}s | taxa {taxa:.2f} MB/s")

    elif rank == 1:                         #aqui é o que o P1 vai rodar
        received = np.empty(n, dtype='d')   #vamos criar um espaço vazio para guardados os dados recebidos, recv precisa guardar o dado na memória, diferente do send que le direto do array
        comm.barrier()
        comm.Recv(received, source=0)       #agora vamos receber os dados
        print("Processo 1 recebeu os dados")
        comm.Send(received, dest=0)         #vamos retornar ele ao p0
        print("Processo 1 devolveu os dados!")

if rank == 0:
    with open("Resultados.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["n (doubles)", "tempo (s)", "taxa (MB/s)"])
        for r in resultados:
            writer.writerow([r["n (doubles)"], r["tempo (s)"], r["taxa (MB/s)"]])

    print("\n Resutlados Salvos em 'Resultados.csv do repositório desse programa!'")
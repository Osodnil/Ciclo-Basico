# Importando a biblioteca random para sortear os nomes
import random

# criando as listas com os nomes dos alunos que fizeram e com os nomes dos que não fizeram o curso de python anteriormente
nomes_sem_curso = ["Adriel Faustino de Oliveira", "Amanda Emi Yamasaki", "Ana Werneck de Souza Dias", "Felipe de Souza Lourenço", "Fernanda Mayumi Sakamoto Iizuka", 
                   "Guilherme Vinicius Afonso Dias de Freitas", "Kim Ju Hyang", "Leticia Amy Siramidu", "Marcelo Tamay Honda", "Maria Dulce Navarro de Britto Matos", 
                   "Mateus Pamio Forcione de Oliveira e Souza", "Milena da Silva Ramos", "Paulo Sergio Almeida de Oliveira", "Theo Borten Radesca Migliano", "Vitor Tatiama Gouveia"]
nomes_com_curso = ["André Menniti Pennini", "Fernanda Mees Antunes", "Gabriel Grub Vidal da Silva", "Henrique Nogueira Pedro Lindoso"]

# criando a função para sortear os nomes dos grupos com 5 integrantes
def sorteio_grupo():
    n = 0
    resultado_sorteados_sem_curso = []
    while n < 4:
        sorteados_sem_curso = random.choice(nomes_sem_curso)
        resultado_sorteados_sem_curso.append(sorteados_sem_curso)
        nomes_sem_curso.remove(sorteados_sem_curso)
        n += 1
    resultado_sorteados_com_curso = []
    sorteados_com_curso = random.choice(nomes_com_curso)
    resultado_sorteados_com_curso.append(sorteados_com_curso)
    nomes_com_curso.remove(sorteados_com_curso)
    resultado_final = resultado_sorteados_sem_curso + resultado_sorteados_com_curso
    print(resultado_final)

# criando a função para sortear os nomes do último grupo, com 4 integrantes
def sorteio_grupo_final():
    n = 0
    resultado_sorteados_sem_curso = []
    while n < 3:
        sorteados_sem_curso = random.choice(nomes_sem_curso)
        resultado_sorteados_sem_curso.append(sorteados_sem_curso)
        nomes_sem_curso.remove(sorteados_sem_curso)
        n += 1
    resultado_sorteados_com_curso = []
    sorteados_com_curso = random.choice(nomes_com_curso)
    resultado_sorteados_com_curso.append(sorteados_com_curso)
    nomes_com_curso.remove(sorteados_com_curso)
    resultado_final = resultado_sorteados_sem_curso + resultado_sorteados_com_curso
    print(resultado_final)

# realizando todos os sorteios
sorteio_grupo()
sorteio_grupo()
sorteio_grupo()
sorteio_grupo_final()
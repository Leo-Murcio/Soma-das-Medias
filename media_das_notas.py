turma = {}

for i in range(3):
    nome = input("Escreva seu nome: ")
    nota = float(input("Digite sua nota: "))
    turma[nome] = nota
soma_notas = 0
for nota in turma.values():
    soma_notas += nota
media_notas = soma_notas / len(turma)

print("A média das notas foram:", media_notas)
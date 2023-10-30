from datetime import date

today = date.today()
anoAtual = today.year


idadeMaior = []
IdadeMenor = []
for i in range(8):
    anoNascimento = int(input("digite seu ano de nascimento"))
    if anoAtual - anoNascimento >= 18:
        idadeMaior.append(anoNascimento)
    else:
        IdadeMenor.append(anoNascimento)


print(idadeMaior)
print(IdadeMenor)

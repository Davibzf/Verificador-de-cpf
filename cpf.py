c = 10
d = 10
validacao = 0
segvalidacao = 0
while True:
    cpf = input("Digite um cpf sem ponto: ")
    if len(cpf) == 11:
        break
for i in range(9):
    validacao += int((cpf[i]))*c
    c -=1
validacao = validacao%11
if validacao == 0 or validacao == 1:
    validacao = 0
else:
    validacao = 11 - validacao
for i in range(1,9):
    segvalidacao += int((cpf[i]))*d
    d -=1
segvalidacao += validacao*2
segvalidacao = segvalidacao%11
if segvalidacao == 0 or segvalidacao == 1:
    segvalidacao = 0
else:
    segvalidacao = 11 - segvalidacao
if int(cpf[9])==validacao:
    if int(cpf[10])==segvalidacao:
        print("Cpf valido!!!")
    else:
        print("Cpf invalido!!")
else:
    print("Cpf invalido!!")
    
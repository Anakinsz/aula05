#Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade dehoras trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas aseguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize umcaractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$37,50


turno = input("Digite o seu turno de trabalho (N para noturno, D para diurno): ")
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

if turno == 'N':
    valor_hora = 45.00
else:
    if turno == 'n':
        valor_hora = 45.00
    else:
        valor_hora = 37.50

salario = valor_hora * horas_trabalhadas
print("O valor do seu salário é: R$", salario)
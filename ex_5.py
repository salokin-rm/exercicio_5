"""
Programa: Salário e Descontos
Descrição: Este programa pergunta o número de horas trabalhadas e imprime o salário bruto, líquido e total de descontos. 
           Desconto do imposto = 30%. Hora-aula = R$40,00
Autor: Nikolas Martins
Data: 21/06/2023
Versão: 0.0.1
"""

# Atribuição de variáveis

valores = [0] * 3
horas = [] 

# Entrada de dados

horas = float(input(f"Quantas horas você trabalhou?: "))
        
# Processamento e Saída de dados

for i in range(len(valores)): 
    if i==0:
        valores[i] = horas * 40
        print("Salário Bruto: R$",valores[i],"\n")
        valores[i+1] = ((valores[i]) - (valores[i]*0.3))
        valores[i+2] = valores[i]*0.3
    if i==1:
        print("Salário Líquido: R$",valores[i],"\n")
    if i==2:
        print("Descontos aplicados: R$",valores[i],"\n")
    
# Lê um número (salário) e mostra o seu novo valor com 15% de aumento

valor_salario_atual = float(input("Qual o valor do seu salário? (R$) "))

salario_reajustado = (valor_salario_atual * 15) / 100 + valor_salario_atual

print("O valor do seu salário corrigido em 15% é de {}".format(salario_reajustado))

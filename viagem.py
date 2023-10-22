# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

print("saiba qual o preço da sua passagem")
distancia = float(input("insira a distância que ira percorrer em km:"))
if distancia < 200.0 :
    print(f"o preço da sua passagem é:{0.5*distancia} $")
else :
    print(f"o preço da sua passagem é:{0.45*distancia} $")
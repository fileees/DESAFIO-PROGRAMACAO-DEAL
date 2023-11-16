a = float(input("Insira a primeira nota => "))
b = float(input("Insira a segunda nota => "))
med = (a + b) / 2

if med >= 7:
    print("Aprovado")
elif med < 3:
    print('Reprovado')
else:
    print('Prova final')
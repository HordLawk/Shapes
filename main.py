from figura import Figura
from circulo import Circulo
from retangulo import Retangulo
from quadrado import Quadrado    

tipo = int(input('Figuras:\n1 - Círculo\n2 - Retângulo\n3 - Quadrado\n> '))
if (tipo < 1) or (tipo > 3):
    print('\nFigura invalida!')
    exit()
f: Figura
filledInt = int(input('\nPreenchimento:\n1 - Não\n2 - Sim\n> '))
if (filledInt > 2) or (filledInt < 1):
    print('\nPreenchimento invalido!')
    exit()
filled = bool(filledInt - 1)
cor = input('\nCor: ')
if tipo == 1:
    raio = int(input('Raio: '))
    f = Circulo(cor, filled, raio)
elif tipo == 2:
    base = int(input('Base: '))
    altura = int(input('Altura: '))
    f = Retangulo(cor, filled, base, altura)
elif tipo == 3:
    lado = int(input('Lado: '))
    f = Quadrado(cor, filled, lado)
print(f'\nArea: {f.calcArea()}\nPerimetro: {f.calcPerimetro()}\n{f}')
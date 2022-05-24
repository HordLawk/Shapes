import math
from figura import Figura

class Circulo(Figura):
    raio: int

    def __init__(self, cor: str, filled: bool, raio: int) -> None:
        super().__init__(cor, filled)
        self.raio = raio

    def calcArea(self) -> float:
        return math.pi * (self.raio ** 2)

    def calcPerimetro(self) -> float:
        return math.pi * self.raio * 2
    
    def __str__(self) -> str:
        drawing = ''
        for i in range((self.raio << 1) + 1):
            for j in range((self.raio << 1) + 1):
                dist = math.sqrt(((i - self.raio) ** 2) + ((j - self.raio) ** 2))
                drawing += ((dist < (self.raio + 0.5)) and (self.filled or (dist > (self.raio - 0.5)))) and '##' or '  '
            drawing += '\n'
        return drawing
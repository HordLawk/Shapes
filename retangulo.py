from figura import Figura

class Retangulo(Figura):
    base: int
    altura: int

    def __init__(self, cor: str, filled: bool, base: int, altura: int) -> None:
        super().__init__(cor, filled)
        self.base = base
        self.altura = altura

    def calcArea(self) -> float:
        return self.base * self.altura

    def calcPerimetro(self) -> float:
        return (self.base + self.altura) << 1

    def __str__(self) -> str:
        drawing = ''
        for i in range(self.altura):
            for j in range(self.base):
                drawing += ((not (i % (self.altura - 1))) or (not (j % (self.base - 1))) or self.filled) and '##' or '  '
            drawing += '\n'
        return drawing
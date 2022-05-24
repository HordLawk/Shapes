from figura import Figura

class Quadrado(Figura):
    lado: int

    def __init__(self, cor: str, filled: bool, lado: int) -> None:
        super().__init__(cor, filled)
        self.lado = lado
    
    def calcArea(self) -> float:
        return self.lado ** 2

    def calcPerimetro(self) -> float:
        return self.lado << 2

    def __str__(self) -> str:
        drawing = ''
        for i in range(self.lado):
            for j in range(self.lado):
                drawing += (not (i % ((self.lado - 1) or -1)) or not (j % ((self.lado - 1) or -1)) or self.filled) and '##' or '  '
            drawing += '\n'
        return drawing
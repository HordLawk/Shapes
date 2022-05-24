from abc import ABC, abstractmethod

class Figura(ABC):
    cor: str
    filled: bool

    def __init__(self, cor: str, filled: bool) -> None:
        self.cor = cor
        self.filled = filled
    
    @abstractmethod
    def calcArea(self) -> float:
        pass

    @abstractmethod
    def calcPerimetro(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """

    def __init__(self, operandoA: int, operandoB: int):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        if self.operandoB == 0:
            return 0
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(10, 5)

print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicación: {aritmetica1.multiplicar()}')
print(f'Dividir: {aritmetica1.dividir()}')
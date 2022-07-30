# usar iter y next

lista = [1, 2, 3, 4, 5, 6]
a = iter(lista)

while True:
    try:
        print(next(a))
    except StopIteration:
        break
    
print('finish program')

# generar un iterador
import time

class fibonachiIter():
    
    def __iter__(self):
        """Funcion generador del iterador"""
        self.num1 = 0
        self.num2 = 0
        return self
    
    def __next__(self):
        """funcion que se ejecutara al poner next"""
        if self.num1 == 0 and self.num2 == 0:
            self.num2 = 1
            return 0
        else:
            aux = self.num1 + self.num2
            self.num1, self.num2 = self.num2, aux
            return self.num2
        

fibonachi = fibonachiIter()
for item in fibonachi:
    print(item)
    time.sleep(0.5)
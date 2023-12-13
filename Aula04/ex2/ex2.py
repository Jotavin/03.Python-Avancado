class Fibonacci():
    def __init__(self, range):
        self.anterior, self.atual = 0, 1
        self.proximo = self.anterior + self.atual
        self.index = 0
        self.range = range
    def __iter__(self):
        return self
    
    def create(self):
        while self.range >= self.index:
            yield self.anterior
            self.anterior = self.atual
            self.atual = self.proximo
            self.proximo = self.anterior + self.atual


fib = Fibonacci.create(50)
print(fib)
print(Fibonacci(50))

for n in fib:
    print(n)
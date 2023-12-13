class Fibonacci():
    def __init__(self, num):
        self.anterior, self.atual = 0, 1
        self.proximo = self.anterior + self.atual
        self.num = num
        self.index = 0

    def __iter__(self):
        return self

    
    def __next__(self):
        if self.index <= self.num:
            print(self.anterior)
            self.anterior = self.atual
            self.atual = self.proximo
            self.proximo = self.anterior + self.atual
            self.index += 1
        else:
            raise StopIteration

new_fib = Fibonacci(20)

for num in new_fib:
    num

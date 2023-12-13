# É possível, como um for dentro de for.

def listing(n):
    for i in range(n):
        if i % 2 != 0:
            yield 'Odd'
        for j in range(n):
            if j % 2 == 0:
                yield 'Even'

list = listing(10)
for i in list:
    print(i)

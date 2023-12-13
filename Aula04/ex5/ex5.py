## Utilizando Iterator
# class Count():
#     def __init__(self, num):
#         self.num = num
#         self.index = 0
        

#     def __iter__(self):
#         return self

    
#     def __next__(self):
#         if self.index < self.num:
#             print(self.index)
#             self.index += 1
#         else:
#             raise StopIteration

# new_count = Count(20)

# for number in new_count:
#     number

## Utilizando Generator

def Count2(n):
    for num in range(n):
        yield num

count = Count2(20)

for num in count:
    print(num)
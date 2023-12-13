from typing import Optional

def greetings(name: Optional[str]) -> str:
    if name:
        return f"Olá, {name}!"
    else:
        return "Olá, mundo!"


greetings_1 = greetings("Alice")
greetings_2 = greetings(None)

print(greetings_1)
print(greetings_2)
 




 



 

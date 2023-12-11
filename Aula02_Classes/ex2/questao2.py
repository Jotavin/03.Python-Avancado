class Animal:
    def __init__(self, name: str, specie: str):
        self.name = name
        self.specie = specie

    def introduce(self) -> str:
        return f'{self.name} is of the {self.specie} species'

dog = Animal('Dog', 'Felis catus')
cat = Animal('Cat', 'Persian')
goat = Animal('Goat', 'Capra aegagrus')
print(dog.introduce())
print(cat.introduce())
print(goat.introduce())
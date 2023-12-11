class Animal:
    def __init__(self, name: str, characteristic: str, species: str, integument: str) -> None:
        self.name = name
        self.characteristic = characteristic
        self.species = species
        self.integument = integument
    
    def introduce(self) -> str:
        return f'{self.name} is of the {self.species} species'

    def sound(self):
        if self.name == 'Goat':
            print('Baah Baah Baah')

        elif self.name == 'Dog':
            print('Woof Woof Woof')

        elif self.name == 'Cricket':
            print('Chirp Chirp Chirp')

        else: 
            print('Animal não encontrado.')

cricket = Animal('Cricket', 'Insect', 'Gryllidae', 'Chitinous exoskeleton')
goat = Animal('Goat', 'Mammalia', 'Capra aegagrus', 'Fur')
dog = Animal('Dog', 'Mammalia', 'Canis lupus', 'Fur')
monkey = Animal('Monkey', 'Mammalia', 'Sapajus nigritus', 'Fur')

cricket.sound()
goat.sound()
dog.sound()
monkey.sound()
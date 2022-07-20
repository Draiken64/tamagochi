class WildAnimal:
    def __init__(self, name, legs):
        self.name = name
        self.age = 0
        self.legs = legs

    def give_voice(self):
        print(f"Mam na imie {self.name}, mam {self.age} lat i {self.legs} nogi.")

    def birthday(self):
        self.age += 1


class Lion(WildAnimal):
    def give_voice(self):
        print("Wrrr")
        super().give_voice()


class Parrot(WildAnimal):
    def __init__(self, name, color):
        legs = 2
        super().__init__(name, legs)
        self.color = color

    def give_voice(self):
        print(f"Jestem papugą, mam na imie {self.name}, mam {self.age} lat i {self.legs} nogi.")
        print(f"Jesten koloru {self.color}")


def new_year(zoo):
    for animal in zoo:
        animal.birthday()



def animals_give_voice(zoo):
    for animal in zoo:
        animal.give_voice()


def main():
    # lion = WildAnimal('lion', 4)
    # parrot = WildAnimal('parrot', 2)

    # lion.give_voice()

    simba = Lion("Simba", 4)
    poli = Parrot("Poli", "czerwony")
    alien = WildAnimal("alien", 5)

    zoo = [simba, poli, alien]
    animals_give_voice(zoo) 


    simba.give_voice()





if __name__ == '__main__':
    main()

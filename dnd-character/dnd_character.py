import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        ran_list = [random.randint(1, 6) for _ in range(4)]
        ran_list.sort(reverse=True)
        ran_list.pop()
        return sum(ran_list)


def modifier(const):
    return (const - 10) // 2

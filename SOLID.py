from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.attack()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} наносит {self.weapon.attack()}.")
        else:
            print(f"{self.name} не вооружен!")

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    if fighter.weapon:
        fighter.attack()
        print(f"{monster.name} побежден!")
    else:
        print(f"{fighter.name} не может атаковать, так как не выбрано оружие.")

# Демонстрация работы
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч и атакует
sword = Sword()
fighter.change_weapon(sword)
battle(fighter, monster)

# Боец выбирает лук и атакует
bow = Bow()
fighter.change_weapon(bow)
battle(fighter, monster)
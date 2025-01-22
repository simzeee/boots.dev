class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = 100 * stamina
        self.mana = 10 * intelligence


fireball_damage = 500
potion_mana = 100


class Wizard2:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self):
        self.health = self.health - 500

    def drink_mana_potion(self):
        self.mana = self.mana + 100


fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard3:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana = self.mana - fireball_cost
            target.get_fireballed()

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana

class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
        print(f"{self.name} | Level: {self.level} | Power: {self.power} | "
              f"Health: {self.health} | Coins: {self.coins}")

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health -= self.power
        print(f"{self.name} attacked {other.name}. {other.name}'s health: {other.health}")

    def earn_coins(self, amount):
        self.coins += amount

    def buy_potion(self):
        if self.coins >= 20:
            self.coins -= 20
            self.health += 30
        else:
            print("Not enough coins")

    def level_up(self):
        self.level += 1
        self.power += 5
        print(f"{self.name} reached level {self.level}. New power: {self.power}")


arya = Character("Arya", 10, 100, 50)
bran = Character("Bran", 8, 100, 10)

arya.attack(bran)
bran.attack(arya)
arya.attack(bran)
bran.attack(arya)

arya.buy_potion()
bran.buy_potion()  # فقط ۱۰ سکه دارد → Not enough coins

bran.earn_coins(30)
bran.level_up()

print("Is Arya alive?", arya.is_alive())
print("Is Bran alive?", bran.is_alive())

arya.show_info()
bran.show_info()

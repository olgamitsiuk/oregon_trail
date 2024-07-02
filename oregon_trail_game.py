import random

class Game:
    def __init__(self):
        self.distance_remaining = 1000  # miles to Oregon
        self.food = 500  # pounds of food
        self.health = 100  # player health
        self.money = 300  # dollars
        self.day = 1
        self.status = "Alive"
    
    def travel(self):
        travel_distance = random.randint(30, 60)
        self.distance_remaining -= travel_distance
        self.food -= 5 * travel_distance / 50
        self.health -= random.randint(5, 15)
        self.day += 1
        self.check_status()
    
    def rest(self):
        self.health += random.randint(10, 20)
        self.food -= 10
        self.day += 1
        self.check_status()
    
    def hunt(self):
        food_gained = random.randint(20, 50)
        self.food += food_gained
        self.health -= random.randint(0, 5)
        self.day += 1
        self.check_status()
    
    def buy_supplies(self):
        if self.money >= 50:
            self.food += 100
            self.money -= 50
            print("You bought 100 pounds of food.")
        else:
            print("You don't have enough money to buy supplies.")
        self.check_status()
    
    def check_status(self):
        if self.food <= 0:
            self.health -= 10
            self.food = 0
        if self.health <= 0:
            self.status = "Dead"
        if self.distance_remaining <= 0:
            self.status = "Won"
    
    def display_status(self):
        print(f"Day: {self.day}")
        print(f"Distance Remaining: {self.distance_remaining} miles")
        print(f"Food: {self.food} pounds")
        print(f"Health: {self.health}")
        print(f"Money: ${self.money}")
        print(f"Status: {self.status}")

def main():
    game = Game()
    print("Welcome to the Oregon Trail Game!")

    while game.status == "Alive" and game.distance_remaining > 0:
        game.display_status()
        print("\nChoose an action:")
        print("1. Travel")
        print("2. Rest")
        print("3. Hunt")
        print("4. Buy Supplies")
        print("5. Quit")

        choice = input("> ")

        if choice == "1":
            game.travel()
        elif choice == "2":
            game.rest()
        elif choice == "3":
            game.hunt()
        elif choice == "4":
            game.buy_supplies()
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

        if game.status == "Dead":
            print("You have died. Game over.")
        elif game.status == "Won":
            print("Congratulations! You have reached Oregon.")

if __name__ == "__main__":
    main()

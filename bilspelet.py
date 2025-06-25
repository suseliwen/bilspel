import random

class Car():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0
    
    def drive(self):
        meters = random.randint(10, 30)
        self.position += meters 
        print(f"{self.name} körde {meters} meter! Totalt: {self.position} meter.")

def show_car_icon(car):
    icon = "🚗"
    space = " " *(car.position // 2)
    print(f"{car.name:10}: {space} {icon} ({car.position} m)")

garage = [
    Car('Volvo', 'blå'),
    Car('Ford', 'gul'),
    Car('Kia', 'svart'),
    Car('Polestar', 'brun'),
    Car('Jaguar', 'grön')
]

print('Välj en bil: ')
for i, car in enumerate(garage, start = 1):
    print(f"Bil {i}: {car.color} {car.name}")

choice = int(input('Skriv numret på den bil du vill tävla med: ')) -1
player_car = garage[choice]

print("")
print(f"Du tävlar med en {player_car.color} {player_car.name}. Lycka till!")
print("------------------------")

available_cars = [car for car in garage if car != player_car]

computer_car = random.choice(available_cars)

print(f"Datorn spelar med {computer_car.color} {computer_car.name}. ")
print("")

print("*****************")
print("Nu gasar vi! Först till 100 meter vinner.")

print("Klicka på tangenten [K] och sedan ENTER på ditt tangentbord för att köra iväg")
print("")

while True:

    key = input("\nKlicka på K för att köra: ").lower()

    if key == 'k':
        print("\n---Din tur---!")
        player_car.drive()

        if player_car.position >= 100:
            print(f"\nDu vann loppet med din {player_car.color} {player_car.name}!")
            break

        print("\n--- Datorns tur ---")
        computer_car.drive()
        
        if computer_car.position >= 100:
            print(f"\nDatorn vann med sin {computer_car.color} {computer_car.name}. Bättre lycka nästa gång!")
            break

        print("\nPositioner:")
        show_car_icon(player_car)
        show_car_icon(computer_car)
    else:
        print("Tryck på 'K' och ENTER för att köra.")


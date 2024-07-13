import os

class Car:
    def __init__(self, license_plate, brand, model):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model

def add_car(parking_lot):
    license_plate = input("Enter license plate: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    
    car = Car(license_plate, brand, model)
    parking_lot.append(car)
    save_to_file(parking_lot)
    print("Car parked successfully!")

def remove_car(parking_lot):
    license_plate = input("Enter the license plate of the car to be removed: ")
    
    for car in parking_lot:
        if car.license_plate == license_plate:
            parking_lot.remove(car)
            save_to_file(parking_lot)
            print("Car removed successfully!")
            return
    
    print("Car not found in the parking lot!")

def display_cars(parking_lot):
    if not parking_lot:
        print("No cars parked in the parking lot.")
    else:
        print("Cars parked in the parking lot:")
        for car in parking_lot:
            print(f"License Plate: {car.license_plate}, Brand: {car.brand}, Model: {car.model}")

def save_to_file(parking_lot):
    with open("parking_lot.txt", "w") as file:
        for car in parking_lot:
            file.write(f"{car.license_plate} {car.brand} {car.model}\n")

def load_from_file():
    parking_lot = []
    if os.path.exists("parking_lot.txt"):
        with open("parking_lot.txt", "r") as file:
            for line in file:
                data = line.strip().split()
                if len(data) == 3:
                    license_plate, brand, model = data
                    car = Car(license_plate, brand, model)
                    parking_lot.append(car)
    return parking_lot

def main():
    parking_lot = load_from_file()
    
    while True:
        print("\nCar Parking Management System")
        print("1. Park a car")
        print("2. Remove a car")
        print("3. Display parked cars")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                add_car(parking_lot)
            elif choice == 2:
                remove_car(parking_lot)
            elif choice == 3:
                display_cars(parking_lot)
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice! Please try again.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
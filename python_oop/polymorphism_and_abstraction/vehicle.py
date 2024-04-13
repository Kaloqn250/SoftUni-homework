from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        ...
    @abstractmethod
    def refuel(self, fuel: int) -> None:
        ...


class Car(Vehicle):

    def drive(self, distance: int) -> None:
        SUMMER_BONUS_CONSUMPTION = 0.9
        fuel_needed = distance * (self.fuel_consumption + SUMMER_BONUS_CONSUMPTION)

        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance: int) -> None:
        SUMMER_BONUS_CONSUMPTION = 1.6
        fuel_needed = distance * (self.fuel_consumption + SUMMER_BONUS_CONSUMPTION)

        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        TANK_CAPACITY = 0.95

        self.fuel_quantity += fuel * TANK_CAPACITY



car = Car(20, 5)

car.drive(3)

print(car.fuel_quantity)

car.refuel(10)

print(car.fuel_quantity)
truck = Truck(100, 15)

truck.drive(5)

print(truck.fuel_quantity)

truck.refuel(50)

print(truck.fuel_quantity)
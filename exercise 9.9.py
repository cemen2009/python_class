class Car:

    def __init__(self, make, model, year):
        self.brand = make
        self.model = model
        self.year = str(year)
        self.odometer = 0

    def car_describe(self):
        message = f'{self.year} {self.brand.title()} {self.model.title()}'
        return message

    def read_odometer(self):
        message = f'Odometer: {self.odometer} miles'
        return message

    def update_odometer(self, new_distance):
        if new_distance < int(self.odometer):
            print('You can\'t roll back an odometer!')
        else:
            self.odometer = new_distance

    def increment_odometer(self, increment):
        if increment >= 0:
            self.odometer += increment
        else:
            print('You can\'t add a negative number to odometer count!')


class Battery:

    def __init__(self, capacity):
        self.capacity = capacity
        self.default_capacity = 85

    def update_battery(self):
        if self.capacity == self.default_capacity:
            print(f"Capacity of battery is ok.\nCapacity: {str(self.capacity)}-kWh")
        else:
            print(f'Capacity of battery isn\'t ok.\nMust be 85-kWh battery, now {str(self.capacity)}-kWh.')
            self.capacity = self.default_capacity
            print(f'Now capacity of battery: {str(self.capacity)}-kWh')

    def get_range(self):
        if self.capacity == 70:
            range = 240
        elif self.capacity == 85:
            range = 270
        message = f'This car can go approximately {str(range)} miles on a full charge.'
        return message


class ElectricCar(Car):

    def __init__(self, model, year, make, capacity):
        super().__init__(model, year, make)
        self.capacity = capacity
        self.battery = Battery(self.capacity)


tesla = ElectricCar('s', 2018, 'tesla', 70)
print(tesla.battery.get_range())
tesla.battery.update_battery()
print()
print(tesla.battery.get_range())
tesla.battery.update_battery()

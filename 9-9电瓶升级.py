class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')
    def update_odometer(self, milege):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can"t roll back an odometer!')
    def increment_odometer(self, miles):
        self.odometer_reading+= miles
        
class Battery():
        def __init__(self, battery_size=70):
            self.battery_size = battery_size
        def get_kilometre(self):
            if self.battery_size == 70:
                kilometre = 240
            elif self.battery_size == 85:
                kilometre  = 270
            message = 'This car can go approximately ' + str(kilometre )
            message+= ' miles on a full charge.'
            print(message)
            self.upgrade_battery()
        def describe_battery(self):
            print('This car has a '+str(self.battery_size)+'-kWh battery.')
        def upgrade_battery(self):
            if self.battery_size != 85:
                self.battery_size = 85
            

        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_car = ElectricCar('tesla', 'model s', 2016)
my_car.battery.get_kilometre ()
my_car.battery.get_kilometre ()



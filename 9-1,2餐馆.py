#创建类
class Restaurant:
    def __init__(self,restaurnat_name,cuisine_type):
        self.name = restaurnat_name
        self.type = cuisine_type
    #创建两个方法
    def describe_restaurant(self):
        print(self.name.title() + ' - ' + self.type.title())
    def open_restaurant(self):
        print(self.name.title() + ' is opening.')
#创建三个实例        
restaurant1 = Restaurant('sun', 'japenese')
print("This restaurant's name is " + restaurant1.name.title() + ' which sells '
        + restaurant1.type.title() + ' food.')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('may', 'korean')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('rain', 'chinese')
restaurant3.describe_restaurant()

#创建类
class Restaurant:
    def __init__(self,restaurnat_name,cuisine_type):
        self.name = restaurnat_name
        self.type = cuisine_type
        self.number_served = 0
    #创建两个方法
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,guess_number):
        self.number_served += guess_number
#实例
restaurant4 = Restaurant('win', 'chinese')
print(restaurant4.number_served)
#调用函数并传递值
restaurant4.number_served = 15
print(restaurant4.number_served)
restaurant4.set_number_served(70)
print(restaurant4.number_served)
restaurant4.increment_number_served(4)
print(restaurant4.number_served)


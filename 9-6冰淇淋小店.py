#创建类
class Restaurant:
    def __init__(self,restaurnat_name,cuisine_type):
        self.name = restaurnat_name
        self.type = cuisine_type
        self.number_served = 0
#子类
class IceCreamStand(Restaurant):
    def __init__(self,restaurnat_name,cuisine_type):
        #初始化父类属性再初始化子类特有属性
         super().__init__(restaurnat_name,cuisine_type)
         self.flavors = 'apple'
    def show_flavors(self):
        print('The flavor of ' + self.name.title() +' is ' + self.flavors.title()) 
            
#实例
my_icecream = IceCreamStand('rain', 'ice cream')
my_icecream.show_flavors()

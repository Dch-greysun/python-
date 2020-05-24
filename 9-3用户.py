#创建类
class User():
    #初始化属性
    def __init__(self,first_name,last_name,age='',gender=''):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.gender = gender
    #创建两个方法
    def describe_user(self):
        print('\n' + self.f_name.title() + ' ' + self.l_name.title() + '\n- '
              + self.gender.title() + '\n- ' + str(self.age))
    def greet_user(self):
        print('Hello, ' + self.f_name.title() + '!')
        
#实例并调用方法
user1 = User('may','white',12,'female')
user1.describe_user()
user1.greet_user()

user2 = User('marry','ann','female')
user2.describe_user()
user2.greet_user()

user3 = User('eric','smith',60)
user3.describe_user()
user3.greet_user()
    

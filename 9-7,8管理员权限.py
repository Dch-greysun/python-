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
#另一个类及方法
class Privileges():
    def __init__(self,privileges_type=['can add post','can delete post','can ban user']):
        self.privileges_type = privileges_type
    def show_privileges(self):
        print(self.privileges_type)
#子类
class Admin(User):
    def __init__(self,first_name,last_name,age='',gender=''):
        super().__init__(self,first_name,last_name)
        self.admin_privileges = Privileges()
#实例
my_admin = Admin('karry','win')
my_admin.admin_privileges.show_privileges()
        
    

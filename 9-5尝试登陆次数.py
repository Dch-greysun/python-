#创建类
class User():
    #初始化属性
    def __init__(self,first_name,last_name,login_attempts,age='',gender='',):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts
    #创建两个方法
    def increment_login_attempts(self,number):
        self.login_attempts += number
    def reset_login_attempts(self):
        self.login_attempts = 0
        
#实例并调用方法
user1 = User('may','white',1,12,'female')
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.increment_login_attempts(1)
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)

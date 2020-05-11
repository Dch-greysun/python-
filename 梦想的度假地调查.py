responses = {}
#设置一个标志，指出调查是否继续
target = True
while target:
    #提示输入被调查者的名字和回答
    name = input('What''s your name？')
    place = input('If you could visit one place in the world, where would you go?')
    #将答案储存在字典里
    responses[name] = place
    #看看是否还有人要参与调查
    repeat = input('Would you like to let another person respond?(yes/no)')
    if repeat.lower() == 'no':
        target = False
#调查结束，显示结果
print('\n------Result------')
for name, place in responses.items():
    print(name.title() + ', would like to go to ' + place.title() + '.')

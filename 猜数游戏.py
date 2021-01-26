import random
history = {}

#游戏主体
def try_to_guess():
    selectnum = random.randint(0,1024)
    try_num = 0
    name = input('请输入用户名： ')
    #判断用户是否存在
    if name not in history.keys():
        history[name] = []
    while try_num < 10:
        guess_answer = int(input('请输入一个数字： '))
        if guess_answer < selectnum:
                print('你输入的数字比正确答案小。')
        elif guess_answer == selectnum:
                print('回答正确！')
                history[name].append('成功')
                break
        else:
                print('你输入的数字比正确答案大。')
        try_num += 1
    else:
        print('猜错次数太多，失败。')
        history[name].append('失败')
    return

#游戏菜单
def num_chooesd():
    print('1.历史记录 \n2.继续游戏 \n3.退出游戏')
    choosenum = str(input('请输入数字选择： '))
    
    if choosenum == '1':
        for n, s in history.items():
            print('用户： ' + n)
            print('记录如下： ' + str(s))
    elif choosenum == '3':
        print('游戏结束！')
        pass    
    else:  
        try_to_guess()

active = True
while active:
    num_chooesd()

        

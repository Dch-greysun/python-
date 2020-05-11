sandwich_orders = ['tunna', 'beef', 'pork','pastrami']
finished_sandwiches = []

#弹出缺货标语
promt = "We are out of pastrami."
print(promt)

#将缺少的材料从列表中去除
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    #打印制作的三明治
    sandwiches = sandwich_orders.pop()
    print("I made your " + sandwiches.title() + " sandwich.")
    #将已制作的三明治转到完成列表
    finished_sandwiches.append(sandwiches)
    
#打印所以已完成的三明治
print(finished_sandwiches)

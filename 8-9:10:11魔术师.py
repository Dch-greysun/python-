#打印列表中每个魔术师的名字
def show_magicians(unshowed_magicians):
    for magicians in unshowed_magicians:
        print(magicians.title())
#改变魔术师的头衔
def make_great(great_magician, showed_magician):
    print('\nThese are great magicians: ')
    while unshowded_magicians:
        current_magician = unshowded_magicians.pop()
        print('\nThe Great ' + current_magician.title())
        great_magician.append(current_magician)
#建立两个列表
unshowded_magicians = ['may','sunny','blue']
great_magician = []
#调用函数
show_magicians(unshowded_magicians)
make_great(unshowded_magicians[:],great_magician)

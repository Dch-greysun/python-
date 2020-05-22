#关于专辑的函数
def make_album(name, album, number = ''):
    if number:
        describe = name + ' ' + album + ' - ' + number
    else:
        describe = name + ' ' + album
    return describe.title()
#循环及输入
while True:
    print('\nPlease tell me your favorite album:')
    print("(enter 'q' at any time to quit)")
    s_name = input("Who is the singer?")
    if s_name == 'q':
        break
    albums = input("What's the album's name?")
    if albums == 'q':
        break
    #最喜欢的专辑结果输出
    print("\nYour favorite album is " + albums.title() + " from " + s_name.title() + '.')
#8-7函数调用
singers = make_album('Mary J. Blige', 'Real Love')
print(singers)
singers = make_album('Steven Tyler', 'Dream On')
print(singers)
singers = make_album('Stevie Nicks', 'In Your Dreams', '15')
print(singers)

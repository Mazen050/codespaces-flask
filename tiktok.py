def convert(list):
    
    list[0][0]=((int(list[0][0])/1000) * 220) #344
    list[1][0]=((int(list[1][0])/1000) * 220) #344

    list[0][1]=((int(list[0][1])/1000) * 340) #552
    list[1][1]=((int(list[1][1])/1000) * 340) #552

    list[0][2]=((int(list[0][2])/1000) * 220) #344
    list[1][2]=((int(list[1][2])/1000) * 220) #344

    list[0][3]=((int(list[0][3])/1000) * 340) #552
    list[1][3]=((int(list[1][3])/1000) * 340) #552
    return list

def centered(num):
    l = []
    for i in range(0,2):
        x = (((num[i][3]-num[i][1])/2)+num[i][1]) - 170
        y = (((num[i][2]-num[i][0])/2)+num[i][0]) - 110
        l.append([x,y])
    print(l)
    return l


def format_text(stringi):
    new = ''
    for i in stringi:
        if i.isnumeric():
            new+=i
        elif i == ',':
            new+=' '
        elif i == ']':
            new+='\n'
    ai_numbers = list(map(lambda x: x.split(' '),new.split('\n')))
    normal_numbers = centered(convert(ai_numbers))
    return normal_numbers

# print(format_text(''' - [726, 403, 886, 465]
# - [269, 146, 573, 256]''' ))
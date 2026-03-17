def asterisk_pyramid(rows):
    space = rows-1
    for i in range(rows):
        print(" "*space,'*'*(i+1))
        space-=1

asterisk_pyramid(5)
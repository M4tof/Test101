def magick(a):
    a=str(a)
    if len(a)<=2:
        return True
    else:
        flag_rising=0
        flag_droping=0
        for i in range(1,len(a)):
            if int(a[i-1])<int(a[i]):
                flag_rising=1
                if flag_rising==1 and flag_droping==1:
                    return False
            if int(a[i-1])>int(a[i]):
                flag_droping=1
    return True

print(magick(2321))
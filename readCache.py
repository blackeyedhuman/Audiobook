#read pg number
def readCache():
    f = open("/home/venkatesh/Documents/GitHub/audiobook/cache.txt", "r")
    if os.stat("/home/venkatesh/Documents/GitHub/audiobook/cache.txt").st_size == 0:
        to_return = 0
    else:
        to_return = f.read()
    f.close()
    return to_return

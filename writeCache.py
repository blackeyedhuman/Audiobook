
#write pg number
def writeCache(page):
    f = open("/home/venkatesh/Documents/GitHub/audiobook/cache.txt", "w")
    f.write(page)
    print("The bookmark has been cached!")
    f.close()
    return
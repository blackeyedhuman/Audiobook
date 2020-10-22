import os
from os import path
from glob import glob
import readCache
import writeCache

#main func
def main():
    print("Hi, are you starting a new book? Enter 1 for Yes or 2 for No")
    main_option = input()
    
    if main_option.isdigit() == 1:
        main_option = int(main_option)

    if main_option == 1:
        print("Also heads up, hope you placed the pdf folder in the same file.")
        print("\n\nLet's get started!")
        writeCache(0)
        startFrom = readCache()
    
    else:
        print("Let's get started!*")
        startFrom = readCache()

    audiobook(startFrom)

if __name__ == '__main__':
    main()
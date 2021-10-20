def countWord():
    fileName = input("Write the file name from which you want to count the words.")
    wc = 0
    file = open(fileName, 'r')
    for i in file:
        words = i.split()
        wc = wc + len(words)
    print("Number of words ", wc)

countWord()
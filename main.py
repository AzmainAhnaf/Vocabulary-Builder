
print("Welcome to Vocabulary Builder. Press enter to continue")
input()

while True:
    print('Press (s) to see your current list')
    print('press (c) to check if you desired is in your list or not')
    print('Press (a) to add new words')
    print('Press (d) to delete words')
    print('Press (q) to quit\n')

    response = input('--> ')
    # Printing whole vocubalary list
    if response == 's' or response == 'S':
        print("-------------------")
        f = open('vocabulary.txt', 'r')
        print(f.read())
        f.close()
        print("-------------------\n")

    elif response == 'q' or response == 'Q':
        break

    elif response == 'c' or response == 'C':
        pass

    # Adding word to the list
    elif response == 'a' or response == 'A':
        print("-------------------")
        rf = open("vocabulary.txt", 'r')
        contents = rf.read()
        wf = open("vocabulary.txt", 'w')
        print('\n')
        word = input('Enter the word you want to add --> ')
        wf.write(contents + word + '\n')
        rf.close()
        wf.close()
        print("-------------------\n")

    elif response == 'd' or response == 'D':
        pass
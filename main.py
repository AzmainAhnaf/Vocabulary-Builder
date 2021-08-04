
print("Welcome to Vocabulary Builder. Press enter to continue")
input()

while True:
    # Fuction available to user
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

    # Qutting the application
    elif response == 'q' or response == 'Q':
        break

    # Checks if a word is available on your list or not
    elif response == 'c' or response == 'C':
        print("-------------------")
        
        # Reading contents from files for later use
        rf = open('vocabulary.txt', 'r')
        contents = rf.readlines()
        rf.close()

        word = input("Enter the word you want to search --> ")
        word = word.strip()
        
        # Checking input and comparing with list
        for line in contents:
            if line.strip() == word:
                print("Founded --> ", word)
            elif line == contents[-1]:
                print('Not founded --> ', word)
        print("-------------------\n")

    # Adding word to the list
    elif response == 'a' or response == 'A':
        print("-------------------")
        
        # Reading contents from files for later use
        rf = open("vocabulary.txt", 'r')
        contents = rf.read()
        rf.close()

        wf = open("vocabulary.txt", 'w')
        print('\n')
        word = input('Enter the word you want to add --> ')
        
        # Adding the word
        wf.write(contents + word + '\n')
        wf.close()
        print("-------------------\n")

    # Deliting word from the list
    elif response == 'd' or response == 'D':
        print("-------------------")
        
        # Reading contents from files for later use
        rf = open('vocabulary.txt', 'r')
        contents = rf.readlines()
        rf.close()
        
        wf = open('vocabulary.txt', 'w')
        word = input("Enter the word you want to delete --> ")
        word = word.strip()
        
        # Deleting the word that user inputted
        for line in contents:
            if line.strip() != word:
                wf.write(line[:-1] + "\n")
        wf.close()
        print("-------------------\n")
    
    # Sorting list
    f = open('vocabulary.txt', 'r')
    contents = f.readlines()
    f.close()
    f = open('vocabulary.txt', 'w')
    contents.sort()
    for line in contents:
        f.write(line[:-1] + '\n')
    f.close()

    input("Press enter")
    print('\n')

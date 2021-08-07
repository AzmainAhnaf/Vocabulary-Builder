from PyDictionary import PyDictionary
dictionary = PyDictionary()

# Reusing some code for both the 'c' and the 'l' keyword
def checkword(word, contents):
    for line in contents:
        if line.strip() == word:
            return word
        elif line == contents[-1]:
            return False

print("Welcome to Vocabulary Builder. Press enter to continue")
input()

while True:
    # Fuction available to user
    print('Press (s) to see your current list')
    print('Press (c) to check if you desired is in your list or not')
    print('Press (l) to learn about a word\'s meaning and other stuff')
    print('Press (a) to add new words')
    print('Press (d) to delete words')
    print('Press (q) to quit\n')

    response = input('--> ')
    
    # Printing whole vocubalary list
    if response.strip().lower() == 's':
        print("-------------------")
        f = open('vocabulary.txt', 'r')
        print(f.read())
        f.close()
        print("-------------------\n")

    # Qutting the application
    elif response.strip().lower() == 'q':
        break

    # Checks if a word is available on your list or not
    elif response.strip().lower() == 'c':
        print("-------------------")
        
        # Reading contents from files for later use
        rf = open('vocabulary.txt', 'r')
        contents = rf.readlines()
        rf.close()

        word = input("Enter the word you want to search --> ").title()
        word = word.strip()
        
        # Checking input and comparing with list
        checkedword = checkword(word, contents)
        if checkedword:
            print(f'Found {word}')
        else:
            print(f'Not found {word}')
        
        print("-------------------\n")

    # Learning about a word
    elif response.strip().lower() == 'l':
        print("-------------------")

        # Reading contents from files for later use
        rf = open('vocabulary.txt', 'r')
        contents = rf.readlines()
        rf.close()

        word = input("Enter the word you want to learn about --> ").title()
        word = word.strip()
        
        # Checking input and comparing with list
        checkedword = checkword(word, contents)
        if checkedword:
            worddict = dictionary.meaning(word)
            for key in worddict:
                for meaning in worddict[key]:
                    print(f'{word} ({key}) --> {meaning}')
            
            synonyms = str(dictionary.synonym(word)).replace('[', '').replace(']', '')
            antonyms = str(dictionary.antonym(word)).replace('[', '').replace(']', '')
            print(f'\nSynonyms: {synonyms}')
            print(f'Antonyms: {antonyms}')

        else:
            print(f'Not found {word}')

        print("-------------------\n")

    # Adding word to the list
    elif response.strip().lower() == 'a':
        print("-------------------")
        
        # Reading contents from files for later use
        rf = open("vocabulary.txt", 'r')
        contents = rf.read()
        rf.close()

        wf = open("vocabulary.txt", 'w')
        print('\n')
        word = input('Enter the word you want to add --> ').title()
        
        # Adding the word
        wf.write(contents + word + '\n')
        wf.close()
        print("-------------------\n")

    # Deliting word from the list
    elif response.strip().lower() == 'd':
        print("-------------------")
        
        # Reading contents from files for later use
        rf = open('vocabulary.txt', 'r')
        contents = rf.readlines()
        rf.close()
        
        wf = open('vocabulary.txt', 'w')
        word = input("Enter the word you want to delete --> ").title()
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

    # removing duplicates
    contents = list(set(contents))
    
    for line in contents:
        f.write(line[:-1] + '\n')
    f.close()

    input("Press enter")
    print('\n')

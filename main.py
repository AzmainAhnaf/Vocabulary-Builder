with open('vocabulary.txt', 'r') as rf:
    with open('vocabulary.txt', 'w') as wf:
        print("Welcome to Vocabulary Builder. Press enter to continue")
        input()

        while True:
            rf_contents = rf.read()
            print('Press (s) to see your current list')
            print('press (c) to check if you desired is in your list or not')
            print('Press (a) to add new words')
            print('Press (d) to delete words')
            print('Press (q) to quit\n')

            response = input('--> ')
            # Printing whole list
            if response == 's' or response == 'S':
                for line in rf_contents:
                    print(line)
                print('\n')
            
            # Quitting from the application loop
            elif response == 'q' or response == "Q":
                break
            
            # Adding new words
            elif response == 'a' or response == 'A':
                for line in rf_contents:
                    wf.write('\n' + line)
                word = input("Please enter your new word --> ")
                wf.write('\n' + word)
                print('\n')

            # Deleting words
            elif response == 'd' or response == 'D':
               word = input("Please enter the word that you want to delete --> ")
               for line in rf_contents:
                   if line != word:
                       wf.write(line)

            rf.seek(0)
            


with open('vocabulary.txt', 'r') as rf:
    with open('vocabulary.txt', 'a') as wf:
        print("Welcome to Vocabulary Builder. Press enter to continue")
        input()

        while True:
            print('Press (s) to see your current list')
            print('press (c) to check if you desired is in your list or not')
            print('Press (a) to add new words')
            print('Press (d) to delete words')
            print('Press (q) to quit\n')

            response = input('--> ')
            if response == 's' or response == 'S':
                for line in rf:
                    print(line, end = "")
                print("\n\n")
            elif response == 'q' or response == "Q":
                break
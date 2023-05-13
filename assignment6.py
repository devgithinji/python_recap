running = True
while running:
    print('Please choose')
    print('1: Add Input')
    print('2: Output data')
    print('q: Quit')
    user_input = input('Your choice: ')
    if user_input == '1':
        data_to_store = input('Your text: ')
        with open('assignment.txt', mode='a') as f:
            f.write(data_to_store)
            f.write("\n")
    elif user_input == '2':
        with open('assignment.txt', mode='r') as f:
            file_content = f.readlines()
            for line in file_content:
                print(line)
    elif user_input == 'q':
        running = False




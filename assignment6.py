import json

running = True
user_input_list = []
while running:
    print('Please choose')
    print('1: Add Input')
    print('2: Output data')
    print('q: Quit')
    user_input = input('Your choice: ')
    if user_input == '1':
        data_to_store = input('Your text: ')
        user_input_list.append(data_to_store)
        with open('assignment.txt', mode='w') as f:
            f.write(json.dumps(user_input_list))
            f.write("\n")
    elif user_input == '2':
        with open('assignment.txt', mode='r') as f:
            file_content =json.loads(f.read())
            for line in file_content:
                print(line)
    elif user_input == 'q':
        running = False

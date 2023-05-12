import copy

print("Task one")

people = [
    {
        'name': 'dennis',
        'age': 23,
        'hobbies': ['dancing', 'reading', 'music']
    },
    {
        'name': 'paul',
        'age': 37,
        'hobbies': ['guitar', 'cycling', 'piano']
    },
    {
        'name': 'sarah',
        'age': 21,
        'hobbies': ['sleeping', 'cooking', 'singing']
    }
]

print(people)

print('-' * 20)

print("Task two")

person_names = [el['name'] for el in people]

print(person_names)

print('-' * 20)

print("Task three")

age_bools = all([el['age'] > 20 for el in people])

print(age_bools)

print('-' * 20)

print("Task four")

copied_persons = copy.deepcopy(people)

print(copied_persons)

copied_persons[0]['name'] = 'githinji'

print(copied_persons)

print(people)

print('-' * 20)

print("Task five")

person_one, person_two, person_three = people

print(person_one)
print(person_two)
print(person_three)

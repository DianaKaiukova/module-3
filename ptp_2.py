cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')


if city.capitalize() == tourists[0]['city']:
    print(f"Турист {tourists[0]['user']['name']} возвраст {tourists[0]['user']['age']}. Посетил город {tourists[0]['city']}")

elif city.capitalize() == tourists[1]['city']:
    print(f"Турист {tourists[1]['user']['name']} возвраст {tourists[1]['user']['age']}. Посетил город {tourists[1]['city']}")

elif city.capitalize() == tourists[2]['city']:
    print(f"Турист {tourists[2]['user']['name']} возвраст {tourists[2]['user']['age']}. Посетил город {tourists[2]['city']}")
    
else:
    print('Ни один из туристов не посещал введённый город. Эх.... Как жаль')
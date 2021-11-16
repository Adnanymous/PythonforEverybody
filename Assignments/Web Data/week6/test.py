data = {'note': 'This file contains the sample data for testing',
        'comments': [{'name': 'Romina', 'count': 97},
              {'name': 'Laurie', 'count': 97},
              {'name': 'Bayli', 'count': 90},
              {'name': 'Siyona', 'count': 90},
              {'name': 'Atiya', 'count': 18},
              {'name': 'Rohan', 'count': 18},
              {'name': 'Nuala', 'count': 14},
              {'name': 'Maram', 'count': 12},
              {'name': 'Carlo', 'count': 12},
              {'name': 'Japleen', 'count': 9},
              {'name': 'Breeanna', 'count': 7},
              {'name': 'Zaaine', 'count': 3},
              {'name': 'Inika', 'count': 2}
             ]
}
sum = 0

for item in data['comments']:
    count = int(item['count'])
    sum = count + sum
print(sum)

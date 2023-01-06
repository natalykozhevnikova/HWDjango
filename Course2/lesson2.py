#friend = 'Max'
#print(friend)
#print(type(friend))

#friend = "Max"
#print(friend)

#say ="say'Hello'"
#print(say)

#friend = 'Max'
#first_letter = friend[0]
#print('first letter name of friend', first_letter)
#print(friend[1])

#friend = 'Max'
#first_letter = friend[0:3]
#print('first letter name of friend', first_letter)
#print(friend[0:2])


#friends = 'Максим;Леонид '
#print(friends)
#print(len(friends))
#print(friends.find('Лео'))
#print(friends.split())
#print(friends.split(';'))
#print(friends.isdigit())

#number = '123'
#print(number.isdigit())

#print(friends.upper())
#print(friends.lower())

#name = 'Leo'
#age = 30
#hello_str = 'Hi',  + name + 'you' + str(age) + 'years'
#print(hello_str)
#hello_str = 'Hi  {} you {} age'.format(name, age)
#print(hello_str)

#top5 = 'Первые 5 мест на соревнованиях:1. иванов 2. петров 3. сидоров. 4. орлов. 5. соколов'
#start = top5.find('1')
#end = top5.find('4')
#top3 = top5[start: end]
#result = 'Поздравляем {} с успехом'.format(top3.upper())
#print(result)

#empty_list = []
#friends = ['Max', 'Leo', 'Kate']
#print(type(friends))
#print('Secand friend: ', friends[1])
#print('First friend with end', friends[-1])
#print(friends[1:2])
#print(friends[:2])
#print(friends[1:])

#friends = ['Max', 'Leo', 'Kate']
#print(len(friends))
#friends.append('ron')
#print(friends)
#print(len(friends))

#print(friends.pop())
#print(friends)
#friends.clear()
#print(friends)

#friends = ['Max', 'Leo', 'Kate']
#friends.remove('Kate')
#print(friends)

#del_friends[0]
#print(friends)


#hero = 'Superman'
#hero = 'Super'
#if hero.find('man') != -1:
#    print('Has')

#if 'man' in hero:
#    print('Has')

#goals = ['стать гуру питон', 'здоровье', 'покормить кота']
#if 'здоровье' in goals:
#    print('все хорошо')

#print('соревнование по пайтон')
#count = int(input('Введите количество участников: '))
#i = count
#while i > 0:
#    name = input('Кто занял {} место '. format(i))
#    members.append(name)
#    i -=1
#print('В соревнованиях участвовали:', members)
#members.reverse()
#result = members[0:3]
#result = 'Победители: (). Поздравляем!'.format(re)
#print(result)

#friend_name = 'Max'
#friends = ('Max', 'Leo', 'Kate')
#roles = ('admin', 'guest', 'user')
#if 'Max' in friends:
#    print('I have this friend')
#if 'M' in friend_name:
#    print('Bukva M has in name of friend')

#i = 0
#while i < len(friends):
#    friend = friends[i]
#    print(friend)
#    i += 1

#for friend in friends:
#    print(friend)

#for letter in friend_name:
#    print(letter)
#for role in  roles:
#    print(role)
#print('end')



#winners = ['Max', 'Leo', 'Kate']

#for winner in winners:
#    print(winner)

#numbers = [1, 3, 5]

#for number in numbers:
#    print(number)

#numbers = range(10)
#print(numbers)
#print(type(numbers))
#print(list(numbers))

#numbers = range(66)
#print(list(numbers))

#winners = ['Max', 'Leo', 'Kate']

#for winner in winners:
#    print(winner)

#for i in range(len(winners)):
    #print(i)
    #print(winners[i])
#    print(i+1, ')', winners[i])

#numbers = [1, 3, 5]

#for number in numbers:
#    print(number)

#print(list(range(1, 1000, 2)))

#for number in range(1, 1000,2):
#    print(number)


#friends = ['Max', 'Leo', 'Kate']
#print(friends)
#print(type(friends))
#friend = friends[0]
#print(friends)
#print(type(friend))

#friend = {
#    'name':'Max',
#    'age': 23
#}

#print(friend)
#print(type(friend))


#friend = {
#    'name':'Max',
#    'age': 23
#}

#print(friend)
#print(type(friend))

#print(friend['age'])

#friend['has_car'] = True

#print(friend)

#friend['has_car'] = False

#print(friend)

#del friend['age']
#print(friend)

#if 'age' in friend:
#    print('Has age')

#if 'has_car' in friend:
#    print('Has a car')

#for key in friend.keys():
#    print(key)

#for key in friend:
#    print(key)
#    print(friend[key])

#for val in friend.values():
#    print(val)

#for item in friend.items():
#    print(item)

#for key, val in friend.items():
#    print(key)
#    print(val)


#cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', ' Moscow']

#print(type(cities))
#print(cities)

#cities = set(cities)
#print(cities)


#cities = {'Las Vegas', 'Paris', 'Moscow'}
#print(cities)
#cities.add('Burma')
#print(cities)
#cities.add('Moscow')
#print(cities)
#cities.remove('Moscow')
#print(cities)

#print(len(cities))

#print('Paris' in cities)

#for city in cities:
#    print(city)

max_things = {'Phone', 'Britva', 'Rubashka', 'Shorty'}
kate_things = {'Phone', 'Shorty', 'Zontik', 'Lipctick'}
print(max_things | kate_things)

print(max_things & kate_things)

print(max_things - kate_things)

print(kate_things - max_things)
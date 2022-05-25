# loops
print('#' * 10 + ' while loop ' + '#' * 10)
number = 0
while number <= 10:
    print(number)
    number += 3
print('Finish')

hour = 0
while hour <= 23:
    hour += 1
    if hour == 13:
        print('Time to lunch')
        continue  # this will make infinite loop
    print('Running code at the ', hour)

names = ['Adel', 'Aldo', 'Cruz', 'Giorgio']
print(len(names))
index = 0
while index < len(names):
    name = names[index]
    print(index, name)
    index += 1

index = 0
while index < len(names):
    name = names[index]
    print(name)
    if name == 'Giorgio':
        print(name, 'I found you!')
        break
    index += 1

basket = [{'fruit': 'apple', 'qty': 20}, {'fruit': 'banana', 'qty': 10}]
fruit = input('Enter a fruit:')
index = 0
found_it = False

while index < len(basket):
    item = basket[index]
    if item['fruit'] == fruit:
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        found_it = True
        break  # else is not execute
    index += 1
else:  # it is the same as: "if not found_it:"
    qty = int(input(f'Enter the qty for {fruit}:'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)

print('#' * 10 + ' for loop ' + '#' * 10)
ids = []
for name in names:
    ids.append(hash(name))

for index in range(20, 24+1):
    print(index)

for i in range(len(names)):
    print(names[i], ids[i])

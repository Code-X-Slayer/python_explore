nums = [1, 2, 3, 4, 5]

for num in nums:
    if num==4:
        break
    elif num%2 == 0:
        continue
    else:
        print(num)

for num in nums:
    for letter in 'ab':
        print(letter, num)

for i in range(3):
    print(i)

for i in range(0, 3):
    print(i)

for i in range(0, 3, 1):
    print(i)

x = 1
while x < 20:
    print(x)
    x *= 2

x = 1
while True:
    if x==5:
        break
    print(x)
    x+=1
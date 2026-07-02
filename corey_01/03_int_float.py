# int has no decimal
# float has decimal values

num1 = 2
num2 = 2.0

print(type(num1))
print(type(num2))

# arithmetic op
# + - * / // ** %
print(3+2)
print(type(3+2))
print(3-2)
print(type(3-2))
print(3*2)
print(type(3*2))
print(3/2)
print(type(3/2))
# this is only float since no upcast bw op bw int except div
print(3//2)
print(type(3//2))
print(3**2)
print(type(3**2))
print(3%2)
print(type(3%2))

# precedence
print(3*2+1)
print(3*(2+1))

# shorthand
num1 = num1 + 1
num2 += 1

# methods
print(abs(-1))

print(round(3.75)) # 4
print(round(3.25)) # 3

# if half way round to nearest even
print(round(3.5)) # 4
print(round(2.5)) # 2

# same rule goes for precision too
print(round(2.5, 0)) # 2
print(round(3.5, 0)) # 4
print(round(2.25, 1)) # 2.2
print(round(2.35, 1)) # 2.4

# ndigits can also be negative
print(round(1234, -1)) # 1230
print(round(1234, -2)) # 1200
print(round(1234, -3)) # 1000
print(round(1234, -4)) # 0000

# comparision
# < <= > >= == !=
# boolean output True of False

num_1 = '10'
num_2 = '20'
print(num_1+num_2) 
# its str concatentaion

# cast
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
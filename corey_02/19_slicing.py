# lists

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(my_list[-10])
print(my_list[0])

# list[start:end:step]
print(my_list[0:6:1])
print(my_list[-10:-4:1])
print(my_list[3:8:1])
print(my_list[-7:-2:1])
print(my_list[1:-2:1])
print(my_list[1:])
print(my_list[:-2])
print(my_list[:])
print(my_list[2:-1:2])
print(my_list[2:-1:-2])
print(my_list[8:1:-2])
print(my_list[-2:1:-2])
print(my_list[8:-9:-2])
print(my_list[-2:-9:-2])
print(my_list[::-1])

# str
sample_url = 'http://coreyms.com'

print(sample_url)
print(sample_url[::-1])
print(sample_url[-4:])
print(sample_url[7:])
print(sample_url[7:-4])
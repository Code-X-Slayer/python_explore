# == -> equality if values are equal
# is -> identity checks for memory

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1==l2)

# True
# as == checks values both lists are same

print(l1 is l2)

# False
# as == just checks equality
# is checks are they belong to same mem address
# since they weren't it returns false

l2 = l1
print(l1 is l2)

# True
# as now l2 l1 mapping to same list
# now is checks that both pointing to same mem address it ret True

# to test it further changing one also affects other
l1[0] = 100
print(l1)
print(l2)

# [100, 2, 3]
# [100, 2, 3]

# we can check it ourselves
print(id(l1))
print(id(l2))
print(id(l1) == id(l2))

# 2067035873472
# 2067035873472
# True
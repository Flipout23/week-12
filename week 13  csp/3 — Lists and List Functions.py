# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lists are part of the collections family in python
#creating a list
my_list = [1,2,3,4,5]
print(my_list)
print(len(my_list))
print(type(my_list)) #tells you the type of list
print(my_list[0]) #1
print(my_list[1:4]) # [2,3,4]
print(my_list[1:])# 2 3 4 5
print(my_list[:-1])# 1 2 3 4
#reverse the list
print(my_list[::-1])#reversed
#modifying a list
my_list.append(6) #adds 6 to the end of the list
print(my_list)# 1,2,3,4,5,6
# add 7 and 8 to the list
my_list.extend([7,8])
print(my_list)# 1 2 3 4 5 6 7 8
#remove the last item
my_list.pop()
print(my_list)# 1-7
# remove the item in index 2
my_list.pop(2)
print(my_list)
#sort in ascending order
my_list.sort()
print(my_list)
#reverse the list
my_list.reverse()
print(my_list)
#remove a single value (4)
my_list.remove(4)
print(my_list)
#remove the last item using negative index
#my_list.remove(-1)
print(my_list)
#add 50 more to the end
new_list = list(range(12,120))
print(new_list)
my_list.append(new_list)
print(my_list)
#my_list.extend(new_list)
#print(my_list)
#print every 3rd number
print(my_list[ : : 3])
#remove every third element
# every_third_element = new_list[2::3]
# print(every_third_element)
#or
del my_list[::3]
print(len(my_list))
print(my_list)

#why is a list more useful than a variable?
# a ;list can hold multiple values
#while a variable can only hold one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
#access the first item
print(cakes[0])#chocolate
#access the last item
print(cakes[-1])#carrot
#want to chocolate cake instead of vanilla
cakes[0]= 'strawberry'
print(cakes)
cakes[1] = 'chocolate'
print(cakes)
# remove the last cake
cakes.pop()
print(cakes)
#insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes)
# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
fruit_list = ['orange','pineapple','apple','banana','blueberries']

# Print the second and last item.
print(fruit_list[1])
print(fruit_list[-1])
# Add a new item using .append().
fruit_list.append('cherry')
print(fruit_list)
# Remove the first item using .pop(0).
fruit_list.pop(0)
print(fruit_list)
# Reverse your list using .reverse().
fruit_list.reverse()
print(fruit_list)

#sets = {1,2,3}
#sets are unordered collections of unique items
#sets do not support slicing or indexing
#sets are mutable meaning you can add or remove items
#sets are created using curly brackets
#sets dont allow duplacite items
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
#add one item to the list
my_set.add(6)
print(my_set)
#remove an item from the set
my_set.remove(3)
print(my_set)
#check if an item is in the set
print(4 in my_set)
print(3 in my_set)

#tuples are ordered collections of lists
# tuples are immutable meaning you cannot modify them after creation
# tuples are created using parenthesis
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
#trying to modify the tuple will result in an error.
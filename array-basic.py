

#sampriti banerjee--ece--41--j.

# Python program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#Q1 Testcase2

def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [1, 2, 3]

print(swapList(newList))
#Q2 Test case 1
# Python program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))

#Q2 Test case 1
# Python program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos2, pos5):
    list[pos2], list[pos5] = list[pos5], list[pos2]
    return list

#Q2 Teset case 2
# Driver function
List = [1, 2, 3, 4, 5]
pos2, pos5 = 1, 3

print(swapPositions(List, pos1 - 2, pos2 - 5))
#Q3 Test 1
from collections import Counter

# declaring the list
l = [15, 6, 7, 10, 12, 20, 10, 28, 10]

# driver program
x = 10
d = Counter(l)
print('{} appeares {} times in the given array'.format(x, d[x]))


#Q3 Test case 2
from collections import Counter

# declaring the list
l = [8, 6, 8, 10, 8, 20, 10, 8, 8]

# driver program
x = 16
d = Counter(l)
print('{} appeares {} times in the given array'.format(x, d[x]))

#Q4 Test Case1
# Python3 code to calculate
# average of array elements

# Function that return
# average of an array.
def average(a, n):
    # Find sum of array element
    sum = 0
    for i in range(n):
        sum += a[i]

    print("The sum of the number is ", sum)
    return sum / n;


# Driver code
arr = [4, 5, 1, 2, 9, 7, 10, 8]
n = len(arr)
print(average(arr, n))
#Q4Test case 2
# Python3 code to calculate
# average of array elements

# Function that return
# average of an array.
def average(a, n):
    # Find sum of array element
    sum = 0
    for i in range(n):
        sum += a[i]
    print("The sum of the number is ", sum)
    return sum / n;


# Driver code
arr = [15, 9, 55, 41, 35, 20, 62, 49]
n = len(arr)
print(average(arr, n))

#Q5testcase1
# Python program to multiply all values in the
# list using traversal

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list = [1, 2, 3]
print(multiplyList(list))

#Q5 test 2
# Python program to multiply all values in the
# list using traversal

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list = [3, 2, 4]
print(multiplyList(list))

#Q6Testcase1
# Python program to print Even Numbers in a List

# list of numbers
list1 = [2, 7, 5, 64, 14]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")


#Q6Testcase2
# Python program to print Even Numbers in a List

# list of numbers
print("  ")
list2 = [12, 14, 95, 3]

# iterating each number in list
for num1 in list2:

    # checking condition
    if num1 % 2 == 0:
        print(num1, end=" ")

#Q7 test case 1
# Python program to print odd Numbers in a List

# list of numbers
print("  ")
list1 = [2, 7, 5, 64, 14]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 != 0:
        print(num, end=" ")

#Q7testcase2
# Python program to print odd Numbers in a List

# list of numbers
print("  ")
list1 = [12, 14, 95, 3, 73]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 != 0:
        print(num, end=" ")




#Q8testcase1
# Python program to count Even
# and Odd numbers in a List

# list of numbers
print(" ")
list1 = [2, 7, 5, 64, 14]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


#Q8testcase2
# Python program to count Even
# and Odd numbers in a List

# list of numbers
list1 = [12, 14, 95, 3]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


#Q9Testcase1
# Python program to print positive Numbers in a List

# list of numbers
print(" ")
list1 = [12, -7, 5, 64, -14]

# iterating each number in list
for num in list1:

    # checking condition
    if num >= 0:
        print(num, end=" ")


#Q9Testcase2
# Python program to print positive Numbers in a List

# list of numbers
print("  ")
list2 = [12, 14, -95, 3]

# iterating each number in list
for num in list2:

    # checking condition
    if num >= 0:
        print(num, end=" ")

#Q10Testcase1
# Python program to print negative Numbers in a List

# list of numbers
print(" ")
list1 = [12, -7, 5, 64, -14]

# iterating each number in list
for num in list1:

    # checking condition
    if num < 0:
        print(num, end=" ")

#Q10Testcase2
# Python program to print negative Numbers in a List

# list of numbers
print("  ")
list1 = [12, 14, -95, 3]

# iterating each number in list
for num in list1:

    # checking condition
    if num < 0:
        print(num, end=" ")




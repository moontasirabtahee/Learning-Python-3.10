# Created by Moontasir Abtahee at 1/14/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count("banana"))
print(fruits.index("banana"))
print(fruits.index("banana",4))
print(fruits.sort())
squares = [x**2 for x in range(10)]
print(squares)
squares = list(map(lambda x: x**2, range(10)))
print(squares)

vec = [[1,2,3], [4,5,6], [7,8,9]]
print(list(zip(*vec)))
print([[row[i] for row in vec] for i in range(3)])
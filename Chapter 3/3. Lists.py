# Created by Moontasir Abtahee at 1/13/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
lists = [1,2,3,4,5,6,7,8,9,10]
print(lists)
print(lists[2:3])

p= lists[2:6]
lists[2:4] = []
print(lists)

x = lists + p
print(x)
x.append("Abtahee")
x.append([974,44,65,3/2])
print(x)
print(len(x))
# Created by Moontasir Abtahee at 1/14/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[-1]
print(a)
del a[2:4]
print(a)

del a[:]
print(a)
# Created by Moontasir Abtahee at 1/18/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:3d}; Sjoerd: {Sjoerd:3d}; Dcab: {Dcab:3d}'.format(**table))


for x in range(1, 11):
    print('{0:2d} {1:4d} {2:6d}'.format(x, x*x, x*x*x))
# Created by Moontasir Abtahee at 1/13/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
dann = True
for i in range(10000):
    for j in range(2,i):
        if i % j == 0:
            print(f"{i} is not a prime number {i} = {j} * {i/j}")
            break
    else:
        if dann == False:
            dann = True
            print(f"{i} is a prime Number YES!")
            continue
        print(f"{i} is a prime Number NO!")




# Created by Moontasir Abtahee at 1/14/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here


def standard(x):
    print(x)

def pos_only(x,/):
    print("positional only")

def keywordOnly(*,x):
    print(x)

def combined(x,/,y,*,z):
    print(x,y,z)


standard(2)
pos_only(33)
keywordOnly(x = 5)
combined(2,y = 44,z=8)


def arbitaryFuntion(*args,sep):
    return sep.join(args)


x = arbitaryFuntion("Abtahee","None","Moontasir","Aman",sep="*****")
print(x)
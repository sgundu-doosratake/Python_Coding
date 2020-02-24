#Modular changes to variables when passing as arguments

def update(lst):

    print("Id of list before :",id(lst))

    lst[1] = 25
    print("Id of list after :",id(lst))
    print("x",lst)

lst = [10,20,30]
print("Id of list is",id(lst))
update(lst)
print("List is",lst)

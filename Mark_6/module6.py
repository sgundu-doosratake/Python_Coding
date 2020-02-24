#Types of Arguments

#Formal Arguments
def person(name,age=18):
    print("Name of person is :",name)
    print("Age is :",age)

#Actual Arguments
person('sam',24)

#keyword arguments
person(age=24,name='sam')

#if all values are not passed,default values are taken 
person('sam')



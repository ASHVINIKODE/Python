#define a function

def myfunction():
 print("Hello from a function")
myfunction()

#passing an argument

def myfunc(fname):
    print("Hello from a function "+ fname)
myfunc("Ashvini")

#passing an argument again

def myfunct(fname,lastname):
    print("Hello from a function " +fname +lastname)
myfunct("Ashvini"," Bhagat")

# passing a list as an argument of a function

def my_func(food):
    for x in food:
        print(x)
fruits=["Apple","Banana","Cheery","Mango","Pineapple","Litchi","Grapes","Strawberry","Watermelon"]
my_func(fruits)

#return statement
def my_funct(food):
    count=0
    for x in food:
        count=count+1
        print(x)
    return count
fruits=["Apple","Banana","Cheery","Mango","Pineapple","Litchi","Grapes","Strawberry","Watermelon",1,2,3]
r=my_funct(fruits)
print(r)
 
#list of positive and negative number

list=[6,7,4,8,3,2,-1,-3,-8,-9]
positive_number=0
negative_number=0
for i in list:
    if(i>=0):
        positive_number=positive_number+1
    else:
        negative_number=negative_number+1
print("Positive numbers are:",positive_number)         
print("Positive numbers are:",negative_number)   

#index
list=[5,6,3,4,67,9,1,7,32]
n=int(input("Enter the number to be searched:"))
print("Index of the given number is:",list.index(n))

#unique number
def unique(nums):
    unique_list = []
    for i in nums:
        if i not in unique_list:  
            unique_list.append(i)
    return unique_list 
nums = [1, 2, 3, 4, 5, 6, 4, 2, 4, 4, 2, 4, 6, 8, 9, 0, 6, 3, 1, 4]
print("Unique numbers are:", unique(nums))


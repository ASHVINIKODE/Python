#smallest number in a list
num=[1,2,3,4,5,6,7,8,9,11,21,54,321,76,23,12]
print("smallest number:",min(num))

#largest number in a list
num1=[23,43,54,234,654,213,878]
print("largest number:",max(num1))

#Sum and Average of a list
num2=[23,54,12,65,213,67]
total=sum(num2)
average=total/len(num2)
print("sum:",total)
print("Average:",average)

#Multiply all numbers in a list
num3=[76,78,2,43,454,70]
result=1
for i in num:
    result*=i
print("product:",result)

#count even and odd number in a list:
num4=[23,45,11,332,76,987,34,21,98]
even=0
odd=0
for j in num4:
    if j%2==0:
        even+=1
    else:
        odd+=1
print("Even count:",even)
print("Odd count:",odd)
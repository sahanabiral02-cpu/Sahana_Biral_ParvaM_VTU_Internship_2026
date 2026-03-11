operand1=50
operand2=30

# arithematic operations:+,-,*,/,%
 
sum=operand1+operand2
difference=operand1-operand2
product=operand1*operand2
quotient=operand1/operand2
floor_division=operand1//operand2
# floor division will 
remainder=operand1%operand2
square=operand1**2

print("sum:",sum,"difference:",difference,"product:",product,"quotient:",quotient,"remainder:",remainder,"square of the number:",square)

# assignment operators:=,+=,-=,*=,/=,%=,**=,//=
number=20
print("original number:",number)
number+=5
print("5 is added to the number", number)
number-=5
print("5 is subtracted from the number", number)
number*=5
print("5 is multipled with the number", number)
number/=5
print("5 is divided by the number", number)
# number has been converted to float ,so new number has been taken
number1=23
number1//=5
print("23 is  divided by 5 using floor division", number1)
new_number=3
new_number**=5
print("number is updated with power of 5:",new_number)







# comparison operators:>,<,>=,<=,==,!=

n1=25
n2=35
print("number1 is greater then number 2:",n1>n2)
print("number1 is lesser  then number 2:",n1<n2)
print("number1 is greater then or equal to number 2:",n1>=n2)
print("number1 is lesser then or equal to number 2:",n1<=n2)
print("number 1 is equal to number2:",n1==n2)
print("number 1 is not equal to number2:",n1!=n2)

# logical operators:and,or,not

# we use "AND" operators to check *le conditions together and if both are true ,then the result is true, if one fails then the result is false

print("number1 is greater than 5 and multile of 5:",n1>5 and n1 % 5==0)

print("number2 is lesser than 50 and it can be divisible by 4:",n2<50 and n2 % 4==0)


# identity operators: is & is not - we shall use this in list

# membership operators: in & not in -we shall use it in list
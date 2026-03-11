#index:0 1 2 3 4 5 6 7 8 9 10
numbers =[3, 7, 4, 8, 9, 13, 10, 15, 12, 4, 8]
# neg : -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(numbers)

#Slicing
#list[Star, end]
#start is inclusive , end is execlusive
 
#Prints from 0 to 4th position
print(numbers[0:5])

#Prinys from 2 to 6th position
print(numbers[2:7])

#prints from 3 to last position
#list[start:]
print(numbers[:6])

#print from 0 to 5th position
#list[:end]
print(numbers[6:])

#prints from last 5th position to 2nd position
print(numbers[-5:-1])

print(numbers[-7])

print(numbers[:-1])

#list[start, end, stop]
#step is for skipping the items
print (numbers[1:7:2])

print(numbers[0::3])

print(numbers[::4]))





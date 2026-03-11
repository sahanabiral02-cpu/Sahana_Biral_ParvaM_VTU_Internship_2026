# list properties:ordered,mutable(changeable)and allow duplicate values

vegitables=["carrot","tomato","onion","radish","carrot","raddish"]
print(vegitables,type(vegitables))
print(vegitables[0]) 
# values are stored in respective index followed by the list

#  ordered property refers to the sequence follwed by the list
print(vegitables[0],vegitables[3])

# list methods:append,insert,remove,pop,clear,extend,count,index,reverse,sort


# append is used to add the list items at the end of the list 
vegitables.append("cucumber")
print(vegitables)

# append is used to add the new list items at any specific index number
vegitables.insert(1,"beans")
print(vegitables)

# pop is used to remove the last item from the list
vegitables.pop(3)
vegitables.pop()
print(vegitables)

# remove is used to remove the specific value from the list
vegitables.remove("beans")
print(vegitables)




# count is used to check the number of itms repeatation in the list
carrotCount=vegitables.count("carrot")
print("carrot is repeated for",carrotCount,"times in the list")

# copy is used to copy the list items rom one list to another list
basket=[]
print(basket)
# new_list=old_list.copy()
basket=vegitables.copy()
print("items added to the basket:",basket)

# extend is used to add or copy the items from another list
fruits=["apple","bannana","mango","watermelon"]
basket.extend(fruits)
print(basket)

# sort is used to sort the list item in ascending or descending order
basket.sort()
print("items in ascending",basket)
basket.sort(reverse=True)
print("items in descending",basket)


# index method will return the position or index of the list item
firstApple=basket.index("apple")
# index(item,start-position)
secondAPple=basket.index("apple",2)
print("first apple found at index",firstApple)


# reverse is used to change the order of the list items
basket.reverse()
print(basket)








# clear is used to remove all items fro the list
vegitables.clear()
print(vegitables)


friends = ["Sarah", "Tom", "Kevin", "Thomas", "Matthew"]

print(friends[0])
print(friends[-1]) #Last item in the list
print(friends[-2]) #Second last item in the list
print(friends[1:3])

friends[1] = "David"
print(friends[1])

# List functions
lucky_numbers = [1, 4, 3, 14, 13, 53, 44]
friends = ["Sarah", "Tom", "Kevin", "Thomas", "Matthew", "Matthew"]

friends.extend(lucky_numbers) #combine two lists
friends.append("Alex") #append at the last of the list
friends.insert(1, "Kelly") #(index, value)
friends.remove("Jim")
friends.clear() #clear the entire list
friends.pop() #pops the last element

print(friends.index("Tom")) #search for the element
print(friends.count("Matthew")) #count how many elements with value "Matthew"

friends.sort() #sort the list in alphabetical/ ascending order
lucky_numbers.reverse() #reverse the list

friends2 = friends.copy() #copy the lists
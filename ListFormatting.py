my_list = [1,2,3] #create a list
print(my_list)

my_list = ["string",2,3.555] #assign new list elements
print(my_list) #prints new list
len(my_list) #shows length

my_list = ["one","two","Three Fifty Five"] #assign new list elements
print(my_list) #prints new list
my_list[0] #returns first element of the new list
print(my_list[0]) #prints first element of the new list

my_list[1:] #returns all element after the first one of the new list
print(my_list[1:]) #prints first element of the new list

another_list = ["nine", "ten"]
new_list = my_list + another_list #adds the named two lists as a string addition
print(new_list) #prints the combined list

new_list[0] = "ONE ALL CAPS" #changin the indexed (1st) element of the list of strings
print(new_list) #prints the combined list

#ADDING ELEMENTS TO THE LIST
new_list.append("eleven") #append "eleven" to the end of the list of strings

'''.append takes exatly one argument, so this results in error:
new_list.append("eleven", "twelve") '''

new_list.append("twelve")
print(new_list) #prints the updated list

#REMOVING ELEMENTS FROM THE LIST
removed = new_list.pop() #as reverse to append, removes the last member of the list
print(new_list) #prints the updated list
print(removed) #prints the removed item

removed = new_list.pop(0) #removes the first element of the list
print(new_list) #prints the updated list
print(removed) #prints the removed item

# SORTING LIST ELEMENTS
unsorted_strings = ['l', 'zs', 'g', 'w', 't', 'e', 'p', 'q', 'gy'] # CREATING AN UNsorted list
unsorted_numbers = [3, 7, 2, 11]
print(unsorted_strings)
print(unsorted_numbers)

unsorted_strings.sort() #sorting letters in ABC order
sorted_strings = unsorted_strings #re assign/name variable
unsorted_numbers.sort()  #sorting letters in ABC order
sorted_numbers = unsorted_numbers #re assign/name variable
print(sorted_strings)
print(sorted_numbers)

unsorted_numbers.reverse()
reverse_numbers = unsorted_numbers
print(reverse_numbers)



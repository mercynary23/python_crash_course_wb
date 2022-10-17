#This is a really interesting exercise; working with a number of in built properties for arrays in Python
#I'm also working with super basic 'for' and 'while' loops; nothing crazy - but fun regardless 

arr_zombies = ['Lazarus', 'Enoch', 'Malachi'] 
print("\nThese are the zombies currently in my collection:")
print(arr_zombies)
print("\n")

#This for loop will take each 'zombie' from the arr and print a message using the value at a given index

for zombie in arr_zombies:
    print(f"Morning {zombie}! Please come to dinner :D ")

#This block of code will take user input; the user input will then be used to remove a specified value
#from the array 

print("\nI've been informed that one of our guests can't make it; which guest is unavailable?")
dead_zombie = input("Please type the name of the zombie who is unavailable:\n")
print(f"\nIt is with great sadness that I must declare that {dead_zombie} will be unable to join us")
arr_zombies.remove(dead_zombie)

#This block of code will take user input; and then use the user input as a value to add to the arr

guest_zombie = input("Who would you like to invite instead?\n")
print(f"\nWe've decided to invite {guest_zombie} to the party XD\n") 
arr_zombies.append(guest_zombie)

for zombie in arr_zombies:
    print(f"Morning {zombie}! Please come to dinner :D ")

print("\nMashallah! We've found a bigger table XD\n")

#First time messing with 'while loops'; always include some type of break clause
#This block of code will prompt the user for input 3 times
#Each time the user input will be recorded in a variable and then the value appended to the arr 
#Each iteration there is an increment so that the conditional for the loop can be broken 

x = 0 
while x < 3:
    new_guest = input("Who else would you like to invite to dinner:\n")
    print(f"Welcome! We're so happy to have you {new_guest} with us this evening\n")
    arr_zombies.append(new_guest)
    x = x+1

print(arr_zombies) 

print("\n")
for zombie in arr_zombies:
    print(f"Would you like to join us for dinner {zombie}?")




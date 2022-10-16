arr_zombies = ['Lazarus', 'Enoch', 'Malachi'] 

for zombie in arr_zombies:
    print(f"Morning {zombie}! Please come to dinner :D ")

print("I've been informed that one of our guests can't make it; which guest is unavailable?")

dead_zombie = input("Please type the name of the zombie who is unavailable:\n")
print(f"It is with great sadness that I must declare that {dead_zombie} will be unable to join us")

arr_zombies.remove(dead_zombie)

guest_zombie = input("Who would you like to invite instead?\n")
print(f"We've decided to invite {guest_zombie} to the party XD ") 
arr_zombies.append(guest_zombie)

for zombie in arr_zombies:
    print(f"Morning {zombie}! Pleas come to dinner :D ")




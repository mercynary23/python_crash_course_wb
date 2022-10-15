bicycles = ['trek', 'cannondale', 'redline', 'specialised'] 
print(bicycles) 

#printing the item stored at a particular index location 
print(bicycles[1])

#formatting the item that was returned; valid action as its a string
print(bicycles[1].title())

#The code will below will attempt to return the item at the end of the array; should return 'specialised; 
print(bicycles[-1])

#Lets take things further 
message = f"My 3rd bicycle was a {bicycles[2].upper()} and I loved it so"
print(message)




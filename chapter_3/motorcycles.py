motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#The index can be reassigned to point to a different item
motorcycles[0] = 'Ducati'
print(motorcycles)

#Adding an item to the end of a list 
motorcycles.append('Trek')
print(motorcycles)

motorcycles.insert(0, 'Aston')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

#Using the pop() method on an arr 
arr_motorcycles = ['Honda', 'Yamaha', 'Suzuki'] 
print(arr_motorcycles)

pmcycle = arr_motorcycles.pop()
print(arr_motorcycles)
print(pmcycle)

last_owned = arr_motorcycles.pop()
msg = f"The last motorcycle I owned was a {last_owned.upper()}"
print(msg)

#You can pop() an item from an arr at any location using the corresponding index 
arr_mcycles_2 = ['honda', 'Ducati', 'Nissan'] 
first_mcycle = arr_mcycles_2.pop(0)
msg_txt = f"The first motorcyle I owned was a {first_mcycle.upper()}"
print(msg_txt)







print("I'll attempt to use a for loop to copy items from one list into another")

arr_mcycles = ['Ducati', 'Honda', 'Toyota'] 

for mcycle in arr_mcycles:
    msg = f"I used to own a {mcycle}"
    print(msg)

arr_emcycles = [] 

for mcycle in arr_mcycles:
    msg_txt = f"I'm moving this cycle {mcycle} into a new garage" 
    print(msg_txt)
    arr_emcycles.append(mcycle)
   

print("Welcome to my new garage")
print(f"Look at all of the bikes we have:")

for emcycle in arr_emcycles:
    print(emcycle)





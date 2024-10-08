global memory 
memory = []

# Add all of the operators into calc memory
def add_to_memory(*args):
    for i in args:
        memory.append(i)
   

def clear_memory():
    global memory
    memory.clear()
    print("Memory cleared:", memory)





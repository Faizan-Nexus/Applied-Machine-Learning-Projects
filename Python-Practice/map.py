# map() = Applies a given function to all items in a collection
# map(func, collection)

cel_temp= [37.0, 25.0, 28.0, 17.0]
print(cel_temp)

def c_to_f(temp):
    return (temp * 9/5) + 32 

far_temp = list(map(lambda temp: (temp * 9/5) + 32 , cel_temp))

print(far_temp)
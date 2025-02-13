import matplotlib.pyplot as plt
import sys
# Simple Matplotlib line plot
x = [1, 2, 3, 4] 
y = [2, 4, 6, 8]
plt.plot(x, y)  
plt.show()

r = range(3)
print(sys.getsizeof(r))

print(list(range(5)))

# Create a set
set1 = {"A", "B", "C"}

# Add new element  
set1.add("D")
print("set1",set1)

# Set union
set2 = {"D", "E", "F"}
set3 = set1 | set2 
print("set3",set3) 

# Set intersection 
set4 = set1 & set2
print("set4",set4)

# Set difference
set5 = set1 - set2 
print("set5",set5)


#### Numero Hash 
print(hash(42))      # Ejemplo con un número entero
## hash: 42
print(hash("texto")) # Ejemplo con una cadena de texto
## hash: 8910540936665217732

pet_info = { 'Name': 'Charlie', 
             'Species': 'Dog'}
print(pet_info.get(0))


## funciones con SET

## isdisjoint()
s1 = set(range(3))
s2 = set("Herman")
print(s1.isdisjoint(s2)) #pregunta si ambos sets tienen elementos en comun 

## subset()
s3 = set(range(10)) #[0,1,2,3,4,5,6,7,8,9]
s4 = set(range(2,6)) #[2,3,4,5]
print(s3.issubset(s4)) # esta [0,1,2,3,4,5,6,7,8,9] en [2,3,4,5] ??? False
print(s4.issubset(s3)) # esta [2,3,4,5] en [0,1,2,3,4,5,6,7,8,9] ??? True

##superset()
print(s3.issuperset(s4)) # estan [2,3,4,5] todos en [0,1,2,3,4,5,6,7,8,9]  ??? True
print(s4.issuperset(s3)) # estan [0,1,2,3,4,5,6,7,8,9] todos en [2,3,4,5]  ??? False

##unión
s5 = set(range(10)) #{0,1,2,3,4,5,6,7,8,9}
s6 = set("edwar1") #{"e","d","w","a","r"}
s7 = set(range(4))
print(s5.union(s6)) #junta todos los elementos de ambos sets, el 1 y el "1" son elementos diferentes
print(s5.union(s7)) #si los sets tienen elemetos en comun solo se cuentan una vez 

## intersection
print(s5.intersection(s7)) #Toma elementos que solo esten em ambos sets

## difference
print(s5.difference(s7)) #Toma elementos que estan en el primer elemento, pero ninguno del segundo


# Function to demonstrate dictionary and set concepts

def dictionary_set_examples(input_list):
    
    # Create dictionary with list values as keys
    data = {}
    for item in input_list:
        data[item] = input_list.count(item)
        
    print(f"Dictionary from list: {data}")
    
    # Convert dictionary keys to a set 
    unique_items = set(data.keys()) 
    print(f"\nUnique items: {unique_items}")
    
    # Find set difference  
    orig_set = {"A", "B", "C", "D"}
    diff_set = orig_set - unique_items
    print(f"\nSet difference: {diff_set}")
    
    # Create histogram dictionary
    hist = {}
    for item in data:
        hist[item] = "*" * data[item]
        
    print(f"\nHistogram:")
    for item in hist:
        print(f"{item} {hist[item]}")
        
input_list = ["A", "B", "C", "B", "A"]
dictionary_set_examples(input_list)

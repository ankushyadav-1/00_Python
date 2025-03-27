file = open('youtube.txt', "w")

try:
    file.write("No NAme")
    
finally:
    file.close()
    
    
with open('youtube.txt', "w") as file:
    file.write('No Name')
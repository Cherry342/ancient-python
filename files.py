my_file = open("anna.txt", "a")

#print(my_file.readlines())

my_file.write('im writing from python\n')

my_file.close()


my_file = open("anna.txt") 
for line in my_file.readlines():
    print(line, end="")

my_file = open("dtodo.py")
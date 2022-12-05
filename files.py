my_file = open("anna.txt", "r+")

#print(my_file.readlines())

for line in my_file.readlines():
    #print(line)

    #print("hello")
    #print("world")
    print(line, end="")
my_file.writelines(['im writing from python'])
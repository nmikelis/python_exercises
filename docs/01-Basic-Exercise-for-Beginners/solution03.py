# accept input string from a user
print("Give a string")
string = input()
# calculate the length of the string
length_of_string = len(string)


# iterate a each character of a string
# start: 0 to start with first character
# stop: length_of_string-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0,length_of_string - 1,2):
    print("index[", i, "]", string[i])


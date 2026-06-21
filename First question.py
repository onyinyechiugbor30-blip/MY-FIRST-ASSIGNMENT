'''Question 1: Store your full name in a variable. Write a program that shifts every letter forward by the number of 
characters in your first name (wrapping Z-A). Print the encrypted version, then write the reverse function to decrypt it back.'''

first_name = "Onyinyechi"
#this is my first name in a variable

last_name = "Ugbor"
#this is my last name in a variable
full_name = (first_name + " " + last_name)
'''this will give my full name stored in a variable, and the purpose of the empty space in quote is for the first name and the 
full name not to be joined together without space'''
print("my full name is :", full_name)
length_of_first_name =(len(first_name))
'''the above program is to get how many characters are in the first name, as that is what will be used to shift every letter 
forward'''
print ("length of first name is :", length_of_first_name)
alphabet = "abcdefghijklmnopqrstuvwxyz"

#the process of encrypting my full name
#function to encrypt a name using a ceaser cipher. A ceaser cipher is a method of hiding
def encrypt(my_name):
    #start with an empty string, and gradually, encrypted letters will be added to the string
    encrypted =""
    for letter in my_name:
        #go through each letter in the name one by one
        if letter == " ":
            encrypted = encrypted + " "
#that means if the character is an empty space, don't change anything about it
        else:
            #.lower() will convert the letter to lower case so that it will match the alphabet string
            letter = letter.lower()
#find the position(index) of the letter inside the alphabet
            index = alphabet.find(letter.lower())
#move forward by length of the first name and the %26 keeps the position within the alphabet range(26 letters)
            new_index = (index + length_of_first_name)%26
#add the encrypted letter to the result
            encrypted =encrypted + alphabet[new_index] 
    #return the completed encrypted full name
    return encrypted

#Function to decrypt a previously encrypted name and it reverses the Caesar Cipher by shifting the letters backwards.

def decrypt(my_name):
#start with an empty string
    decrypted = ""
    for letter in my_name:
#while going through the characters, if the character is an empty space, don't change anything about it
        if letter == " ":
            decrypted = decrypted + " "
        else:
## Find the position of the encrypted letter in the alphabet.
            index = alphabet.find(letter)
#move backwards by the length of the first name, and again the %26 makes the position or index not to exceed the alphabet range
            new_index = (index - length_of_first_name)%26
#add the decrypted characters to the result
            decrypted = decrypted + alphabet[new_index]
#return the completed decrypted full name
    return decrypted
encrypted_name = encrypt(full_name)
print("Encrypted name is:", encrypted_name)
decrypted_name = decrypt(encrypted_name)
print("Decrypted name is:", decrypted_name)
















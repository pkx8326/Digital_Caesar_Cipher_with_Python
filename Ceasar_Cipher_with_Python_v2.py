#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Create a list of English alphabets in lower case for encoding
alphabets = []
for i in range(97,123):
    alphabets.append(chr(i))

#Create a reverse list of English alphabets in lower case for decoding
alphabets_reverse = []
alphabets_reverse = alphabets[::-1]


#Declaring constants and initializing variables:
encryption_key = 0 #The 'shift' integer
space_pos = [] #To store the positions of spaces in the original message
upper_pos = [] #To store the positions of upper-case alphabets in the original message
loop_shift = 0 #For when encryption_key + the position of the alphabet is > 25

#Begin the program----------------------------------------------------------------------
print("Welcome to the Digital Ceasar Cipher!")

run_again = []
while run_again not in ['N', 'n']:

    choice =""
    while choice != "1" and choice != "2":
        choice = input("Please input 1 to encrypt a message or 2 to decrypt a message: ")

    if choice == "1":
        original_message = input("Please input a message to encrypt: ")

        #Getting positions of spaces from the original message
        for i in range(len(original_message)):
            if original_message[i] == " ":
                space_pos.append(i)


        #Getting positions of upper-case characters from the original message
        for c in original_message:
            if c == c.upper() and c != " ":
                upper_pos.append(original_message.index(c))


        #Prepare the original message for encryption:
        text_encode = original_message.strip().replace(" ","").lower()

        #Getting the encryptiopn key:
        while True:
            try:
                encryption_key = int(input("Please input an encryption key: "))
                break
            except ValueError:
                print("Please input only integers.")


        #Encryption process
        coded_text =""
        for letter in text_encode:
                for i in range(len(alphabets)):
                    if letter == alphabets[i]:
                        if i + encryption_key > 25:
                            loop_shift = ((i+encryption_key)%25)-((i+encryption_key)//25)
                            coded_text += alphabets[loop_shift]
                        else:
                            coded_text += alphabets[i+encryption_key]

        print(f"Your coded message is {coded_text}.")
        #print(space_pos)
        #print(upper_pos)

    else: #The choice for decryption
        text_decode = input("Please input the message to decrypt: ").strip().replace(" ","").lower()
        decoded_text_list = [] #First, the decoded text will be stored each character as a list
        decoded_text = "" #To store the final decoded text complete with proper cases and spaces

        #Getting the encryptiopn key (for decryption):
        while True:
            try:
                encryption_key = int(input("Please input an encryption key: "))
                break
            except ValueError:
                print("Please input only integers.")

        #Begin the decryption process
        for letter in text_decode:
            for i in range(len(alphabets)):
                if letter == alphabets[i]:
                    for i in range(len(alphabets_reverse)):
                        if letter == alphabets_reverse[i]:
                            if i + encryption_key > 25:
                                loop_shift = ((i+encryption_key)%25)-((i+encryption_key)//25)
                                decoded_text_list.append(alphabets_reverse[loop_shift])
                            else:
                                decoded_text_list.append(alphabets_reverse[i+encryption_key])


        #spaces re-insertion:
        for n in range(len(space_pos)):
            decoded_text_list.insert(space_pos[n], " ")

        #change to original proper case:
        for m in range(len(upper_pos)):
            decoded_text_list[upper_pos[m]] = decoded_text_list[upper_pos[m]].upper()

        #Change the decoded message into a string
        for i in decoded_text_list:
            decoded_text += i

        print(f"The decoded text is: {decoded_text}.")
        #print(space_pos)
        #print(upper_pos)

    run_again = []
    while run_again not in ['Y', 'y', 'N', 'n']:
        run_again = input("Run the program again?: ")


# In[ ]:





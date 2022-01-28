#!/usr/bin/env python
# coding: utf-8

# In[110]:


#The Digital Caesar Cipher

#The 'shift' variable:
shift = 0


#Create a function to encode
def encode(str_input):
    str_input = str_input.strip().replace(" ","").lower()
    
    str_list = []    
    str_list[:] = str_input
    
    coded_list = []
    for i in range(len(str_list)):
        coded_list.append(chr(ord(str_list[i])+shift))
    
    coded_string = ""
    print(f"Your coded message is: {coded_string.join(coded_list)}.")
    

#Create a function to decode
def decode(coded_string):
    coded_string = coded_string.strip().replace(" ","").lower()
    
    coded_list = []
    coded_list[:]  = coded_string
    
    decoded_list = []
    for i in range(len(coded_list)):
        decoded_list.append(chr(ord(coded_list[i])-shift))
        
    decoded_string = ""
    print(f"Your decoded message is: {decoded_string.join(decoded_list)}.")
    

#Begin the program    
print("Welcome to the Caear Cipher program!")

choice = 0
while choice != 1 and choice != 2:
    choice = int(input("Please input 1 to encode, or 2 to decode: "))

if choice == 1:
    text_string = input("Input a text to encode: ")
    
    while True:
        try:
            shift = int(input("Input the 'shift key': "))
            break
        except ValueError:
            print("Please input only integers.")
            
    encode(text_string)
else:
    text_string = input("Input a text to decode: ")
    
    while True:
        try:
            shift = int(input("Input the 'shift key': "))
            break
        except ValueError:
            print("Please input only integers.")
            
    decode(text_string)


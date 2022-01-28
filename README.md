# Digital_Ceasar_Cipher_with_Python
This is a fun Python project to encrypt and decryp messages using the Cesar Cipher technique. The algorithm is simple. You provide a string message (in English), the program will shift all the characters in the message in a direction to a certain number. This number is the 'encryption key' provided by the user. In order to decrypt the encryted message, the user will provide the encrypted message along with its accompanying encryption key.

Version 1:
The first version of this program is a very simple excercise with Python's function, for loop and list. This program can decrypt and encrypt any input from the keyboard. However, every character will be lower-cased and there will be no information about the spacing carried over from the original message.

Version 2:
This version is a more realistic of the Ceasar Cipher technique. It only encrypts and decrypts the 26 English alphabets. It will not give any error message if you try to encrypt the character 'z'. For example, if your message contains 'z' and your encryption key is '5', 'z' will become 'e'. The program is also capable of retaining the information about the positions of the upper-cased characters and spaces in the original message. The encrypted message will be typically 'cryptic' with all lower-cased characters and no spaces. However, the decrypted message will be exactly like the original message with proper-cased characters and all spacings originally provided by the user.

def encoder():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))    
        while shift >=50:
            if shift %2 == 0:
                shift = shift/2
            elif shift %5 == 0:
                shift = shift/5
            elif shift % 3 == 0:
                shift = shift/3
            else:
                shift = shift -1
        def encode(text, shift):
            encoded_msg = ""
            for letter in text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_pos = position + round(shift)
                    new_letter = alphabet[new_pos]
                    encoded_msg += new_letter
                else:
                    encoded_msg += letter   
            print(encoded_msg)
        encode(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))    
        while shift >=50:
            if shift %2 == 0:
                shift = shift/2
            elif shift %5 == 0:
                shift = shift/5
            elif shift % 3 == 0:
                shift = shift/3
            else:
                shift = shift -1
        def decode(text,shift):
            decoded_msg = ""
            for letters in text:
                if letters in alphabet:
                    pos = alphabet.index(letters)
                    new_posi = pos - round(shift)
                    new_letter = alphabet[new_posi]
                    decoded_msg += new_letter
                else:
                    decoded_msg += letters
            print(decoded_msg)
        decode(text , shift) 
    else:
        print("Please Enter A Valid Parameter")
    def ask():
        pa = input("Do You Want To Play Again Type y for Yes and n for No\n").lower()
        if pa == "y":
            encoder()
        elif pa == "n":
            print("BYE")
        else:
            print("Please Enter A Valid Parameter")
            ask()
    ask()
encoder()
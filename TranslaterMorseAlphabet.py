import time

def encrypt(message):
    word = ''
    for letter in message:
        if letter != ' ':
            word += latin_to_morse[letter] + ' '
        else:
            word = ' '
    return word


def decrypt(message):
    message += ' '
    deword = ''
    text = ''
    for letter in message:
        if(letter != ' '):
            i = 0
            text += letter
        else:
            i += 1
            if i==2:
                deword += ' '
            else:
                deword += list(latin_to_morse.keys())[list(latin_to_morse.values()).index(text)]
                text = ''
    
    return deword
             
    
latin_to_morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',

                    '(':'-.--.', ')':'-.--.-'}


print("What do you want ?\n1.Latin to morse\n2.Morse to latin: ", end="")
lang = input()

match(lang):
    case "1":
        message = input()
        result = encrypt(message.upper())
        time.sleep(0.5)
        print(result)
    case "2":
        message = input()
        result = decrypt(message)
        time.sleep(0.5)
        print(result)
    case other:
        print("This is not correct!")
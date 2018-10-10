from __future__ import print_function

def removeDuplicateChar(string):
    return ''.join(list(set(list(string))))

def ceasar_encrypt(string, key):
    code = []
    for char in string:
        tmp = ord(char)
        if tmp == 32:
            code.append(char)
        elif tmp <= 127 - key:
            print(chr(tmp + key))
            code.append(chr(tmp + key))
        else:
            code.append(chr((tmp + key + 33) % 128))
    return ''.join(code)

def ceasar_decrypt(string, key):
    code = []
    for char in string:
        pass
        
if __name__ == '__main__':
    print(ceasar_encrypt('The sky', 13))
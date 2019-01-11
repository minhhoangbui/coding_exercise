# -*- coding: utf-8 -*-
from __future__ import print_function

def removeDuplicateChar(string):
    return ''.join(list(set(list(string))))

class CeasarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        return self._transform(message, self._forward)
    
    def decrypt(self, message):
        return self._transform(message, self._backward)
    
    @staticmethod
    def _transform(message, code):
        msg = list(message)
        output = list(message)
        for i in range(len(msg)):
            if msg[i].isupper():
                j = ord(msg[i]) - ord('A')
                output[i] = code[j]
        return ''.join(output)

def reverse_words(string):
    string = list(string)
    reversed_str = []
    while string:
        reversed_str.append(string.pop())
    return ''.join(reversed_str)

if __name__ == '__main__':
    print(reverse_words('I love you'))

'''Solve Daily Coding Problems from #21-#30'''

def prob_22(string, tokens):
    '''
    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence 
    in a list. If there is more than one possible reconstruction, return any of them. If there is no possible 
    reconstruction, then return null.

    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you 
    should return ['the', 'quick', 'brown', 'fox'].

    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
    return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
    '''
    output = []

    while string:
        for token in tokens:
            if string.startswith(token):
                tokens.remove(token)
                output.append(token)
                string = string[len(token):]
    return output

def prob_25(string, regex_pattern):
    '''
    Implement regular expression matching with the following special characters:

        . (period) which matches any single character
        * (asterisk) which matches zero or more of the preceding element
    That is, implement a function that takes in a string and a valid regular expression and returns whether or not 
    the string matches the regular expression.

    For example, given the regular expression "ra." and the string "ray", your function should return true. The same 
    regular expression on the string "raymond" should return false.

    Given the regular expression ".*at" and the string "chat", your function should return true. The same regular 
    expression on the string "chats" should return false.
    '''
    import re
    regex_pattern = re.compile(regex_pattern)
    result = regex_pattern.search(string).group()
    return result == string

def prob_27(string):
    '''
    Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

    For example, given the string "([])[]({})", you should return true.

    Given the string "([)]" or "((()", you should return false.
    '''
    temp_list = []
    temp_dict = {')': '(', ']': '[', '}': '{'}
    for c in string:
        if c in '([{':
            temp_list.append(c)
        if c in ')]}':
            if temp_list.pop(-1) != temp_dict[c]:
                return False
    return True

def prob_28(word_list, k):
    '''
    Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings 
    which represents each line, fully justified.

    More specifically, you should have as many words as possible in each line. There should be at least one space between 
    each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as 
    equally as possible, with the extra spaces, if any, distributed starting from the left.

    If you can only fit one word on a line, then you should pad the right-hand side with spaces.

    Each word is guaranteed not to be longer than k.

    For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
    and k = 16, you should return the following:

    ["the  quick brown", # 1 extra space on the left
    "fox  jumps  over", # 2 extra spaces distributed evenly
    "the   lazy   dog"] # 4 extra spaces distributed evenly
    '''
    temp_list = []
    output = []
    reserved = k
    num_characters = 0
    while True:
        if len(word_list) != 0 and k - len(word_list[0]) >= 0:
            k -= len(word_list[0]) + 1
            num_characters += len(word_list[0])
            w = word_list.pop(0)
            temp_list.append(w)
        else:
            n = reserved - num_characters
            min_num_spaces = n / (len(temp_list) - 1)
            residual = n % (len(temp_list) - 1)
            spaces = [min_num_spaces for _ in range(len(temp_list) - 1)]
            for i in range(residual):
                spaces[i] += 1
            spaces.append(0)
            string = ''
            for word, space in zip(temp_list, spaces):
                string += word
                string += ' ' * space
            output.append(string)
            k = reserved
            temp_list = []
            num_characters = 0
            if len(word_list) == 0:
                break
    return output

def prob_29(string):
    '''
    Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent 
    repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" 
    would be encoded as "4A3B2C1D2A".

    Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and 
    consists solely of alphabetic characters. You can assume the string to be decoded is valid.
    '''

    def _encode(string):
        characters = []
        occurrences = []
        prev = None
        output = ''
        for char in string:
            if prev == None:
                characters.append(char)
                prev = char
                count = 1
            elif char == prev:
                count += 1
            else:
                occurrences.append(count)
                characters.append(char)
                prev = char
                count = 1
        occurrences.append(count)
        for char, num in zip(characters, occurrences):
            output += str(num)
            output += char
        return output

    def _decode(string):
        char_indices = list(range(1, len(string), 2))
        count_indices = list(range(0, len(string), 2))
        output = ''
        for char_idx, count_idx in zip(char_indices, count_indices):
            partial = string[char_idx] * int(string[count_idx])
            output += partial
        return output

    encoded = _encode(string)
    print _decode(encoded)

def prob_30(array):
    '''
    You are given an array of non-negative integers that represents a two-dimensional elevation map where each 
    element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls 
    get filled up.

    Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

    For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

    Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth 
    index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
    '''
    pass

if __name__ == '__main__':
    prob_29("AAAABBBCCDAA")
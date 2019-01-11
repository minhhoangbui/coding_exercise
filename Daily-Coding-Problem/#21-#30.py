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
    pass


if __name__ == '__main__':
    print prob_25("chats", r'.*at')
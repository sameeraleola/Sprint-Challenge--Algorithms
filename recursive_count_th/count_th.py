'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    s = "th"
    str_size = len(word)

    # Base case
    if str_size == 0 or str_size < len(s):
        return 0

    if (word[:2] == s):
        return count_th(word[1:]) + 1 
    else:
        return count_th(word[1:])

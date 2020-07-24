'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case
    if len(word) ==0 or len(word) < 2:
        return 0
        
    else:
        #recursive solution
        if word[0:2] == "th":
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])

print(count_th("hwhorkth"))

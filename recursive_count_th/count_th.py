'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    check = 'th'
    count = 0
    if len(word) > 1:
        if word[0:2] == check:
            return count + 1 + count_th(word[2:])
        else:
            return count_th(word[1:])
    else:
        return count

wrd = 'mythriftyThirties'

print(count_th(wrd))
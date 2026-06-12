def toLowerCase(s):
    #to be clear, this is an easy problem that can be solved with a built in function, so I purposefully made this slightly more convoluted.

    for char in s:
        if ord(char) in range(65, 91):
            s = s.replace(char, chr(ord(char) + 32))
    return s

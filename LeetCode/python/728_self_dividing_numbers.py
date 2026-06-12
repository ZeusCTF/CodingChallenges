def selfDividingNumbers(left, right):
    ans = []

    def check(char, num):
        if char == '0':
            return False
        
        elif num % int(char) == 0:
            return True
        else:
            return False


    for num in range(left, right+1):
        valid = True
        for char in str(num):
            valid = check(char, num)
            if valid:
                pass
            else:
                break
        if valid:
            ans.append(num)

    return ans


selfDividingNumbers(left = 47, right = 85)
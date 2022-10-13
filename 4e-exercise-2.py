def is_palindrom(strin):
    
    return strin == strin[::-1]

    ########### OR #############

    # if strin == strin[::-1]:
        # return True
    # else:
        # return False

    ########### OR #############

    # if strin == strin[::-1]:
        # return True
    # return False

word = input("Enter the word : ")
print(is_palindrom(word))
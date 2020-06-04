def devisors_func(user_str1, user_str2):
    user_inputted_num1 = int(user_str1)
    user_inputted_num2 = int(user_str2)
    print 'The greatest common divisor of these two numbers is: '

    found = False

    idx = user_inputted_num1
    if idx < user_inputted_num2:
        idx = user_inputted_num2

        while idx > 0:
            if user_inputted_num1 % idx == 0 and user_inputted_num2 % idx == 0:
                found = True
                return idx
                break
                idx -= 1

                if found == False:
                    return "No divisor found (or it's 1)!"

def v38():
    start_value = 99999
    found = True

    while found:
        new_string = ''
        try_new = True
        multi = ''

        while try_new:
            for i in range(1, 10):
                new_string += str(i*start_value)
                if len(new_string) > 8:
                    break
                multi += str(i)
            
            if len(new_string) != 9:
                try_new = False
                break

            # to the check
            for a in range(1,9):
                if new_string.count(str(a)) != 1:
                    try_new = False
                    break

            if try_new == True:
                print('Found: ', start_value, ' ', multi, ' ', new_string)
                found = False



        start_value -= 1


if __name__ == "__main__" :
    v38()
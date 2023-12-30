# 38803160272
while True:
    idcode = input('Please enter ID: ')
    if idcode.lower() == 'exit':
        print('Good bye!')
        break
    try:
        int(idcode)
        if len(idcode) == 11:
            print('GOOD', idcode)
        else:
            raise Exception
    except ValueError:
        print('ID must be numeric. Try again or type "exit"')
        continue
    except Exception:
        if len(idcode) < 11:
            print('ID is too short')
        else:
            print('ID too long')
        continue
    else:
        while True:
            user_choice = input('1.Gender\n'
                                '2.Date of birth\n'  # DD.MM.YYYY
                                '3.Region of birth\n'
                                '4.Validation\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '--> ')
            if user_choice == '1':
                print('Choose 1')
            elif user_choice == '2':
                print('Choose 2')
            elif user_choice == '3':
                print('Choose 3')
            elif user_choice == '4':
                print('Choose 4')
            elif user_choice == '5':
                break
            elif user_choice == '0':
                exit()
            else:
                print('Choice is out of range!')



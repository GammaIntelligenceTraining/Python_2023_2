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
                if idcode[0] not in '09':
                    if int(idcode[0]) % 2 == 0:
                        print('You are Female')
                    else:
                        print('You are Male')
                else:
                    print('There is something wrong with your ID!')
            elif user_choice == '2':  # DD.MM.YYYY
                if idcode[0] not in '09':
                    birth_cent = ''
                    if idcode[0] in '12':
                        birth_cent = '18'
                    elif idcode[0] in '34':
                        birth_cent = '19'
                    elif idcode[0] in '56':
                        birth_cent = '20'
                    elif idcode[0] in '78':
                        birth_cent = '21'
                    birth_date = f'{idcode[5:7]}.{idcode[3:5]}.{birth_cent}{idcode[1:3]}'
                    print(f'Birth date: {birth_date}')
                else:
                    print('There is something wrong with your ID!')
            elif user_choice == '3':
                region_num = idcode[7:10]
                if int(region_num) in range(1, 11):
                    print('You were born in Kuressaare Hospital')
                elif region_num >= '011' and region_num <= '019':
                    print('You were born in Tartu University Women\'s Clinic')
                elif '021' <= region_num <= '150':
                    print('You were born in East Tallinn Central Hospital, Pelgulinna Maternity Hospital (Tallinn)')
                else:
                    print('You were not born in Estonia.')
            elif user_choice == '4':
                chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                result = 0
                for index in range(10):
                    result += int(idcode[index]) * chk1[index]
                if result % 11 == int(idcode[-1]):
                    print('ID is valid 1')
                elif result % 11 == 10:
                    result = 0
                    for index in range(10):
                        result += int(idcode[index]) * chk2[index]
                    if result % 11 == int(idcode[-1]):
                        print('ID is valid 2')
                    else:
                        print('ID is not valid 2')
                else:
                    print('ID is not valid 1')
            elif user_choice == '5':
                break
            elif user_choice == '0':
                exit()
            else:
                print('Choice is out of range!')



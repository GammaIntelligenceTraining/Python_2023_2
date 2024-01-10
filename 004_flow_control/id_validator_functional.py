# 38803160272
def ask_for_id():
    global idcode
    while True:
        user_id = input('Please enter ID: ')
        if user_id.lower() == 'exit':
            print('Good bye!')
            exit()
        try:
            int(user_id)
            if len(user_id) == 11:
                print('GOOD', user_id)
            else:
                raise Exception
        except ValueError:
            print('ID must be numeric. Try again or type "exit"')
            continue
        except Exception:
            if len(user_id) < 11:
                print('ID is too short')
            else:
                print('ID too long')
            continue
        else:
            idcode = user_id
            break
    menu()


def get_gender():
    if idcode[0] not in '09':
        if int(idcode[0]) % 2 == 0:
            print('You are Female')
        else:
            print('You are Male')
    else:
        print('There is something wrong with your ID!')


def get_birthday():
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


def get_region():
    region_num = idcode[7:10]
    if int(region_num) in range(1, 11):
        print('You were born in Kuressaare Hospital')
    elif region_num >= '011' and region_num <= '019':
        print('You were born in Tartu University Women\'s Clinic')
    elif '021' <= region_num <= '150':
        print('You were born in East Tallinn Central Hospital, Pelgulinna Maternity Hospital (Tallinn)')
    else:
        print('You were not born in Estonia.')


def validation_process(chk):
    result = 0
    for i in range(10):
        result += int(idcode[i]) * chk[i]
    return result % 11


def validate():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    if validation_process(chk1) == int(idcode[-1]):
        print('ID is valid 1')
    elif validation_process(chk1) == 10:
        if validation_process(chk2) == int(idcode[-1]):
            print('ID is valid 2')
        else:
            print('ID is not valid 2')
    else:
        print('ID is not valid 1')

def menu():
    while True:
        user_choice = input('1.Gender\n'
                            '2.Date of birth\n'  # DD.MM.YYYY
                            '3.Region of birth\n'
                            '4.Validation\n'
                            '5.Change ID\n'
                            '0.Exit\n'
                            '--> ')
        if user_choice == '1':
            get_gender()
            continue
        elif user_choice == '2':
            get_birthday()
            continue
        elif user_choice == '3':
            get_region()
            continue
        elif user_choice == '4':
            validate()
            continue
        elif user_choice == '5':
            break
        elif user_choice == '0':
            exit()
        else:
            print('Choice is out of range!')

    ask_for_id()

idcode = ''
ask_for_id()
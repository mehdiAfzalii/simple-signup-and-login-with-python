import datetime
import json


class Signup:
    def __init__(self):
        self.username = input('Enter your username : ')
        with open('usernames.json') as infile:
            username = json.load(infile)
        if self.username not in username:
            username.append(self.username)
            with open('usernames.json', 'w') as outfile:
                json.dump(username, outfile)
            self.name = input('Enter your name : ')
            self.birthYear = int(input('Enter your birth year : '))
            self.gender = input('Enter your gender : ')
            self.id = input('Enter your id : ')
            self.password = input('Enter your password : ')
            self.save()
        else:
            print('invalid username...'.title())

    def calcAge(self):
        year = datetime.datetime.now().year
        return year - self.birthYear

    def save(self):
        with open('database.json') as infile:
            db = json.load(infile)
        data = {
            'username': self.username,
            'full name': self.name.title(),
            'gender': self.gender,
            'age': self.calcAge(),
            'code': self.id,
            'password': self.password,
            'last seen': str(datetime.datetime.now())
        }
        db.append(data)
        with open('database.json', 'w') as outfile:
            json.dump(db, outfile, indent=4)


class Login:
    def __init__(self):
        self.username = input('Enter your username : ')
        self.password = input('Enter your password : ')

    def check(self):
        with open('database.json') as infile:
            db = json.load(infile)
            for i in db:
                try:
                    if i['username'] == self.username and i['password'] == self.password:
                        return True, self.username
                except:
                    return False


def calcAge(birthYear):
    year = datetime.datetime.now().year
    return year - birthYear


message = 'Do you want to open account or you an account if you have account enter 1 else enter 2 and for exit enter 3.'
print(message.title())
while True:
    question = input('Enter your option 1 : '.title())
    if question == '1':
        Signup()
        break
    elif question == '2':
        result, username = Login().check()
        if result:
            print('welcome to your profile...'.title())
            text = 'if you want change your full name enter 1 or change your gender enter 2 or change your password eneter 3 or change your birth year enter 4 and you have exit enter 5....'
            print(text.title())
            choice = input('Enter your option 2 : '.title())
            with open('database.json') as infile:
                db = json.load(infile)
                for i in db:
                    if i['username'] == username:
                        if choice == '1':
                            new_name = input('please enter your new full name : '.title())
                            i['full name'] = new_name.title()
                            i['update'] = f'Full Name update in {datetime.datetime.now()}'.title()
                            i['last seen'] = f'last seen at {datetime.datetime.now()}'
                            with open('database.json', 'w') as outfile:
                                json.dump(db, outfile, indent=4)
                            print('its done...'.title())
                            break
                        elif choice == '2':
                            new_gender = input('please enter your new gender : '.title())
                            i['gender'] = new_gender
                            i['update'] = f'Gender update in {datetime.datetime.now()}'.title()
                            i['last seen'] = f'last seen at {datetime.datetime.now()}'
                            with open('database.json', 'w') as outfile:
                                json.dump(db, outfile, indent=4)
                            print('its done...'.title())
                            break
                        elif choice == '3':
                            new_password = input('please enter your new password : '.title())
                            i['password'] = new_password
                            i['update'] = f'password update in {datetime.datetime.now()}'.title()
                            i['last seen'] = f'last seen at {datetime.datetime.now()}'
                            with open('database.json', 'w') as outfile:
                                json.dump(db, outfile, indent=4)
                            print('its done...'.title())
                            break
                        elif choice == '4':
                            new_birthYear = int(input('please enter your new birth Year : '.title()))
                            i['age'] = calcAge(new_birthYear)
                            i['update'] = f'age update in {datetime.datetime.now()}'.title()
                            i['last seen'] = f'last seen at {datetime.datetime.now()}'
                            with open('database.json', 'w') as outfile:
                                json.dump(db, outfile, indent=4)
                            print('its done...'.title())
                            break
                        elif choice == '5':
                            print('BYE...')
                            exit()
                        else:
                            print('invalid answer'.title())
        else:
            print('Some thing wrong, you dont have account or username or password is wrong....')
            break
    elif question == '3':
        print('BYE...')
        break
    else:
        print('Invalid answer, please try again...')

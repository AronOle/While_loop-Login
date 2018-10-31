correct_pasword = 'xx1'
name = input('Enter name: ')
surname = input('Enter surname: ')
pasword = input('Enter the paswword: ')

while correct_pasword != pasword:
    pasword = input('ERROR, Enter the pasword again: ')

message = 'Hello %s %s, you are succesfuly  logged In' % (name,surname)
print(message)

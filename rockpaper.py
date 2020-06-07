import random

rating_file = open('rating.txt','w')
rating_file.write('Olesia 1000\nNatalia 1500\n')
rating_file.close()
# Write your code here

print('Enter your name: ', end='')
name = input()
print('Hello, ' + name)
score = 0
options = input().split(',')

if options == ['']:
    options = ['rock', 'paper', 'scissors']
print('Okay, let\'s start')
print(options)

rating_file = open('rating.txt','r')
rating = rating_file.readlines()
rating_file.close()

for rate in rating:
    a, b = rate.split(' ')
    if a == name:
        score = int(b)


user = input()
while user != '!exit':
    if user not in options:
        if user == '!rating':
            print('Your rating: {}'.format(score))
        else:
            print('Invalid input')
    else:
        option = random.choice(options)
        if user == option:
            print('There is a draw ({})'.format(option))
            score += 50
        else:
            new_opt = options[options.index(user)+1:]
            new_opt.extend(options[:options.index(user)])
            if option in new_opt[0:int(len(new_opt)/2)]:
                print('Sorry, but computer chose', option)
            else:
                print('Well done. Computer chose {} and failed'.format(option))
                score += 100
    user = input()
else:
    print('Bye!')

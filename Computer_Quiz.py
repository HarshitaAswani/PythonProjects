print("Welcome")
playing = input('Do you want to play?')
print(playing)
if playing != "yes":
    quit()
else:
    print("okay, let's play")
score = 0
answer = input('What does DSA stand for?')
if answer.lower() == 'data structure and algorithm':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does API stand for?')
if answer.lower() == 'application programming interface':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does ML stand for?')
if answer.lower() == 'machine learning':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does AI stand for?')
if answer.lower() == 'artificial intelligence':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does DL stand for?')
if answer.lower() == 'deep learning':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does NLP stand for?')
if answer.lower() == 'natural language processing':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does GUI stand for?')
if answer.lower() == 'graphic user interface':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does HTML stand for?')
if answer.lower() == 'hyper text markup language':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does HTTP stand for?')
if answer.lower() == 'hyper text transfer protocol':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does WWW stand for?')
if answer.lower() == 'world wide web':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does JS stand for?')
if answer.lower() == 'java script':
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input('What does CSS stand for?')
if answer.lower() == 'cascading style sheets':
    print('correct!')
    score += 1
else:
    print('incorrect!')
print('You got '+ str(score) + ' questions correct!')
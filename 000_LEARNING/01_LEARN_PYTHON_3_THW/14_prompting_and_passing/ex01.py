from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to as you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking meself.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''')

''' OUTPUT
python.exeex01.py masfergi
Hi masfergi, I'm the ex01.py script.
I'd like to as you a few questions.
Do you like me masfergi?
> yes
Where do you live masfergi?
> surabaya
What kind of computer do you have?
> asus

Alright, so you said yes about liking meself.
You live in surabaya. Not sure where that is.
And you have a asus computer. Nice.
'''

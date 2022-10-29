mood = input("How's your mood?")
if 'good' in mood or 'ok' in mood:
    print("Great, I'm also doin' good!")
elif 'bad' in mood or 'terrible' in mood:
    print("Don't worry, it'll be better soon!")
else:
    print('Oh, really?')

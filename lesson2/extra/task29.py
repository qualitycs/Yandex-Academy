favoriteHoliday = input("What is your favorite Holiday? Enter 1 for Christmas, enter 2 for Halloween,"
                        " enter 3 for Easter or enter 4 For Valentine's day:")
if favoriteHoliday != '1' and favoriteHoliday != '2' and favoriteHoliday != '3' and favoriteHoliday != '4':
    print('Invalid Input')
    quit()
favoriteFood = input("What is your favorite type of food? Enter 1 for Burgers, enter 2 for Sushi or enter 3 for Pizza:")
if favoriteFood != '1' and favoriteFood != '2' and favoriteFood != '3':
    print('Invalid Input')
    quit()
favoriteColor = input('What is your favorite color? Enter 1 for Red, enter 2 for Green or enter 3 for blue:')
if favoriteColor != '1' and favoriteColor != '2' and favoriteColor != '3':
    print('Invalid Input')
    quit()

if favoriteHoliday == favoriteFood == favoriteColor:
    print('You are a prolific copier!')
if favoriteHoliday == '1' and favoriteFood == '2' and favoriteColor == '3':
    print('You are an incredible counter!')
if favoriteHoliday == '4' and favoriteFood == '2' and favoriteColor == '1':
    print('You are a romantic!')
if favoriteHoliday == '3' and favoriteFood == '1' and favoriteColor == '3':
    print('You are mentally insane.')
else:
    print('You are an enigma.')

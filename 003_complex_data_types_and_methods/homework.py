# Write a code that asks user to enter something
# Then checks if length of the input is longer than 10
# Adds it to long_words list
# Else adds it to short_words list
#
# long_words = []
# short_words = []
#
# user_input = input('Enter something: ')
# if len(user_input) > 10:
#     long_words.append(user_input)
# else:
#     short_words.append(user_input)
#
# if len(long_words) > 0:
#     print(f'Long words: {", ".join(long_words)}.')
# elif len(short_words) > 0:
#     print(f'Short words: {", ".join(short_words)}.')


# # Write a code that takes user input and checks if color is in a list
# colors = ['red', 'green', 'blue', 'yellow', 'gold']
# user_input = input('Name a color: ')
# if user_input.lower() in colors:
#     print(f'{user_input.title()} is in colors.')
# else:
#     print(f'{user_input.title()} is not in colors.')



# Write a code that takes user input and checks if color entered by user is in colors list
# If it is, deletes it and prints message.
# If it is not in a list prints "Color not found"
colors = ['red', 'green', 'blue', 'yellow', 'gold']
user_input = input('Choose color: ')
if user_input.lower() in colors:
    colors.remove(user_input.lower())
    print(f'{user_input} is deleted from list.')
else:
    print(f'{user_input} is not found.')
print(f'Colors: {", ".join(colors)}.')
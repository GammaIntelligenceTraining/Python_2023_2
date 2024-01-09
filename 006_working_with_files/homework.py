with open('text_files/big.txt', 'r', encoding='utf8') as file:
    data = file.read()
    symbols = '!?.,*"'
    data = data.lower()
    for sym in symbols:
        data = data.replace(sym, '')
    data = data.replace('\n', ' ')
    words = data.split()
    unique = list(set(words))

with open('text_files/big_result.txt', 'w', encoding='utf8') as file:
    file.write(f'There are {len(words)} words in big.txt\n')
    file.write(f'There are {len(unique)} unique words in big.txt\n')
    unique.sort()
    for word in unique:
        file.write(f'{word}\n')


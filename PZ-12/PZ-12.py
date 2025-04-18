from string import ascii_letters
letters = 'hыtφтrцзqπ'
is_eng = [f'{letter}-ДА' if letter in ascii_letters else f'{letter}-НЕТ' for
letter in letters]
print(is_eng)

string = 'hhhhhellllooooowwwwwweehhhhhhh'
count_char_dict = {}
for char in string:
    count = count_char_dict.get(char, 0)
    count += 1
    count_char_dict[char] = count

letter_with_max_count = ""
max = 0
for k, v in count_char_dict.items():
    if v > max:
        letter_with_max_count = k
        max = v

print (letter_with_max_count)
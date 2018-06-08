def reverse_string(string_to_be_reversed):
    reversed_string = []
    string_len = len(string_to_be_reversed)
    for count in range(1 , string_len+1):
        print(count)
        reversed_string.append(string_to_be_reversed[string_len - count])
    return "".join(reversed_string)

reversed = reverse_string("Mareena")


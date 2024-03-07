string = input()
upper_string = string.upper()
lower_string = string.lower()
output = []

for i in range(len(string)):
    if string[i] == upper_string[i]:
        output.append(lower_string[i])
    else:
        output.append(upper_string[i])

print(''.join(output))
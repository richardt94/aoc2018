with open("input5.txt") as f:
    polymer = f.read().rstrip()

for letter in range(26):
    i = 1
    result = polymer
    while result[0] == chr(letter + 65) or result[0] == chr(letter + 97):
        result = result[1:]
    while i < len(result):
        if ord(result[i]) == letter + 65 or ord(result[i]) == letter + 97:
            result = result[:i] + result[i+1:]
        elif abs(ord(result[i-1])-ord(result[i])) == 32:
            result = result[:i-1] + result[i+1:]
            if i > 0:
                i -= 1
        else:
            i += 1

    print(chr(letter + 65), len(result))
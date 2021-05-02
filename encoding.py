#from https://www.geeksforgeeks.org/how-to-encode-and-decode-a-message-using-python/

input = "some input goes here"

conversion_code = {
    #uppercase
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
    'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
    'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
    'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
    'Y': 'B', 'Z': 'A',
    #lowercase
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
    'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    's': 'h', 't': 'g', 'u': 'F', 'v': 'e', 'w': 'd', 'x': 'c',
    'y': 'b', 'z': 'a'
}

#for x in conversion_code:
#  print(x)

converted_output = ""

for i in range(0, len(input)):
    if input[i] in conversion_code.keys():
        converted_output += conversion_code[input[i]]
    else:
        converted_output += input[i]

print(converted_output)
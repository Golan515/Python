def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar !=char:
            encodedList.append((prevChar,count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList
def decodeString(encodedList):
    decodeStr = ''
    for item in encodedList:
        decodeStr = decodeStr + item[0] * item[1]
    return decodeStr
user_input = input("Enter text to encode: ").strip()
if user_input:  # Check if input is not empty
    encoded = encodeString(user_input)
    print("Encoded:", encoded)
    decoded = decodeString(encoded)
    print("Decoded:", decoded)
    print("Matches original:", user_input == decoded)
else:
    print("No input provided!")
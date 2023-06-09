def get_most_common_letter(text):
    counter = {}
    for char in text:
        # print(char)
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
        # print(counter[char])
    # print (f' counter is: {counter}')
    # print (f"sorted counter is: {sorted(counter.items())}")
    # need to sort according to values not keys
    letter = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    # need to slice to return max value key
    # print(f'should show counter sorted by values{sorted(counter.items(), key=lambda item: item[1])}')
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
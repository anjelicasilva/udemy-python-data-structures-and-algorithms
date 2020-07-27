def anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    letter_dict = {}

    for char in s1:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1

    for char2 in s2:
        if char2 not in letter_dict:
            return False
        elif letter_dict[char2] == 1:
            del letter_dict[char2]
        else:
            letter_dict[char2] -= 1
    
    return True
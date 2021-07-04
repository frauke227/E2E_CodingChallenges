# Uncensoring Strings
def uncensor(string, vowels):
    """Given a censored string and a string of the censored vowels, return the original uncensored string.

    Args:
        string ([string]): [censored string]
        vowels ([string]): [(censored) vowels]
    """
    original_string=""
    vowels_index = 0 
    for i in range(len(string)):
        if string[i] == "*":
            original_string += vowels[vowels_index]
            vowels_index += 1
        else:
            original_string += string[i]
    return original_string

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
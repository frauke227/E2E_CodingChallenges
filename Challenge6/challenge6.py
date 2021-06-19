#String Comparison

def neutralise(string1, string2):
    """
    Given are two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

    - When positives and positives interact, they remain positive. --> "+" against a "+" returns another "+".
    - When negatives and negatives interact, they remain negative. --> "-" against a "-" returns another "-".
    - But when negatives and positives interact, they become neutral, and are shown as the number 0. -->"+" against a "-" returns "0".
    The first character of each string is compared, then the next in turn and so on. A new string of characters will be returned.
    Example: neutralise("+-+", "+--") ➞ "+-0"

    Args:
        string1 ([string]): [comprised of + and -]
        string2 ([string]): [comprised of + and -]
    """
    string3 = "" 
    for x, y in zip(string1, string2):
        if x == y:
            string3 += x
        else:
            string3 += "0"
    return string3

print(neutralise("--++--", "++--++"))
print(neutralise("-+-+-+", "-+-+-+"))


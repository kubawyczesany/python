# Given a string, simple swap the case for each of the letters.
# e.g. HeLLo -> hEllO

string = input ("Give a string to swap: ")

def swap(string_):
    _string = ''.join([i.upper() if i.islower() else i.lower() for i in string_])
    return (_string)

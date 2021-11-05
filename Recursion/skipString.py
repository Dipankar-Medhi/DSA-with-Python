def skip(upstring, processed):
    # return the processed stirng if the given string is empty
    if upstring == "":
        print(processed)
    # if the given string is not empty, proceed with intializing char var
    if upstring != "":
        char = upstring[0]

        # if char is equal to a, call function after removing the char variable from the given string along with the processed string
        if char == 'a':
            skip(upstring.replace(char, "", 1), processed)
        else:
            skip(upstring.replace(char, "", 1), processed+char)


def skipStr(upstring):

    if upstring != "":
        strng = upstring[0:5]
        if strng == "apple":
            return skipStr(upstring.replace(strng, "", 1))
        else:
            return strng + skipStr(upstring.replace(strng, "", 1))
    else:
        return ""


# skip("adhkdfa", "")
print(skipStr("helloapplemyfriend"))

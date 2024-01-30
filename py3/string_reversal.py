def string_reversal(str_in: str) -> str:
    if str_in == "":
        return ""
    return string_reversal(str_in[1:]) + str_in[0]


print(string_reversal("hello"))

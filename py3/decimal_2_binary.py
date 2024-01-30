def decimal_2_binary(dec: int, bin: str) -> str:
    if dec == 0:
        return bin
    return decimal_2_binary(dec // 2, str(dec % 2) + bin)


print(decimal_2_binary(99999999, ""))

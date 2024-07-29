def string_upper(s: str) -> str:
    """将某个字符串里所有英文字母由小写转为大写"""
    chars = []
    for ch in s:
        if ch >= "a" and ch <= "z":
            # 32 是小写字母与大写字母在ASCII码表中的距离
            chars.append(chr(ord(ch) - 32))
        else:
            chars.append(ch)
    return "".join(chars)

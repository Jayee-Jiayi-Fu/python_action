
def strStr( haystack: str, needle: str) -> int:

    try:
        return haystack.index(needle)
    except ValueError as e:
        return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))


haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))


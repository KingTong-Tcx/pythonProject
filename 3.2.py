lst = ["as", "asdfff", "aaaabbbb", "ass"]
str1 = ""
for item in lst:
    if len(item) > len(str1):
        str1 = item
print(str1)
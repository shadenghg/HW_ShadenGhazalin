str1 = "working"
str2 = "work"
if len(str1) >= 3:
    if str1[-3:] == "ing":
        str1 = str1 + "ly"
        print(str1)
    else:
        str1 = str1 + "ing"
        print(str1)
else:
    print(str1)

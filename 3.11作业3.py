Score = float(input("请输入分数：\n"))
if Score < 0 or Score > 1:
    print("error message")
elif Score >= 0.9:
    print("A")
elif Score >= 0.8:
    print("B")
elif Score >= 0.7:
    print("C")
elif Score >= 0.6:
    print("D")
elif Score < 0.6:
    print("F")
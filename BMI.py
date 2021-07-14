#CalBMI++.py
try:
    w,h = eval(input("请输入您的身高体重并用逗号隔开"))
except:
    print("输入信息有误")
bmi = w / (h ** 2)
who,nat = "正常","正常"
print("{:.2f}".format(bmi))
if 0 < w < 100000 and 0 < h < 100000 :
    if bmi < 18.5 :
            who,nat = "偏瘦","偏瘦"
    elif 18.5 <= bmi< 24:
            who,nat = "正常","正常"
    elif 24 <= bmi< 25:
            who,nat = "正常","偏胖"
    elif 25 <= bmi< 28:
            who,nat = "偏胖","偏胖"
    elif 28 <= bmi< 30:
            who,nat = "偏胖","肥胖"
    else :
            who,nat = "肥胖","肥胖"
print(who,nat)
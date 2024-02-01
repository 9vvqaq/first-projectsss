#BMI.py
height,weight = eval(input("请输入:"))
bmi = weight / pow(height,2)
print("BMI is {:.2f}".format(bmi))
if bmi < 18.5:
    INT,CHINA = "偏瘦","偏瘦"
elif 18.5 <= bmi < 30:
    INT,CHINA = "还不错","OK"
else :
    INT,CHINA = "寄了"
print("对应的指标为:国际：{0}，国内：{1}".format(INT,CHINA))

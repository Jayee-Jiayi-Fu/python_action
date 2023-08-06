# 条件判断计算BMI
# height =  input('Your height: ')
# weight = input('Your weight: ')

# BMI  = float(weight)/float(height)**2
# # print('BMI = %f' % BMI)
# if BMI < 18.5:
#     print('BMI is %.1f, too light' % BMI)  
# elif BMI >= 18.5 and BMI < 25:
#     print('BMI is %.1f, normal'% BMI)  
# elif BMI >= 25 and BMI  < 28:
#     print('BMI is %.1f, over weight'% BMI)  
# elif BMI >= 28 and BMI < 32:
#     print('BMI is %.1f, fat' % BMI)  
# else:
#     print('BMI is %.1f, too fat' % BMI)  



# 循环
sum = 0
for x in range(1,101):
    sum += x
print(sum)


L = ['Bart', 'Lisa', 'Adam']
i = 0
while i < len(L):
    print(L[i])
    i+=1


for x in range(1,11):
    if x % 2 == 0:
        continue
    print(x)
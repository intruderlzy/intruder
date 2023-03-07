# 实操题讲解-科拉茨猜想
<img src="attachment:image.png" alt="Drawing" style="width: 800px;" align="left"/>
# 解题思路
<img src="attachment:image.png" alt="Drawing" style="width: 700px;" align="left"/>
#输入一个数字，但是注意这时是字符串形式的。
n = input()
# print("输入的数字为:",n,"\nn的类型为：",  type(n))  #这一行考试不需要

#将输入的字符串n转换为整数型
n = int(n)

#设置NumList用于存放每次更新的科拉茨数
NumList = [ ]

#while循环，终止条件为1出现
while n != 1:
    #将更新的n加入Nunlist进行保存
    NumList.append(n)
    #打印显示每次循环的整个科拉茨数列
#     print(NumList)  #考试不需要
    
#     # 查看当前的科拉茨数是不是1，然后进行计数。
#     if n == 1 : CountLabel += 1
    
    
    if n % 2 == 0:          #通过判定除2的余数是否为0来判定偶数
        n = n // 2          #偶数除以2
    else:
        n = n * 3 +1        #奇数乘3+1

#[1,2,3,4,5] extend [6,7,8]为 [1,2,3,4,5,6,7,8]。
#此处补[1,4,2,1]而不是[4,2,1]是因为 条件（while n != 1）在n==1时终止，循环内的append无法执行。
NumList.extend([1,4,2,1])
# NumList.append(1)
# NumList.append(4)
# NumList.append(2)
# NumList.append(1)
# for i in [1,4,2,1]:
#     NumList.append(i)
print(NumList)
# 算法分析2
<img src="attachment:image.png" alt="Drawing" style="width: 600px;" align="left"/>
# 代码实现
#输入一个数字，但是注意这时是字符串形式的。
n = input()
print("输入的数字为:",n,"\nn的类型为：",  type(n))
#将输入的字符串n转换为整数型
n = int(n)

#设置CountLabel，用于记录1出现的次数
CountLabel = 0

#设置NumList用于存放每次更新的科拉茨数
NumList = []

#while循环，终止条件为1出现的次数为2
# while CountLabel != 2:
while NumList.count(4) != 2:
    #将更新的n加入Nunlist进行保存
    NumList.append(n)
    #打印显示每次循环的整个科拉茨数列
    print(NumList)
    
    # 查看当前的科拉茨数是不是1，然后进行计数。
#     if n == 1 : CountLabel += 1
    
    
    if n % 2 == 0:          #通过判定除2的余数是否为0来判定偶数
        n = n // 2          #偶数除以2
    else:
        n = n * 3 +1        #奇数乘3+1
NumList.extend([2,1])
print(NumList)

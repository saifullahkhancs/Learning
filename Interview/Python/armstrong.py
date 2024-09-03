num = int(input("enter the number"))
# str_num = str(num)
result = []
i=num
length=0
while(i > 0):
    num1 = i%10
    i = i//10
    length += 1
    result.append(num1)

sum = 0
for i in result:
    sum = i**length + sum

if sum == num:
    print("yes")
else:
    print("no")
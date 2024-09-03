listt = [3,9,7,6,5,4]

for i in range(len(listt)):
    a= listt[i]
    for j in range(i,len(listt)):
        if listt[i] > listt[j]:
            listt[i] , listt[j] = listt[j] , listt[i] 
print(listt)

# swapping method  bove question is solved by the swapping method

# candies= 15
# offer = [3 rappers of candies = 1 free candy] = 23

# 5-3 = 2+1 = 3-3 = 1
# 22 correct answer




# str = "my name is khan"
# output_str = "khan is name my"

# new_str = ""
# def reverse_str(new_str, str):
#     strrr = str.split(" ")
#     print(len())
#     for i in range(-1,-(len(strrr))):     
#          print(i)           
#          new_str = new_str + strrr[i]
#          print(new_str)
#     return new_str

# rs = reverse_str(new_str , str)
# print(rs)

 



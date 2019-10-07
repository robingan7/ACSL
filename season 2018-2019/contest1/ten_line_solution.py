'''answer=input()
list1=[]
i3=0
for i in range(len(answer.split('\n'))):
    list1.append(answer.split(' ')[i])
for i2 in range(5):
 
    number,base=list1[i3],int(list1[i3+1])
    i3=i3+2
    print(sum([int((number+"0"*(base-len(number)%base))[i*base:(i+1)*base]) for i in range(len(number+"0"*(base-len(number)%base))//base)]))
    
'''
numbers= []
for i in range(0,5):
    raw=input().split(" ")
    num,length,total=raw[0],int(raw[1]),0
    num+=("0"*(length-(len(num)%length)))
    for j in range(int(len(num)/length)):
        total+= int(num[j*length:(j+1)*length])
    numbers.append(total)
for i in range(0,5): 
    print(numbers[i])
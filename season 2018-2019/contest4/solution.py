def isSign(input1):
    if(str(input1)=="-" or str(input1)=="+" or str(input1)=="*" or str(input1)=="@" or str(input1)=="|" or str(input1)==">"):
        return True
    else:
        return False
def cal(a,s,d):
    if(str(a)=="-"):
        return int(s)-int(d)
    elif(str(a)=="+"):
        return int(s)+int(d)
    elif(str(a)=="*"):
        return int(s)*int(d)
def cal2(a,s,d,f):
    if(str(a)==">"):
        return max(int(s),int(d),int(f))
    else:
        if(int(s)>0):
            return int(d)
        else:
            return int(f)
        
origin_list,tem=input().split(" "),[]
for x in range(len(origin_list)-1,-1,-1):
    if(not isSign(origin_list[x])):
        tem.append(origin_list[x])
    else:
        if(str(origin_list[x])=="-" or str(origin_list[x])=="+" or str(origin_list[x])=="*"):
            tem.append(cal(origin_list[x],tem.pop(),tem.pop()))
        elif(str(origin_list[x])=="@" or str(origin_list[x])==">"):
            tem.append(cal2(origin_list[x],tem.pop(),tem.pop(),tem.pop()))
        else:
            tem.append(abs(tem.pop()))
print(tem[0])            
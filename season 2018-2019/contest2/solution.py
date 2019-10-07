#Robin Gan ACSL contest2 2019/1/20
def first_diff(str1,str2):
    str1,str2=str(str1),str(str2)
    list_str1,list_str2,common=str1.split(" "),str2.split(" "),""
    for i in range(len(list_str1)):
        for i2 in range(len(list_str2)):
            if(list_str1[i] in list_str2[i2]):
                common+=list_str1[i]
                list_str2[i2]=list_str2[i2].strip(list_str1[i])
    return common
def second_diff(list1,list2):
    list1,list2,common_string=str(list1),str(list2),""
    for i in range(len(list1)):
            if(list1[i] in list2):
                common_string+=list1[i]
                list2=list2[list2.index(list1[i])+1:len(list2)]
    return common_string
result=[]
string1=input()
result.append(string1)
string2=input()
result.append(string2)
string3=input()
result.append(string3)
string4=input()
result.append(string4)
string5=input()
result.append(string5)
string6=input()
result.append(string6)
string7=input()
result.append(string7)
string8=input()
result.append(string8)
string9=input()
result.append(string9)
string10=input()
result.append(string10)
for i in (0,2,4,6,8):
    print(second_diff(first_diff(result[i],result[i+1]),first_diff(result[i+1],result[i])))

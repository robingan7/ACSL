#This is ACSL 2018 ALl-Star Problem. This code is written by Robin Gan. And it is incompleted.
#more info check out acsl.org
#probelm name=Compressed_Tree
def main():
    global orgSet
    global editSet
    global targetWord
    global answerStr

    answerStr=""
    ipl=input()
    useWord=ipl[0:len(ipl)-1]
    targetWord=ipl[len(ipl)-1]
    orgSet=[]
    editSet=[]
    for char in useWord:
        orgSet.append(char)
        editSet.append(char)

def same_letter():
    global editSet
    global orgSet
    editSet=set(editSet)
    editSet=list(editSet)


def check():
    pass


def find_fre():
    global orgSet
    global editSet
    global testSet
    global numSet
    testSet=[]
    numSet=[]
    strSet=""
    for i4 in range(len(editSet)):
        numSet.append(orgSet.count(editSet[i4]))

    for i5 in range(len(editSet)):
        strSet=str(numSet[i5])+editSet[i5]
        testSet.append(strSet)
    testSet=sorted(testSet)
    return numSet

def list_edit(listtest):
    listtest=list(listtest)
    copy=listtest
    new_element=join(copy[0],copy[1])
    listtest.pop(0)
    listtest.pop(0)
    listtest.append(new_element)
    listtest=sorted(listtest)
    return listtest

def extract_number(str4):
    str4=str(str4)
    number=['1','2','3','4','5','6','7','8','9','0']
    finalStr=""
    for i10 in range(len(str4)):
        for i11 in range(len(number)):
            if str4[i10]==str(number[i11]):
                finalStr=finalStr+str4[i10]

    return finalStr

def extract_string(str4):
    str4=str(str4)
    if len(extract_number(str4))==1:
        str7=str4.replace(str4[0],"")
        return str7

    if len(extract_number(str4))==2:
        if extract_number(str4)[0]!=extract_number(str4)[1]:
            str7=str4.replace(str4[0],"")
            str8=str7.replace(str7[0],"")
            return str8
        if extract_number(str4)[0]==extract_number(str4)[1]:
            str7=str4.replace(str4[0],"")

            return str7

def join(element1,element2):

    str1=str(extract_string(element1))+str(extract_string(element2))
    str11=''
    for iii in range(len(str1)):
        str11=str11+str1[iii]

    str1=sorted(str1)
    str2=str(int(extract_number(element1))+int(extract_number(element2)))
    #print(extract_number(element1),extract_number(element2))
    return str2+str11

def sort_list():
    global copy2

    an=extract_string(copy2[0])

    numlist=extract_number(copy2[0])
    oo=[]
    oo2=""
    for ii1 in range(len(an)):
        oo.append(an[ii1])
    oo=sorted(oo)


    for ii2 in range(len(oo)):
        oo2=oo2+oo[ii2]

    return numlist+oo2

def position():
    global copy2
    global targetWord
    global answerStr

    if len(copy2)>1:
        for index in range(0,2):
            for index2 in range(len(copy2[index])):
                if copy2[index][index2]==targetWord:
                    if index==0:
                        answerStr=answerStr+'0'
                    if index==1:
                        answerStr=answerStr+'1'
    else:
        pass



def combine():
    global testSet
    global combined
    global numSet
    global copy2

    copy2=testSet
    while(len(copy2)>1):
        position()
        list_edit(copy2)
        copy2=list_edit(copy2)

        print(copy2)

    return sort_list()

main()
same_letter()
find_fre()
combine()
print(answerStr)

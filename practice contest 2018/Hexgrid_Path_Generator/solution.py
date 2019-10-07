ipl=[]
length=0
possibleway=0
ipl2=[]

def main():
    global ipl
    global secondCoord
    global firstCoord
    inp=input()
    length=len(ipl)
    for index in range(len(inp)):
        ipl.append(inp[index])
    firstCoord=ipl[0]+ipl[1]
    secondCoord=ipl[2]+ipl[3]
    ipl2.append(firstCoord)    

def close_function(letter,number):
    upNum=number+1
    downNum=number-1
    sameNum=number
    closeGird=[]
    if letter=='A':
        girdCoord='A'+str(upNum)
        closeGird.append(girdCoord)
        girdCoord2='A'+str(downNum)
        closeGird.append(girdCoord2)
        girdCoord3='B'+str(upNum)
        closeGird.append(girdCoord3)
        girdCoord5='B'+str(sameNum)
        closeGird.append(girdCoord5)
        
        
    elif letter=='Z':
        girdCoord='Z'+str(upNum)
        closeGird.append(girdCoord)
        girdCoord2='Z'+str(downNum)
        closeGird.append(girdCoord2)
        girdCoord3='Y'+str(upNum)
        closeGird.append(girdCoord4)
        girdCoord5='Y'+str(sameNum)
        closeGird.append(girdCoord5)
        
    
    elif ord(letter)%2==0 and letter!='A'and letter!='Z':
        letterNum=ord(letter)
        girdCoord=letter+str(upNum)
        closeGird.append(girdCoord)
        girdCoord2=letter+str(downNum)
        closeGird.append(girdCoord2)
        girdCoord3=chr(letterNum+1)+str(downNum)
        closeGird.append(girdCoord3)
        girdCoord4=chr(letterNum+1)+str(sameNum)
        closeGird.append(girdCoord4)
        girdCoord5=chr(letterNum-1)+str(sameNum)
        closeGird.append(girdCoord5)
        girdCoord6=chr(letterNum-1)+str(downNum)
        closeGird.append(girdCoord6)
        
        
    else:
        letterNum=ord(letter)
        girdCoord=letter+str(upNum)
        closeGird.append(girdCoord)
        girdCoord2=letter+str(downNum)
        closeGird.append(girdCoord2)
        girdCoord3=chr(letterNum+1)+str(upNum)
        closeGird.append(girdCoord3)
        girdCoord4=chr(letterNum+1)+str(sameNum)
        closeGird.append(girdCoord4)
        girdCoord5=chr(letterNum-1)+str(sameNum)
        closeGird.append(girdCoord5)
        girdCoord6=chr(letterNum-1)+str(upNum)
        closeGird.append(girdCoord6)
           
        for index in range(len(closeGird)):
            num=int(closeGird[index][1])
            if num<1 or num==0:
                closeGird[index]=""
            else: 
                pass 
          
        
    return closeGird        
         
def serperate(coord):
    var1=coord[0]
    var2=int(coord[1])
    print(var2)
    return close_function(var1,var2)


def list_choose(list1):
    for i2 in range(len(list1)):
        serperate(list1[i2])
        
        
def combine(list2):
    orig=[]
    for i4 in range(len(list2)):
        orig.extend(serperate(list2[i4]))
    return orig

def check(li1,li2):
    for i5 in range(len(li1)):
        if li1[i5] in li2:
            li2.remove(li1[i5])
    return li2        

def solve():
    global originalSet
    global ipl2
    global orgSet
    global firstCoord
    
    orgSet=[]
    orgSet.append(ipl2)
    originalSet=serperate(ipl[0:2])
    changingSet=originalSet
    orgSet.append(originalSet)
    for i4 in range(int(ipl[4])-1):
        comChanging=combine(changingSet)
        orgSet.append(comChanging)
        
        if orgSet.index(comChanging)>2:
            finalSet=check(orgSet[orgSet.index(comChanging)-2],comChanging)
        else:
            coordNum=comChanging.count(firstCoord)
            for i7 in range(coordNum):
                comChanging.remove(firstCoord)
            finalSet=comChanging
            
        changingSet=finalSet
        
    return orgSet[int(ipl[4])]    
        
def num_possible():
    global possibleway
    global secondCoord
    for i6 in range(len(solve())):
        if solve()[i6]==secondCoord:
            possibleway=possibleway+1
    return possibleway   
        

main()  
#print(ipl)
solve()
print(num_possible())
    
#print(solve())

#print(len(solve()))
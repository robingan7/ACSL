global r,c,s,n,letters,answer
inputlist=input().split(" ")
r,c,s,nf,letters,answer,letterlist,n,way=int(inputlist[0]),int(inputlist[1]),int(inputlist[2]),inputlist[4:len(inputlist)],["A","B","C","D","E"],"",[],[],""
if(s%c==0):
    way="start_right"
else:
    way="start_left"   
n=[int(x) for x in nf]
def getCol(inputnum):
    if inputnum%c==0:
        return inputnum//c
    else:
        return inputnum//c+1 
class Letter:
    def __init__(self,which_letter,start_point,which_way):
        self.le=which_letter
        self.sp=start_point
        self.way=which_way
        self.isf=False
        if self.le!="B":
            if self.way=="start_left":
                self.circle="1"
            else:
                self.circle="2"
        else:
            j=True
            for ele in [self.sp,self.sp+c,self.sp+2*c]:
                if(ele in n):
                    j=False
            if(j and getCol(self.sp+2*c)<=r):
                self.circle="1"
            else:
                self.circle="2"
    def getNextStartPoint(self):
        if self.way=="start_left":
            if self.le=="A":
                return int(self.sp+3)
            elif self.le=="B":
                if(self.circle=="1"):
                    return self.sp+2*c+1
                else:
                    return self.sp-2*c+1
            elif self.le=="C":
                return self.sp+c+1+1
            elif self.le=="D":
                return self.sp+2*c+1+1
            elif self.le=="E":
                return self.sp+c+3
            else:
                print("inavailable letter")
        elif self.way=="start_right":      
            if self.le=="A":
                return self.sp-3
            elif self.le=="B":
                if(self.circle=="1"):
                    return self.sp+2*c-1
                else:
                    return self.sp-2*c-1
            elif self.le=="C":
                return self.sp-c-1-1
            elif self.le=="D":
                return self.sp-2*c-1-1
            elif self.le=="E":
                return self.sp-c-3
            else:
                print("inavailable letter")
    def getRoundTile(self):
        if self.way=="start_left":
            if self.le=="A":
                return [self.sp,self.sp+1,self.sp+2]
            elif self.le=="B":
                if(self.circle=="1"):
                    return [self.sp,self.sp+c,self.sp+2*c]
                else:
                    return [self.sp,self.sp-c,self.sp-2*c]
            elif self.le=="C":
                return [self.sp,self.sp+c,self.sp+c+1]
            elif self.le=="D":
                return [self.sp,self.sp+1,self.sp+c+1,self.sp+2*c+1]
            elif self.le=="E":
                return [self.sp,self.sp+1,self.sp+c+1,self.sp+c+2]
            else:
                print("inavailable letter")
        elif self.way=="start_right":      
            if self.le=="A":
                return [self.sp,self.sp-1,self.sp-2]
            elif self.le=="B":
                if(self.circle=="1"):
                    return [self.sp,self.sp+c,self.sp+2*c]
                else:
                    return [self.sp,self.sp-c,self.sp-2*c]
            elif self.le=="C":
                return [self.sp,self.sp-1,self.sp-c-1]
            elif self.le=="D":
                return [self.sp,self.sp-c,self.sp-2*c,self.sp-2*c-1]
            elif self.le=="E":
                return [self.sp,self.sp-1,self.sp-c-1,self.sp-c-2]
            else:
                print("inavailable letter")
        else:
            print("inavailable tile")
    global x
    x=0
    def isLegal(self):
        global x
        x=x+1
        isLe=True
        if(self.way=="start_left"):
            if(self.getNextStartPoint()-1>=1 and getCol(self.getNextStartPoint()-1)==getCol(self.getNextStartPoint()-2)):
                pass
            else: 
                isLe=False
            if(((self.getNextStartPoint()-1)%c==0 and self.le=="B") or ((self.getNextStartPoint()-1)%c==0 and self.le=="D") or ((self.getNextStartPoint()-1)%c==1 and self.le=="B") or ((self.getNextStartPoint()-2)%c==1 and self.le=="C")):
                isLe=False
        else:
            if(self.getNextStartPoint()+1>=1 and getCol(self.getNextStartPoint()+1)==getCol(self.getNextStartPoint()+2)):
                pass
            else:
                
                isLe=False
            if(((self.getNextStartPoint()+1)%c==0 and self.le=="B") or ((self.getNextStartPoint()+1)%c==1 and self.le=="C") or ((self.getNextStartPoint()+1)%c==1 and self.le=="B")):
                
                isLe=False    
        for ele in self.getRoundTile():
            if((ele in n) or getCol(ele)<1 or getCol(ele)>r):
                isLe=False
        return isLe   
    
    def isFinish(self):
        if(self.way=="start_left"):
            if(getCol(self.getNextStartPoint()-1)==(self.getNextStartPoint()-1)//c):
                self.isf=True     
            return self.isf
        else:   
            if((self.getNextStartPoint()+1)%c)==1:
                self.isf=True     
            return self.isf    
fake=Letter("B",-100,"start_left")
letterlist.append(fake)
def putting_together(start_tile):
    global answer,letters,letterlist,way
    while(True):
        l1=Letter(letters[0],start_tile,way) 
        letters.pop(0)
        if(len(letters)==0):
            letters=["A","B","C","D","E"]
        if(l1.isLegal()): 
            count=0
            le1list=l1.getRoundTile()
            le2list=letterlist[len(letterlist)-1].getRoundTile()
            if(l1.way=="start_left"):
                for les in le1list:
                    if les-1 in le2list:
                        count=count+1
            else:
                for les in le1list:
                    if les+1 in le2list:
                        count=count+1
            if(count>1):
                pass
            else:
                break  
    if(l1.isFinish()):
        answer=answer+l1.le
        letterlist=[]
        return answer
    else:
        answer=answer+l1.le
        letterlist.append(l1)
        return putting_together(l1.getNextStartPoint())
print(putting_together(s))
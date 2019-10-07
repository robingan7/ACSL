def main():
    global originalNum
    global base
    ipl=input("Enter the input")
    originalNum=ipl[0:len(ipl)-3]
    base=ipl[len(ipl)-2:]


def ABCD(num):
    num=str(num)
    if(num=='1'):
        return '1'
    if(num=='2'):
        return '2'
    if(num=='3'):
        return '3'
    if(num=='4'):
        return '4'
    if(num=='5'):
        return '5'
    if(num=='6'):
        return '6'
    if(num=='7'):
        return '7'
    if(num=='8'):
        return '8'
    if(num=='9'):
        return '9'
    if(num=='A'):
        return '10'
    if(num=='B'):
        return '11'
    if(num=='C'):
        return '12'
    if(num=='D'):
        return '13'
    if(num=='E'):
        return '14'
    if(num=='F'):
        return '15'
    if(num=='0'):
        return '0'


def ABCD_reverse(num):
    num=int(num)
    if(num==1):
        return '1'
    if(num==2):
        return '2'
    if(num==3):
        return '3'
    if(num==4):
        return '4'
    if(num==5):
        return '5'
    if(num==6):
        return '6'
    if(num==7):
        return '7'
    if(num==8):
        return '8'
    if(num==9):
        return '9'
    if(num==10):
        return 'A'
    if(num==11):
        return 'B'
    if(num==12):
        return 'C'
    if(num==13):
        return 'D'
    if(num==14):
        return 'E'
    if(num==15):
        return 'F'
    if(num==0):
        return '0'


def edit(l):
    l=list(l)
    result=""
    for i5 in range(len(l)):
        result+=str(ABCD_reverse(l[i5]))
    return add_reverse(result)

def add(input_number):

    intbase=int(base)
    input_number=str(input_number)
    if(intbase==10):
        input_number=int(input_number)
        return input_number+int(add_reverse(str(input_number)))
    else:
        reverse=add_reverse(input_number)
        reduncy=[0]
        index=[]
        for i3 in range(len(input_number)):

            sum1=int(ABCD(input_number[i3]))+int(ABCD(reverse[i3]))

            if(sum1>(intbase-1)):
                sum1=sum1-intbase+reduncy[i3]

                index.append(sum1)
                reduncy.append(1)
            elif(sum1==(intbase-1)):
                sum1=sum1-intbase+reduncy[i3]
                if(sum1>=0):
                    index.append(sum1)
                    reduncy.append(1)
                else:
                    index.append(sum1++intbase-reduncy[i3])
                    reduncy.append(0)

            else:
                sum1=sum1+reduncy[i3]

                reduncy.append(0)
                index.append(sum1)

        if(reduncy[len(reduncy)-1]==1):
            index.append(1)

        return edit(index)

def add_reverse(input_string):
    input_string=str(input_string)
    reverse_str=""
    count=1
    for i in range(len(input_string)):
        reverse_str+=(input_string[len(input_string)-count])
        count+=1

    return reverse_str

def is_check(input_string):

    input_string=str(input_string)
    if(input_string[:int(len(input_string)/2)]==add_reverse(input_string[int(len(input_string)/2):])):
        return True
    elif(input_string[:(int(len(input_string)/2)+1)]==add_reverse(input_string[(int(len(input_string)/2)-0):])):
        return True
    else:

        return False

def execute():
    count=0
    intial_number=originalNum
    intial_number=str(intial_number)
    while(count<10 and is_check(intial_number)==False):

        intial_number=add(intial_number)

        is_check(intial_number)
        count+=1

    if(is_check(intial_number)):
        return intial_number
    else:
        return 'None,'+str(intial_number)

main()
print(execute())

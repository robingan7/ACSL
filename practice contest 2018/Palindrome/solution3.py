def main():
    global originalNum
    global base
    ipl=input("Enter the input")
    originalNum=ipl[0:len(ipl)-3]
    base=ipl[len(ipl)-2:]


def ABCD(num):
    num=str(num)
    if(num=='A'):
        return 10
    if(num=='B'):
        return 11
    if(num=='C'):
        return 12
    if(num=='D'):
        return 13
    if(num=='E'):
        return 14
    if(num=='F'):
        return 15

def add(input_number):
    intbase=int(base)
    input_number=str(input_number)
    if(intbase==10):
        input_number=int(input_number)
        return input_number+int(add_reverse(str(input_number)))
    if(intbase==16):
        addition=0
        exponent=0
        for i in range(len(input_number)):
            addition+=pow(11,exponent)*1




def convert_add(system,cal_base):

    cal_base=int(cal_base)
    rawint=int(system)
    numlist=[]
    result=""
    if(cal_base==11):
        for i in range(len(system)):
            left=system/11
            remind=system%11
            numlist.append(remind)
            system=left

        for i2 in range(len(numlist)):
            numlist.reverse()
            result+=numlist[i2]

    return result


def add_reverse(input_string):
    input_string=str(input_string)
    reverse_str=""
    count=1
    for i in range(len(input_string)):
        reverse_str+=(input_string[len(input_string)-count])
        count+=1

    return reverse_str

main()
print(add(originalNum))

#9103 2018-2019 contest1
#by Robin Gan

def main():
   global original_number
   global length
   ipl=ipl2
   breakpoint=0
   for i in range(len(ipl)):
       if(ipl[i]==" "):
           breakpoint=i

   original_number=ipl[0:breakpoint]
   length=ipl[breakpoint+1:len(ipl)]

def group():
   global result_list
   global length
   global original_number
   length=int(length)
   count=0
   result_list=[]
   if(original_number[0]!="-"):
       if(len(original_number)%length==0):
           for i2 in range(int(len(original_number)/length)):
               result_list.append(original_number[count:count+length])
               count=count+length
       else:
           for i3 in range(int(len(original_number)/length)):
               result_list.append(original_number[count:count+length])
               count=count+length
           reminder=original_number[len(original_number)-len(original_number)%length:len(original_number)]

           for i4 in range(length-len(original_number)%length):
               reminder=reminder+"0"
           result_list.append(reminder)

   else:
       original_number = original_number[1:len(original_number)]
       if(len(original_number)%length==0):
           for i2 in range(int(len(original_number)/length)):
               result_list.append(original_number[count:count+length])
               count=count+length
               result_list[0]="-"+result_list[0]
           print(result_list)
       else:
           for i3 in range(int(len(original_number)/length)):
               result_list.append(original_number[count:count+length])
               count=count+length
           reminder=original_number[len(original_number)-len(original_number)%length:len(original_number)]

           for i4 in range(length-len(original_number)%length):
               reminder=reminder+"0"
           result_list.append(reminder)
           result_list[0]="-"+result_list[0]
           print(result_list)


def add():
   global result_list
   sum1=0
   for i5 in range(len(result_list)):
       sum1=sum1+int(result_list[i5])
   print(sum1)


global ipl2
content=open("contest1sampledata.txt","r")
lines=content.readlines()
for line in lines:
    ipl2=line
    main()
    group()
    add()

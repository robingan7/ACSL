#This is skyscrapper 
#this is only for four not five
def main4():
    ipl=input("Enter a input")
    global all_list
    global top_bottom
    global sides
    top_bottom=[ipl[0]+ipl[len(ipl)-4],ipl[1]+ipl[len(ipl)-3],ipl[2]+ipl[len(ipl)-2],ipl[3]+ipl[len(ipl)-1]]
    
    sides=[ipl[5:7],ipl[8:10],ipl[11:13],ipl[14:16]]
    
   
    all_list=[]
    for lay1 in range(1,5):
        for lay2 in range(1,5):
            for lay3 in range(1,5):
                for lay4 in range(1,5):
                    if(str(lay1)!=str(lay2) and str(lay1)!=str(lay3) and str(lay1)!=str(lay4) and str(lay2)!=str(lay3) and str(lay2)!=str(lay4) and str(lay3)!=str(lay4)):
                        layer=str(lay1)+str(lay2)+str(lay3)+str(lay4)
                        all_list.append(layer)
                    else: pass    
 
def none():
    pass

def reverse(input_string):
    input_string=str(input_string)
    reverse_str=""
    count=1
    for i in range(len(input_string)):
        reverse_str+=(input_string[len(input_string)-count])
        count+=1

    return reverse_str

def single_check4(point,select_row):
    point=str(point)
    select_row=str(select_row)
    if(point=="1" and select_row[0]=="4"):
        return True
    elif(point=="4" and select_row=="1234"):
        return True
    elif(point=="2" and select_row[0]=="3"):
        return True
    elif(point=="2" and select_row[1]=="4"):
        return True
    elif(point=="2" and select_row=="2143"):
        return True
    elif(point=="3" and select_row[3]!="4" and int(select_row[2])>int(select_row[1]) and int(select_row[1])>int(select_row[0])):
        return True
    elif(point=="3" and select_row[3]=="4" and select_row[1]=="3"):
        return True
    elif(point=="3" and select_row=="2134"):
        return True
    else: return False
 
      
def double_check4(coord, select_row2):
    coord=str(coord)
    select_row2=str(select_row2)
    if(single_check4(coord[0],select_row2) and single_check4(coord[1],reverse(select_row2))):
        return True
    else: return False

def make_vertical(input_list):
    input_list=list(input_list)
    first_pai=""
    second_pai=""
    third_pai=""
    four_pai=""
    for i in range(len(input_list[0])):
        first_pai+=input_list[i][0]
    for i in range(len(input_list[0])):
        second_pai+=input_list[i][1]
    for i in range(len(input_list[0])):
        third_pai+=input_list[i][2]
    for i in range(len(input_list[0])):
        four_pai+=input_list[i][3]
    result=[first_pai,second_pai,third_pai,four_pai]
    return result
    
def hasSame4(input_string):
    input_string=str(input_string)
    if('1' in input_string and '2' in input_string and '3' in input_string and '4' in input_string):
        return True
    else: False
        

def execute4():
    possible1=[]
    possible2=[]
    possible3=[]
    possible4=[]
    one_row_possible=[]
    final_possible=[]
    all_vertical=[]

    for i2 in range(len(all_list)):
        if(double_check4(sides[0],all_list[i2])):
            possible1.append(all_list[i2])
    for i2 in range(len(all_list)):
        if(double_check4(sides[1],all_list[i2])):
            possible2.append(all_list[i2])        
    for i2 in range(len(all_list)):
        if(double_check4(sides[2],all_list[i2])):
            possible3.append(all_list[i2])
    for i2 in range(len(all_list)):
        if(double_check4(sides[3],all_list[i2])):
            possible4.append(all_list[i2])   
    
    for index1 in range(len(possible1)):
        for index2 in range(len(possible2)):
            for index3 in range(len(possible3)):
                for index4 in range(len(possible4)):
                    one_row_possible.append(possible1[index1])
                    one_row_possible.append(possible2[index2])
                    one_row_possible.append(possible3[index3])
                    one_row_possible.append(possible4[index4])
                    final_possible.append(one_row_possible)
                    one_row_possible=[]
    
    for index2 in range(len(final_possible)):
        all_vertical.append(make_vertical(final_possible[index2]))
    result_num=[]
    for index3 in range(len(final_possible)):
        if(double_check4(top_bottom[0],all_vertical[index3][0]) and double_check4(top_bottom[1],all_vertical[index3][1]) and double_check4(top_bottom[2],all_vertical[index3][2]) and double_check4(top_bottom[3],all_vertical[index3][3])):
            if(hasSame4(all_vertical[index3][0]) and hasSame4(all_vertical[index3][1]) and hasSame4(all_vertical[index3][2]) and hasSame4(all_vertical[index3][3])):
                result_num.append(index3)
    print(final_possible[result_num[0]])
    
main4()
execute4()
    

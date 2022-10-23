input_number=int(input())
total_number=0
while(input_number>0):
    digits=input_number%10
    #print("digits:",digits)
    total_number=total_number+digits
    #print("total_number:",total_number)
    input_number=input_number//10
    #print("input_number:",input_number)
print("total_number:",total_number)
#if len(str(total_number))>1:
    #print("total_number:",(total_number+digits)-1)
    #print("total_number:",digits*len(str(total_number)))
# the black notebook is our handwriting

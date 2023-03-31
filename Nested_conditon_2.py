x=45
is_x_greater = x>30
is_x_both_greater = x>50
if is_x_greater:
    print("X is Greater than 30")
    if is_x_both_greater:
        print("X is Greater than 50")
result==>> 
case_1==>> 
X is Greater than 30
case_2==>> 
X is Greater than 30
X is Greater than 50


R=7
is_R_less_3 = R<=3
is_R_less_10 = R<=10

if is_R_less_3:
    print("One of Top 3")
elif is_R_less_10:
    print("Not Top 3 but One of Top 10")
else:
    print("Not Top 3 but One of Top 10")


result==>> 
One of Top 3



w = 60
is_w_great_100 = w>=100
is_w_not_great_100 = w<100 or w>=30

if is_w_great_100:
    print("Box is Heavier")
elif is_w_not_great_100:
    print("Box is Heavy")
else:
    print("Box is Heavy")

result==>> 
Box is Heavy



H = "Y"
I = "N"
is_H_equal = H == "Y"
is_I_equal = I == "Y"

if is_H_equal:
    print("Allowed to Exam - Has Hall ticket")
elif is_I_equal:
    print("Allowed to Exam - Has Identification Card")
else:
    rint("Allowed to Exam - Has Identification Card")

result==>> 
Allowed to Exam - Has Hall ticket




a=1634
sum = 0
for i in a:
    s=int(i)**4
    sum += s

if sum == int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

    
Result==>>  Armstrong Number
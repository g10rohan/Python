# 21.	Write a C program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
unit=int(input("Enter Unit:-"))
if unit<=50:
    charge=unit*0.50;
    print("Charge:-", charge);
elif unit>=51 and unit<=150:
    temp=(unit-50);
    charge=temp*0.75+50*0.50;
    print("Charge:-",charge);
elif unit>=151 and unit<=250:
    temp=(unit-150);
    charge=temp*1.20+50*0.50+100*0.75;
    print("Charge:-", charge);
elif unit>=251:
    temp=(unit-250);
    charge=temp*1.50+100*1.20+50*0.50+100*0.75;
    charge=charge+charge*0.20;
    print("Charge:-", charge);

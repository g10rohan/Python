# # 17. Write a Python program to remove duplicates from Dictionary.
d1={1:1,2:2,3:3,4:4,5:4,6:4}
d2={}
for k,v in d1.items():
    if v not in d2.values():
        d2[k]=v;
print(d2);

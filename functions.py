def cal_avg(a,b,c):
    sum= a+b+c
    avg= sum/3
    print(avg)
    return(avg)

q= int(input("Give us your marks in sst: "))
w= int(input("Give us your marks in eng: "))
e= int(input("Give us your marks in pbi: "))

cal_avg(q,w,e)

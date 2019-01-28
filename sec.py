#name =himanshu akolkar
#div=p
#batch=b1
'''to convert the sec in to days ,hour, min, sec'''
x=int(input('enter the no of sec  '))
q1=x//86400
r1=x%86400
q2=r1//3600
r2=r1%3600
q3=r2//60
r3=r2%60
print('no of days',q1,'no of hour',q2,'no of min',q3,'no of sec',r3  )





def fibon(m):
 a=[]

 if (m > 0):
  if (m == 1):
      a.append(0)
      print(a)
  elif (m == 2):
    a.append(0 , 1)
    print(a)
  else:
     a.append(0 , 1)
     while (m> len(a)):
        num=0
        num= a[(len(a)-2)]+a[(len(a)-1)]
        a.append(num)
        print(a)

 else:
    print("you most enter positve number")
    
    m=int(input("enter the num"))
    fibon(m)
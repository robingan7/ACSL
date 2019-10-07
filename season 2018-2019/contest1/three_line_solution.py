for line in open("/Users/robingan7/Desktop/Programs/ACSL/contest1sampledata.txt","r").readlines():
    x=line
    y,z=x.split(' ')[0],int(x.split(' ')[1])
    n=y+"0"*(z-len(y)%z)
    print(sum([int(n[i*z:(i+1)*z]) for i in range(len(n)//z)]))

import numpy as np
from numpy import linalg as LA
from numpy.linalg import matrix_power

def expMethod(M):
    Yi=np.ones(3)*1/(3)**1/2
    Zk=M.dot(Yi)
    print("X_0", Yi)
    # print(Zk)
    MaxEigenI=0
    MaxEigenINext=abs(Zk[0]/Yi[0])
    YiNext=Zk/LA.norm(Zk)
    print("Myu", MaxEigenINext)
    print("X_ 1", YiNext)
    n=1
    while(abs(MaxEigenI-MaxEigenINext)>10**-4):
        Yi=YiNext
        Zk=M.dot(YiNext)
        MaxEigenI=MaxEigenINext
        MaxEigenINext=abs(Zk[0]/Yi[0])
        print("Myu", MaxEigenINext)
        YiNext=Zk/LA.norm(Zk)
        print("X_",n+1,"->", YiNext)
        n+=1
    EigenVector=YiNext/MaxEigenINext #Власний вектор з точністю до константи множення
    print("The end!")
    return MaxEigenINext,EigenVector,n

def Inverse(M):
    l=len(M[0])
    Temp=np.zeros((l,2*l))
    for i in range(l):
        for j in range(l):
            Temp[i,j]=M[i][j]
    for i in range(l):
        Temp[i,i+l]=1
    #Прямий хід
    for j in range(l):
        if(Temp[j][j]!=0):
            for i in range(j+1,l):
                Temp[i]=Temp[i]-Temp[j]*Temp[i][j]/Temp[j][j]
    #Обернений хід
    for j in range(l):
        Temp[j]=Temp[j]/Temp[j][j]
    for j in range(l-1,0,-1):
        mult=Temp[j]
        for i in range(j-1,-1,-1):
            Temp[i]=Temp[i]-Temp[i][j]*mult
    for i in range(l):
        for j in range(2*l):
            Temp[i,j]=round(Temp[i][j],3)
    Res=np.empty((l,l))
    for i in range(l):
        for j in range(l):
            Res[i,j]=Temp[i][l+j]
    return Res
    

#Степеневий метод з точністю epsillon=10^-4 знайти максимальне та мінімальне за модулем власні значення та власні вектори
#A=np.array([[5.18+1.5,1.12,0.95,1.32,0.83],[1.12,4.28-1.5,2.12,0.57,0.91],[0.95,2.12,6.13+1.5,1.29,1.57],[1.32,0.57,1.29,4.57-1.5,1.25],[0.83,0.91,1.57,1.25,5.21+1.5]])
A = np.array([[1.,0.5, 1./3],[0.5,1./3,0.25],[1./3,0.25,0.2]])
MaxEv,EigVec,r=expMethod(A)#отримаємо максимальне за модулем власне значення та його вектор
inv=Inverse(A)
MaxEv1,EigVecM,n=expMethod(inv)#максимальне для оберненої матриці та кількість ітерацій
MinEv=1/MaxEv1#мінімальне за модулем власне значення
Yi=np.ones(3)*1/(3)**1/2
EigVecM=matrix_power(inv,n).dot(Yi)
# print(MaxEv,EigVec)
# print(MinEv,EigVecM/LA.norm(EigVecM))
print('Max:', MaxEv,' Min:', MinEv)


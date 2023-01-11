import numpy as np
import math
from normal_reader import read_matrix
import csv
import pandas as pd


def parametre():
    P=[]
    with open('parametre.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            P.append(row[0])
    return P


#VIF Variance influence facteur , VIF doit il etre toujours positif ?
def VIF(N):
    Q=np.linalg.inv(N)
    V=[]
    for i in range(len(N)):
        Vi=N[i][i]*Q[i][i]
        V.append(Vi)
    return V


def cos_teta(V):
    cos_teta=[]
    for i in range(len(N)):
        if (1/(V[i])>1):
            cos_teta.append("Error")
            print("il y a une erreur")
        else:
            cos_teta.append(math.sqrt(1-(1/(V[i]))))
    return cos_teta


def teta(T):
    teta=[]
    for i in range(len(T)):
        if (T[i]<1):
            teta.append(math.degrees(math.acos(T[i])))
        else:
            teta.append(None)
    return teta


def coefficient_de_determination(V):
    R_2=[]
    for i in range(len(N)):
        R_2.append((1-(1/(V[i]))))
    return R_2
    

def compteur_multicolinearite(V):
    compt1_5=0
    compt5_10=0
    compt_sup=0

    for i in range(len(V)):
        if(V[i]<5):
            compt1_5+=1
        elif(V[i]>5 and V[i]<10):
            compt5_10+=1
        else:
            compt_sup+=1
    L=[]
    L.append(compt5_10)
    L.append(compt_sup)

    return L

def tolerance(R):
    Tol=[]
    for i in range(len(R)):
        Tol.append(1-R[i])
    return Tol
            






if __name__ == "__main__":

    N=read_matrix()

    Q=np.linalg.inv(N)
    
    V=VIF(N)
    
    T=cos_teta(V)
    
    Teta=teta(T)
    
    R_2=coefficient_de_determination(V)
    
    P=parametre()
    
    Mylist=[]
    
    c=0
    
    for i in range(len(V)):
        liste=[P[i],V[i],T[i],R_2[i],Teta[i]]
        Mylist.append(liste)
    
    df=pd.DataFrame(Mylist)
    
    df.rename(columns={0:"Parametre",1:"VIF",2:"cos_teta",3:"R_2",4:"Teta"},inplace=True)
    # print("La matrice normale est N \n")
    # print(N)
    # print("\n")
    # print("La matrice covariance, l'inverse de N est Q \n")
    # print(Q)
    # print("\n")
    # print("Le VIF pour chaque parametre \n")
    # print(V)
    print("\n")
    print("La plus grand valeur du VIF est ")
    print(max(V))
    print("La plus petite valeur du VIF est ")
    print(min(V))
    print("\n")
    # print("Le VIF versio  pourcentage avec cos teta qui est egale à R \n ")
    # print(T)
    # print("\n")
    print("La plus grand valeur du cos teta est ")
    print(max(T))
    print("La plus petite valeur du cos teta est ")
    print(min(T))
    # print("Le coefficient de determination R_carre \n")
    # print(R_2)
    
    
    df.to_csv('Students.csv', sep =';')


    comp=compteur_multicolinearite(V)

    dfVIFcomp=pd.DataFrame(comp)
    df.to_csv('compteur.csv', sep =';')
    
    
    





    
    
    
    


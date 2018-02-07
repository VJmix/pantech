# 0. import the needed packages
import numpy as np
import pandas as pd
from numpy import genfromtxt
import matplotlib.pyplot as plt
import re

# 1. Read the data points
my_data = pd.read_csv('data.csv', sep=',',header=0)
cleaned_data = np.array([ my_data['length'].tolist(),my_data['width'].tolist()]).T

print( my_data )
print( cleaned_data ) 
print( "::::::::::::::::::" )
def check_Classified(Cl,D):
    kk=0;
    for j in range(Db_Val):
        if Cl[j]==D[j]:
            kk=kk+1;
        return kk;


def Calculate_Weight(Neeta,D,Y,W,X,i):
    D=np.array(D);
    D=D.astype(float);
    Y=np.array(Y);
    Y=Y.astype(float);
    print( "###" )
    print( W )
    Wn=W+Neeta*(D[i]-Y)*X;

    return(Wn)
    
kk=0;   
X0=1;
X1=my_data['length'];
X2=my_data['width'];
X1=np.array(X1);
X1=X1.astype(float);
X2=np.array(X2);
X2=X2.astype(float);
Cl=my_data['Class'];
Cl=np.array(Cl);
Cl=Cl.astype(float);
Db_Val= len(Cl);
D=MeanG1=np.zeros((4,), dtype=np.float);
w0=1;
w1=1;
w2=1;
W=[w0,w1,w2]
W=np.array(W);
W=W.astype(float);
##Region of classifiation in average detection
MeanG1=np.zeros((2,), dtype=np.float);
MeanG2=np.zeros((2,), dtype=np.float);
GainMean=np.zeros((2,), dtype=np.float);
groups = my_data.groupby('Class')
GroupNo=len(groups);
Grp_avail1=groups.get_group(1);
Grp_avail2=groups.get_group(2);
for j in range(GroupNo):
    Grp_avail=groups.get_group(j+1);
    G1=Grp_avail['length'];
    G2=Grp_avail['width'];
    MeanG1[j]=np.mean(G1);
    MeanG2[j]=np.mean(G2);


GainMean[0]=np.mean(MeanG1);
GainMean[1]=np.mean(MeanG2);  
print( GainMean )

print( "####################" )

##Data Traning starting here
x0=X0;
val=1;
while kk<4:
    for i in range(Db_Val):
        x1=X1[i];
        x2=X2[i];
        Cls_Val=Cl[i];
        X=[x0,x1,x2];
        X=np.array(X);
        X=X.astype(float);
        Sum_Val=X[0]*W[0]+X[1]*W[1]+X[2]*W[2];
    ##thresholding
        if Sum_Val>=0:
            print( "class1" )
            D[i]=1;
            if Cls_Val!=D[i]:
                Y=i+1;
                print( "Calculate weightage" )
                Neeta=.1;
                W=Calculate_Weight(Neeta,D,Y,W,X,i)
                print( W )
                kk=check_Classified(Cl,D)
                print( kk )
        else:
            print( "class2" )
            D[i]=2;
            if Cls_Val!=D[i]:
                Y=i+1;
                print( "Calculate weightage" )
                Neeta=.1;
                W=Calculate_Weight(Neeta,D,Y,W,X,i)
                print( W )
                kk=check_Classified(Cl,D)
                print( kk )







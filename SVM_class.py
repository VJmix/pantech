from sklearn import svm
x=[[0.,0.],[1.,1.]];
y=[0,0];

clf = svm.SVC()

clf.fit(x,y);
##Testing
Predict_OP=clf.predict([[2., 2.], [-1., -2.]])
print (Predict_OP)

from sklearn.neural_network import MLPClassifier
x=[[0.,0.],[1.,1.]];
y=[0,1];
##Defining
clf=MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=1);
##Training
clf.fit(x,y)
##Testing
Predict_OP=clf.predict([[2., 2.], [-1., -2.]])
print Predict_OP

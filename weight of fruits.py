

import unittest
from main import *



from sklearn import tree

features=[[120 ],[160],[30]]
labels=["apple","banana","grapes"]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
s=int(input("weight >"))

print (clf.predict([[s]]))
	

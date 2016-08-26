clf=tree.DecisionTreeClassifier()

clf.fit(features_train, labels_train)

result = clf.predict(features_test)

acc = sum(map(lambda x,y:x==y,result,labels_test))/float(len(labels_test))
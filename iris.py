class Iris():

    def iris_run(self,n1,n2,n3,n4):
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression

        iris = pd.read_csv('python/Machine_Learning/CSV_Files/Iris.csv')

        X = iris.drop('species',axis = 1)
        y = iris.species

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.5)

        lr = LogisticRegression()

        lr.fit(X_train,y_train)

        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4


        self.predict = lr.predict([[self.n1,self.n2,self.n3,self.n4]])
        self.predict = np.array2string(self.predict)
        self.predict = self.predict[2:-2]
        return self.predict
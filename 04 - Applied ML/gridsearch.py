import findspark
findspark.init()

import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#from spark_sklearn import GridSearchCV
from splearn.grid_search import SparkGridSearchCV
from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("App")
conf.setMaster("yarn")
conf.set('spark.executor.memory', '40G')
conf.set('spark.driver.memory', '45G')
conf.set('spark.driver.maxResultSize', '10G')

sc = SparkContext(conf=conf)





newgroup = fetch_20newsgroups()
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(newgroup.data)# vectorise
X_train, X_test, y_train, y_test = train_test_split(vectors, newgroup.target, test_size=0.1, random_state=1)

print(X_train.shape)

X_rdd = sc.parallelize(X_train.toarray())
y_rdd = sc.parallelize(y_train)
Z = DictRDD((X_rdd, y_rdd),
            columns=('X', 'y'),
            dtype=[np.ndarray, np.ndarray])

param_grid =   {'n_estimators': np.arange(145, 155,5), #todo a agrandir !!!
              'max_depth': np.arange(30, 36,3)
               }
clf = RandomForestClassifier()
grid_search = SparkGridSearchCV(clf, param_grid=param_grid,n_jobs=-1,cv=3)
param = grid_search.fit(Z)

print(grid_search.best_params_)
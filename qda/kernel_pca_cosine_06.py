
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Datasets/diabetes_1.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values




from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:8])
X[:, 1:8] = imputer.transform(X[:, 1:8])


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.6, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



from sklearn.decomposition import KernelPCA
kpca = KernelPCA(kernel ='cosine', gamma = 15)
X_train = kpca.fit_transform(X_train, y_train)
X_test = kpca.transform(X_test)

#QDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
classifier = QuadraticDiscriminantAnalysis()
classifier.fit(X_train, y_train)

y_pred=classifier.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)


from sklearn.metrics import classification_report


print(classification_report(y_test, y_pred))

# True Positive (TP): we predict a label of 1 (positive), and the true label is 1.
tp = np.sum(np.logical_and(y_test == 1, y_pred == 1))
 
# True Negative (TN): we predict a label of 0 (negative), and the true label is 0.
tn = np.sum(np.logical_and(y_test == 0, y_pred == 0))
 
# False Positive (FP): we predict a label of 1 (positive), but the true label is 0.
fp = np.sum(np.logical_and(y_test == 1, y_pred == 0))
 
# False Negative (FN): we predict a label of 0 (negative), but the true label is 1.
fn = np.sum(np.logical_and(y_test == 0, y_pred== 1))

# Sensitivity, hit rate, recall, or true positive rate
tpr = tp/(tp+fn)
# Specificity or true negative rate
tnr = tn/(tn+fp) 
# Precision or positive predictive value
ppv = tp/(tp+fp)
# Negative predictive value
npv = tn/(tn+fn)
# Fall out or false positive rate
fpr = fp/(fp+tn)
# False negative rate
fnr = fn/(tp+fn)
# False discovery rate
fdr = fp/(tp+fp)

# Overall accuracy
acc = (tp+tn)/(tp+fp+fn+tn)

if tp>0:
  precision=float(tp)/(tp+fp)
  recall=float(tp)/(tp+fn)
  
print ('\n confussion matrix for Logistic Regression Classifier:\n',confusion_matrix(y_test,  y_pred))
print('\nTrue Positive : %d'%(tp))
print('\nTrue Negative : %d'%(tn))
print('\nFalse Positive : %d'%(fp))
print('\nFalse Negative : %d'%(fn))
print('\nSensitivity, hit rate, recall, or true positive rate : %f' %(tpr))
print('\nSpecificity or true negative rate : %f' %(tnr))
print('\nPrecision or positive predictive value : %f' %(ppv))
print('\nNegative predictive value : %f'%(npv))
print('\nFall out or false positive rate: %f' %(fpr))
print('\nFalse negative rate : %f' %(fnr))
print('\nFalse discovery rate : %f' %(fdr))
print('\nPrecision : %f' %(fnr))
print('\nRecall : %f' %(fdr))
print('\nOverall accuracy for Classifier : %f' %(acc))


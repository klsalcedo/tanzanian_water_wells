from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import plot_confusion_matrix, confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplt as plt

def class_model(model, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=10)
    #do something to normalize/scale data here
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    #use classification model instead
    print('Precision Score:', precision_score(y_test, y_pred))
    print('Accuracy Score:', accuracy_score(y_test, y_pred))
    print('Recall Score:', recall_score(y_test, y_pred))
    print('F1 Score:', f1_score(y_test, y_pred))
    
    #wont work for all models - use if statement or delete
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(false_positve_rate, true_positive_rate)
    print('AUC:', round(roc_auc,2))
    
    #plot seperate confusion matrices for train and test sets -- this outputs both sets together
    print('Confusion Matrix:')
    plot_confusion_matrix(model, X, y, cmap=plt.cm.Blues)
    plt.show()
    
    return model
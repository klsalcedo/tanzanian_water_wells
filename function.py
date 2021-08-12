from sklearn.metrics import accuracy_score, plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt

def class_model(model, X_train, X_test, y_train, y_test):
    
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    print('Classification report for training data:')
    print(classification_report(y_train, y_pred_train))
          
    print('Classification report for testing data:')
    print(classification_report(y_test, y_pred_test))
    
    print('Confusion Matrix Train:')
    plot_confusion_matrix(model, X_train, y_train, cmap=plt.cm.Blues)
    plt.show()
    
    print('Confusion Matrix Test:')
    plot_confusion_matrix(model, X_test, y_test, cmap=plt.cm.Blues)
    plt.show()
    
    return model

#     wont work for all models - use if statement or delete
#     false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
#     roc_auc = auc(false_positve_rate, true_positive_rate)
#     print('AUC:', round(roc_auc,2))
    
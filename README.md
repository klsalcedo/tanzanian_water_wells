# Classifying Water Wells - Tanzania 
Author: Katarina Salcedo

## Motivation
To aid The Water Project in their goal of providing clean water to regions of Africa. I will create a classification model that is accurately able to predict whether a water well is functional or nonfunctional. The Water Project can use this model to decide where to build new wells, if a well needs maintenance and also help them prioritize regions that are in greater need of a water source. 

## Data
The data is sourced from Taarifa and the Tanzanian Ministry of Water. It contains around 59,000 rows and 40 independent variables describing the well's geographical location, funder, management, surrounding population, quantity and quality of water, extraction type, water source, if payment is required, etc. The target variable describes the status of the well as either 'functional', 'non functional' or 'functional needs repair'. 

## Methodology
Before running any models, each independent variable was checked to ensure there was good separability amoung the three different classifications. Variables that scowed good separability were used in the classificaton model and variables that showed little to no separability were dropped. Pandas get_dummies function was used on the categorical variables and class imbalance was also checked. After cleaning the data and selecting useful independent variables, four vanilla models were run. These include: Logistic Regression, Decision Tree Classifier, Random Forest Classifier and Gradient Boosting. Of these four, the two models with the best evaluation metrics - Decision Tree and Random Forest Classifier - were choosen for further hyperparameter tuning using GridSearch. 

## Results 
Out of the Decision Tree and Random Forest Classifier, the latter had the best metrics. I was able to get this model up to 85% accuracy in the test set (94% for train set). Below is the classifiaction report of the final model: 

![Screen Shot 2021-08-16 at 5 08 05 PM](https://user-images.githubusercontent.com/81720110/129644130-4e3c2817-495d-462a-9861-2a056b58502a.png)

![Screen Shot 2021-08-16 at 5 08 24 PM](https://user-images.githubusercontent.com/81720110/129644142-f94f6d91-7e0c-49dc-99cb-98ca93f3ca05.png)
![Screen Shot 2021-08-16 at 5 08 42 PM](https://user-images.githubusercontent.com/81720110/129644147-d5100644-8083-4872-8cc9-cf5763565898.png)

## Conclusions
This model is able to predict water well functionality with 85% accuracy. The most important features affecting this classification are: quanity, payment, waterpoint type and extraction type

## Next Steps
Future work would be to futher increase accuracy score, find a better way to deal with class imbalance in the 'functional needs repair' class, and using alternate methods to deal with missing values in dataset.  

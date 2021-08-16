# Classifying Water Wells - Tanzania 
Author: Katarina Salcedo

## Motivation
To aid The Water Project in their goal of providing clean water to regions of Africa. I will create a classification model that is accurately able to predict whether a water well is functional or nonfunctional. The Water Project can use this model to decide where to build new wells, if a well needs maintenance and also help them prioritize regions that are in greater need of a water source. 

## Data
The data is sourced from Taarifa and the Tanzanian Ministry of Water. It contains around 59,000 rows and 40 independent variables describing the well's geographical location, funder, management, surrounding population, quantity and quality of water, extraction type, water source, if payment is required, etc. The target variable describes the status of the well as either 'functional', 'non functional' or 'functional needs repair'. 

## Methodology
Before running any models, each independent variable was checked to ensure there was good separability amoung the three different classifications. Variables that scowed good separability were used in the classificaton model and variables that showed little to no separability were dropped. Pandas get_dummies function was used on the categorical variables and class imbalance was also checked. After cleaning the data and selecting useful independent variables, four vanilla models were run. These include: Logistic Regression, Decision Tree Classifier, Random Forest Classifier and Gradient Boosting. Of these four, the two models with the best evaluation metrics - Decision Tree and Random Forest Classifier - were choosen for further hyperparameter tuning using GridSearch. 

## Results 
Out of the Decision Tree and Random Forest Classifier, the latter had the best metrics. I was able to get this model up to 85% accuracy in the test set (% for train set). Below is the classifiaction report of the final model: 

## Conclusions
This model is able to predict water well functionality with --% accuracy. The most important features affecting this classification are: 

## Next Steps
Future work would be to futher increase accuracy score, find a better way to deal with class imbalance in the 'functional needs repair' class, and using alternate methods to deal with missing values in dataset.  

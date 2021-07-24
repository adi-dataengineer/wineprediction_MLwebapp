# wineprediction_MLwebapp


Wine Quality Prediction Machine Learning webapp – Created from scratch and hosted on GCP, under 4hrs!
Model creation steps followed:
1.	Data set – winedatset from sklearn 
2.	Pre-Processed data 
3.	Created a pipe for scaling and implementing SVC Kernel 
4.	Used grid search to obtain optimal values of model hyperparameters 
5.	Trained the model and to achieve an accuracy of 95%
Webapp creation steps followed:
1.	Serialized the model using pickle
2.	Deployed the serialized model as a web application using Flask
3.	Tested the app - Pytest
4.	Finally, Hosted the web application on GCP App engine
5.	Done!

## Project description

Banks have a lot of information about one's credit history, monthly income and other material. From the previous cases, banks make mathematical based assumptions if person is capable of handling credit for money X which need to be repaid in Y years

**Main task: predict probability if person who is willing to get a credit will be able to repay it.** 

* Based on Kaggle competition [Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk/data)
* Metric used: area under curve (AUC)
* Contains 2.5 GB of CSV files
* Expected Kaggle result: 0.786

CSV files connections

![](https://raw.githubusercontent.com/TuringCollegeSubmissions/okuzmi-DS.3.4/master/pics/tree.png?token=AQ5OZ6ANU4RJOEFRCJOTXOLAOBJSO)

## Approach steps

1. [Merging CSV files](https://github.com/TuringCollegeSubmissions/okuzmi-DS.3.4/blob/master/notebooks/project%201%20intro.ipynb)
2. [EDA](https://github.com/TuringCollegeSubmissions/okuzmi-DS.3.4/blob/master/notebooks/project%202%20eda.ipynb)
3. [Preprocessing (data cleaning, feature engineering)](https://github.com/TuringCollegeSubmissions/okuzmi-DS.3.4/blob/master/notebooks/project%203%20preprocessing.ipynb)
4. [Modeling](https://github.com/TuringCollegeSubmissions/okuzmi-DS.3.4/blob/master/notebooks/project%204%20modeling.ipynb)

## Result
![](https://raw.githubusercontent.com/TuringCollegeSubmissions/okuzmi-DS.3.4/master/pics/proof.png?token=AQ5OZ6CITJAVIAJ2UNO35MTAOBKFO)

## Conclusions
1. When dealing with many to one relationship inside csv files, it would be more efficient to extract not only AVG and COUNT but MIN, MAX as well.
2. Sometimes advanced imputing techniques like IterativeImputer, KNNImputer and MiceImputer could create bias inside of datasets and SimpleImputer with constant filling outperforms them.
3. Creating different features out of existing ones was the crucial part of the project.
4. Clustering as a feature had the highest correlation coeficient with the target.
5. When dealing with big datasets, it is important to choose fast models. LightGBM helped a lot.


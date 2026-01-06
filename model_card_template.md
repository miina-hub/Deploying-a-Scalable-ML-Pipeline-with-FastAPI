# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
RandomForestClassifer predicst the individual salary range by analyzing census data. This will categorize users into 2 groups based on income, $50,000

## Intended Use
Predict the individual's salary range by analyzing census data

## Training Data
80% of the data is used for training data

## Evaluation Data
Census data was split into train dataset and test dataset. 20% of the dataset is set aside for testing and avaluating purposes. 

## Metrics
Model evaluated the following results. 
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863

## Ethical Consideration
Data may not be representing all groups of people making for a bias dataset. 

## Caveats and Recommendations
Cleaned dataset seems to be gender bias creating an unbalance dataset. 
There is a limitation on data and by having more dataset can result in a better trained model. 
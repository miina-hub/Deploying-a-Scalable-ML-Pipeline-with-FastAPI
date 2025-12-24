import pytest
# TODO: add necessary import
import numpy as np
from ml.model import compute_model_metrics, train_model, inference
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_trainer():
    """
    Test if train_model returns a RandomForestClassifier
    """
    X_train = [[1,2,3,4,5],[1,2,3,4,5]]
    y_train = [[1,2,3,4,5],[1,2,3,4,5]]
    X_test = [[1,2,3,4,5],[1,2,3,4,5]]
    m = train_model(X_train, y_train)
    p = m.predict(X_test)
    assert p.all() == 1

    pass


# TODO: implement the second test. Change the function name and input as needed
def test_compute_metrics_model():
    """
    Test compute model metrics returns correct values
    """
    y_test = [1,0,1,0,1]
    preds = [1,0,1,0,1]
    p, r, fb = compute_model_metrics(y_test, preds)
    assert fb == 1

    pass


# TODO: implement the third test. Change the function name and input as needed
def test_fucntion_inference():
    """
    Test inference returns valid predicted values
    """
    X_train = [[1,2,3,4,5],[1,2,3,4,5]]
    y_train = [[1,2,3,4,5],[1,2,3,4,5]]  
    X_test = [[1,2,3,4,5],[1,2,3,4,5]] 
    random_forest = RandomForestClassifier()
    model = random_forest.fit(X_train, y_train)
    p = inference(model, X_test)
    assert p.all() == 1

    pass

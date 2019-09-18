import pickle
import os , numpy as np , pandas as pd
#from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn.preprocessing import StandardScaler
from django.conf import settings

path = 'http://127.0.0.1:8000/static/'

def get_predictions(raw_data):
    loaded_model = pickle.load(open("PredictionPresenter\\finalized_model.pickle", 'rb'))
    dataframe = pickle.load(open("PredictionPresenter\\dataset.dataframe" , 'rb'))

    raw_values_df = pd.DataFrame([raw_data.values()],columns = raw_data.keys())

    dataframe = pd.concat([raw_values_df , dataframe])

    sc = StandardScaler()
    x = sc.fit_transform(dataframe)
    y_pred = loaded_model.predict(x)
    return y_pred[0]
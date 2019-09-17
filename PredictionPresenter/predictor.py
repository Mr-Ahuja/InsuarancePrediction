import pickle
import os , numpy as np , pandas as pd
#from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn.preprocessing import StandardScaler
from InsuarancePrediction import settings

def get_predictions(raw_data):

    path = "{}\\PredictionPresenter".format(settings.BASE_DIR)
    loaded_model = pickle.load(open(path+"\\finalized_model.pickle", 'rb'))
    dataframe = pickle.load(open(path+"\\dataset.dataframe" , 'rb'))

    raw_values_df = pd.DataFrame([raw_data.values()],columns = raw_data.keys())

    dataframe = pd.concat([raw_values_df , dataframe])

    sc = StandardScaler()
    x = sc.fit_transform(dataframe)
    y_pred = loaded_model.predict(x)
    return y_pred[0]
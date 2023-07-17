import pandas as pd
from inference.precision import Precise as pr
import numpy as np
import warnings
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib
import math
from sklearn.metrics import mean_squared_error

class Model_inference:
    # end_train_date =datetime.strptime('2018-07-18 22:00:00+0000', '%Y-%m-%d %H:%M:%S%z')

    X_test = np.load('./model_params/X_test.npy')

    y_test = np.load('./model_params/y_test.npy')

    scaler_X = joblib.load('./model_params/scaler_x.pkl')
    scaler_Y = joblib.load('./model_params/scaler_y.pkl')

    def __init__(self, model):

        self.__model_params = model

    def get_model_params(self):

        return self.__model_params

    def predict(self, nb_forecast, time_scale):
        if (time_scale == "hourly"):
            hours = nb_forecast
        elif (time_scale == "daily"):
            hours = nb_forecast * 24
        elif (time_scale == "monthly"):
            hours = nb_forecast * 24 * 30
        else:
            hours = nb_forecast * 24 * 30 * 365

        predictions = self.__model_params.predict(Model_inference.X_test[:hours, :, :])

        inv_forecast = Model_inference.scaler_Y.inverse_transform(predictions)

        inv_y = Model_inference.scaler_Y.inverse_transform(Model_inference.y_test.reshape(-1, 1)).flatten()

        #rmse_lstm = math.sqrt(mean_squared_error(inv_y[:hours],
         #                                        inv_forecast))

        #df = pd.DataFrame(data={'Predictions': inv_forecast.flatten(), 'Actuals': inv_y[:hours]})
        precisions = pr(inv_y[:hours], inv_forecast)
        performance = precisions.performance()
        print(performance)
        return performance, inv_forecast.flatten(), inv_y[:hours]



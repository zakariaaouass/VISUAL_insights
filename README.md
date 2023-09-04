Visual Insights :
Implementation of a hybrid CNN-LSTM architecture for electricity price prediction

This project aims to develop  an application called Visual insights that uses deep learning model for electricity price prediction based on a hybrid CNN-LSTM architecture. The goal is to forecast prices for a multivariate time series, leveraging the power of both Convolutional Neural Networks (CNNs) and Long Short-Term Memory networks (LSTMs) to capture spatial and temporal patterns in the data.

**Objective:**
The primary objective of this project is to create an accurate and efficient electricity price prediction model that takes into account the multivariate nature of the time series data. By combining CNNs and LSTMs, we can effectively extract features from the sequential data and capture spatial dependencies, leading to improved forecasting performance.

**Architecture:**
The proposed hybrid CNN-LSTM architecture comprises two key components:

1. **Convolutional Neural Networks (CNNs):** CNNs are applied to process the input time series data. They excel at recognizing spatial patterns in 2D data, and in our case, will be employed to identify spatial dependencies in the multivariate time series.

2. **Long Short-Term Memory networks (LSTMs):** LSTMs are used to handle the sequential nature of the data. They are capable of learning long-term dependencies and capturing temporal patterns over time, which is crucial for accurate time series forecasting.

**Dataset:**
For this project, we will use a historical dataset of electricity prices, containing multiple related features such as date, time, weather conditions, and demand. The dataset will be preprocessed to handle missing values, scaling, and feature engineering to make it suitable for the hybrid CNN-LSTM model.



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

app = FastAPI()

with open('models/model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

class feature(BaseModel):
    features:conlist(float, min_length = 5, max_length = 5)

@app.post('/predict')
def predict(data: feature):
    try:
        # scaler = StandardScaler()

        features = np.array(data.features).reshape(1, -1)
        # features_reshape = scaler.fit_transform(features)
        prediction = loaded_model.predict(features)
        return (f'Prediction : {int(prediction)}')
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))
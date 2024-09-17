from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5500"
]

#adding CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

loaded_model = joblib.load('models/academicperformanceprediction.pkl')

class feature(BaseModel):
    features:conlist(float, min_length = 5, max_length = 5)

@app.post('/predict')
def predict(data: feature):
    try:
        #getting standardscaled value from scaler
        scaler = joblib.load('models/scaler.pkl')
        features = np.array(data.features).reshape(1, -1)
        features_reshape = scaler.transform(features)
        prediction = loaded_model.predict(features_reshape)
        return (int(prediction))
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))
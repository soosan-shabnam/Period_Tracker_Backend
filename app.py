from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.RegressionFeatures import PeriodPredictionFeatureModel

import pickle
import pandas as pd

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['GET', 'POST'],
    allow_headers=['*']
)

rf = pickle.load(open("./randomForest.pkl", "rb"))


@app.get("/")
async def root():
    return "Prediction Backend Running"


@app.post("/api/predict")
async def predict(data: PeriodPredictionFeatureModel):
    try:
        df = pd.DataFrame(
            {
                "Last": data.Last,
                "Flow": data.Flow,
                "Cramps": data.Cramps,
                "Mood": data.Mood,
                "Ovulation": data.Ovulation,
                "Age": data.Age,
                "Weight": data.Weight,
                "Height": data.Height,
                "BMI": data.BMI,
                "Race": data.Race,
                "Medical history": data.Medical_history,
                "Medications": data.Medications,
                "Length of menstrual cycle": data.Length_of_menstrual_cycle,
                "Length of menses": data.Length_of_menses,
            }
            , index=[0]
        )

        preds = rf.predict(df)

        return {"Next": preds[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

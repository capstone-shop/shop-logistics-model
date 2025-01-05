from fastapi import FastAPI, HTTPException
import joblib
import numpy as np

app = FastAPI()

# 모델 및 벡터라이저 로드
model = joblib.load("advertise_logistic_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.post("/predict")
async def predict(title: str):
    try:
        # TF-IDF 변환 및 예측
        transformed_title = vectorizer.transform([title]).toarray()
        prediction = model.predict(transformed_title)[0]
        result = "Advertise" if prediction == 1 else "Not Advertise"
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
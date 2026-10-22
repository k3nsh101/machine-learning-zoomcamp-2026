from __future__ import annotations
from pathlib import Path
from model import normalize_record
import pickle

MODEL_PATH = Path(__file__).with_name("pipeline.bin")

CLIENT = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41
}

with open(MODEL_PATH, "rb") as model:
    pipeline = pickle.load(model)

record = normalize_record(CLIENT)
prediction = float(pipeline.predict_proba([record])[0, 1])
print(round(prediction, 3))

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs("model", exist_ok=True)

# Dummy training data
data = {
    "water_level": [2,3,4,5,6,7,8],
    "turbidity": [20,30,40,50,60,70,80],
    "plastic_density": [0.1,0.2,0.3,0.4,0.6,0.8,0.9],
    "flood": [0,0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df.drop("flood", axis=1)
y = df["flood"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "model/flood_model.pkl")
print("✅ Flood prediction model trained & saved")

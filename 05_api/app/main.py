"""
  Aaron's MLOps and DevSecOps Baseline Project
  Copyright (C) 2021  Aaron Elliott

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as published
  by the Free Software Foundation, either version 3 of the License, or
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

  You may contact Aaron Elliott at mraarone@yahoo.com.
"""

import numpy as np
import onnxruntime
from pydantic import BaseModel
import uvicorn
import pickle
from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier

# Create an object of class FastAPI
global app

# CORS, make sure you set the IP address below to the appropriately for cross domain IP addresses, can be an array.
app = FastAPI(
    servers=[{"url": "http://127.0.0.1:8000", "description": "Development Environment"}]
)

# Load feature_names and target name
feature_names = pickle.load(open("app/features.pickle", "rb"))

target_name = pickle.load(open("app/target.pickle", "rb"))

# Now in onnx model we have to create an InferenceSession and pass the onnx file path in it
session = onnxruntime.InferenceSession("app/rf_m.onnx")

# Now we get the input and out names we used to save the model initially.
first_input_name = session.get_inputs()[0].name

first_output_name = session.get_outputs()[0].name


class Data(BaseModel):
    """In fast-api this class is created just for documentation purposes"""

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(data: Data):
    try:
        # Conver the json into dict
        data_dict = data.dict()
        # Use the feature name to make the dict into a list

        to_predict = [data_dict[feature] for feature in feature_names]
        # Reshape the data into 1 row and n columns where n is the number of features in the dataset.In iris it is 4

        to_predict = np.array(to_predict).reshape(1, -1)
        # Now run the session and since while creating we made sure the input is in flat we explicitly convert the data into float
        pred_onx = session.run(
            [first_output_name], {first_input_name: to_predict.astype(np.float32)}
        )[0]

        # Now we map these labels back to the class names.In case of iris it will setosa,virginica and versicolor.
        encode2label = target_name[int(pred_onx[0])]

        return {"prediction": str(encode2label)}
    except:
        return {"prediction": "error"}

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

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# import numpy as np
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# import pandas as pd
import pickle

# import host environment variables
import os
from dotenv import load_dotenv

load_dotenv()

PROJECTNAME = os.getenv("PROJECTNAME")


def load_data():
    """This function will save the feature names
    and target name

    Returns:X_train and Y_train
    """
    data = load_iris()
    X = data["data"]
    Y = data["target"]
    target_name = data["target_names"]

    feature_names = data["feature_names"]
    """By default the feature names are sepal length (cm) and we will simplify
    it to sepal_length in the name so we will replace it with _"""
    feature_names = [
        " ".join(name.split()[:2]).replace(" ", "_") for name in feature_names
    ]
    # Save the target_name and feature names
    pickle.dump(target_name, open("target.pickle", "wb"))
    pickle.dump(feature_names, open("features.pickle", "wb"))
    return X, Y


def save_onnx():
    # Get the X and Y values from iris data
    X, Y = load_data()

    # Create a RandomForest Classifier
    rf = RandomForestClassifier()
    # Fit the model
    rf.fit(X, Y)

    """Now specify the input as a FloatTensorType and pass the shape as a list.
    Here the shape is None,num_columns which incase of iris data is None,4.
    """
    initial_type = [("float_input", FloatTensorType([None, X.shape[1]]))]

    # Then we convert the model into an onnx object
    onnx = convert_sklearn(rf, initial_types=initial_type)

    # Then we save the file
    with open("rf_m.onnx", "wb") as f:
        f.write(onnx.SerializeToString())


if __name__ == "__main__":
    save_onnx()

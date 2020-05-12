from joblib import load
from preprocess import prep_data
import pandas as pd

def predict_from_csv(path_to_csv):

    df = pd.read_csv(path_to_csv)
    X, y = prep_data(df)
    # reg = load("reg.joblib")
    
    model = load("dtmodel.joblib") 
# ###### "Decision Tree" seems TOO perfect, like the data was generated by this model!

# ###### "Random Forest" acts great
    # model = load("rfmodel.joblib")    

# ###### The below models weren't considered good, e.g. predicting negative/extremly light/heavy weight
    # model = load("Scaledlassomodel.joblib")
    # model = load("scaledlrmodel.joblib")
    # model = load("scaledmlprmodel.joblib")
    # model = load("pcamodel.joblib")
    # model = load("mlprmodel.joblib")
    # model = load("lrmodel.joblib")
    # model = load("lassomodel.joblib")

    predictions = model.predict(X)
    return predictions

if __name__ == "__main__":
    predictions = predict_from_csv("fish_holdout_demo.csv")
    print(predictions)

# ######
# ### HOW TO SCORE ###
# from sklearn.metrics import mean_squared_error
# ho_predictions = predict_from_csv("fish_holdout.csv")
# ho_truth = pd.read_csv("fish_holdout.csv")["Weight"].values
# ho_mse = mean_squared_error(ho_truth, ho_predictions)
# print(ho_mse)
# ######
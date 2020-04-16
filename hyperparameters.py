"""
CSCC11 - Introduction to Machine Learning, Winter 2020, Assignment 2
B. Chan, E. Franco, D. Fleet

===========================================================

 COMPLETE THIS TEXT BOX:
 
 Student Name: Abhinav Chaudhary
 Student number: 1002707733 
 UtorID: chaud349   
 
 I hereby certify that the work contained here is my own
 
 
 Abhinav Chaudhary 
 (sign with your name)
 
===========================================================
"""

# ====================================================
# TODO: Use Validation Set to Tune hyperparameters for the Amazon dataset
# Use Optimal Parameters to get good accuracy on Test Set
AMAZON_HYPERPARAMETERS = {
    "num_trees": 400,
    "features_percent": 0.2,
    "data_percent": 0.8,
    "max_depth": 40,
    "min_leaf_data": 5,
    "min_entropy": 1,
    "num_split_retries": 80
}
# ====================================================

# ====================================================
# TODO: Use Validation Set to Tune hyperparameters for the Occupancy dataset
# Use Optimal Parameters to get good accuracy on Test Set
OCCUPANCY_HYPERPARAMETERS = {
    "num_trees": 4,
    "features_percent": 1,
    "data_percent": 1,
    "max_depth": 10,
    "min_leaf_data": 10,
    "min_entropy": 0.6,
    "num_split_retries": 10
}
# ====================================================

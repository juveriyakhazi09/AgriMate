import pickle

# Load trained model
with open("crop_model.pkl", "rb") as file:
    model = pickle.load(file)

# Test input
# N, P, K, temperature, humidity, pH, rainfall
sample = [[90, 42, 43, 20.88, 82.00, 6.50, 202.94]]

# Make prediction
prediction = model.predict(sample)

print("Predicted crop:", prediction[0])
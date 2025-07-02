import streamlit as st
import pickle

# Load the trained Decision Tree model
with open("DT_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Iris Flower Species Prediction App 🌸")
st.write("Enter the flower measurements below:")

# Input features (Iris dataset style)
sepal_length = st.number_input("Sepal Length (cm)", value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", value=3.5)
petal_length = st.number_input("Petal Length (cm)", value=1.4)
petal_width = st.number_input("Petal Width (cm)", value=0.2)

# Predict button
if st.button("Predict"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)[0]

    # Map numeric prediction to Iris class name
    class_labels = {
        0.0: "Setosa",
        1.0: "Versicolor",
        2.0: "Virginica"
    }
    species_name = class_labels.get(prediction, "Unknown")

    st.success(f"Prediction: {prediction} — {species_name}")
import pickle
knn = pickle.load(open(r'C:\Users\negae\OneDrive\Desktop\BD NOV\frontend\knn_model.pkl', 'rb'))

import streamlit as st
st.title("Airline Passenger Satisfaction")


flight_distance = st.slider('Flight Distance', min_value=31, max_value=4983)
gender = st.selectbox('Gender', ['Male', 'Female'])
Age = st.slider('Age', min_value=7, max_value=85)
Type_of_Travel = st.selectbox('Type of Travel', ['Business travel','Personal Travel'])
Class = st.selectbox('Class', ['Business', 'Eco','Eco Plus'])
Inflight_wifi_service = st.slider('Inflight wifi service', min_value=0, max_value=5)
Customer_Type = st.selectbox('Customer Type', ['Loyal Customer', 'Disloyal Customer'])
Ease_of_Online_booking = st.slider('Ease of Online booking', min_value=0, max_value=5)
Food_and_drink = st.slider('Food and drink', min_value=0,max_value=5)
Online_boarding = st.slider('Online boarding', min_value=0, max_value=5)
Seat_comfort = st.slider('Seat comfort', min_value=0, max_value=5)
Inflight_entertainment = st.slider('Inflight entertainment', min_value=0, max_value=5)
On_board_service = st.slider('On-board service', min_value=0, max_value=5)
Leg_room_service = st.slider('Leg room service', min_value=0, max_value=5)
Baggage_handling = st.slider('Baggage handling', min_value=1, max_value=5)
Checkin_service = st.slider('Checkin service ', min_value=0, max_value=5)
Inflight_service = st.slider('Inflight service', min_value=0, max_value=5)
Cleanliness = st.slider('Cleanliness', min_value=0, max_value=5)
Departure_Delay_in_Minutes = st.slider('Departure Delay in Minutes', min_value=0, max_value=1592)
Arrival_Delay_in_Minutes = st.slider('Arrival Delay in Minutes', min_value=0, max_value=1584)

# Create a button to trigger the prediction
if st.button("Predict"):
    # Create a list to store the input values
    input_values = [
        flight_distance,
        gender,
        Age,
        Type_of_Travel,
        Class,
        Inflight_wifi_service,
        Customer_Type,
        Ease_of_Online_booking,
        Food_and_drink,
        Online_boarding,
        Seat_comfort,
        Inflight_entertainment,
        On_board_service,
        Leg_room_service,
        Baggage_handling,
        Checkin_service,
        Inflight_service,
        Cleanliness,
        Departure_Delay_in_Minutes,
        Arrival_Delay_in_Minutes,
        0
    ]
    
    # Convert categorical values to numerical values
    gender_mapping = {'Male': 0, 'Female': 1}
    Type_of_Travel_mapping = {'Business travel': 0, 'Personal Travel': 1}
    Class_mapping = {'Business': 0, 'Eco': 1, 'Eco Plus': 2}
    Customer_Type_mapping = {'Loyal Customer': 0, 'Disloyal Customer': 1}
    
    input_values[1] = gender_mapping[input_values[1]]
    input_values[3] = Type_of_Travel_mapping[input_values[3]]
    input_values[4] = Class_mapping[input_values[4]]
    input_values[6] = Customer_Type_mapping[input_values[6]]
    
    # Make predictions using the loaded model
    prediction = knn.predict([input_values])
    
    # Display the prediction result
    st.write("Prediction:", prediction[0])
    
   

import numpy as np
from sklearn.linear_model import LinearRegression

def predict_following_quantity(values, threshold):
    # Creates two variables (a and b) for linear regression and makes a forecast based on historical data for drugs
    a = np.arange(len(values)).reshape(-1, 1)
    b = np.array(values).reshape(-1, 1)
    
    # Fit linear regression model based on data storage values for drug consumption (based on Subsahara Africa usage amounts)
    model = LinearRegression()
    model.fit(a, b)
    
    # Forecasts next quantity based on the trend seen in the data 
    following_quantity = model.predict([[len(values)]])[0][0]
    
    # Check if the following quantity is below the threshold amount 
    if following_quantity < threshold:
        alert_message = f"Current inventory is almost depleted. Next forecasted quantity is {following_quantity}. We will send an order to suppliers if depletion continues"
        return following_quantity, alert_message
    else:
        return following_quantity, None

def main():
    # Example numerical values for trial testing 
    numerical_values = [10, 20, 30, 40, 50]
    
    # Threshold for low supply, initial value 25 but can be updated based on individual institute's need
    threshold = 25
    
    # Sorting the numerical values
    sorted_values = sorted(numerical_values)
    print("sorted_amounts:", sorted_values)
    
    # Forecast the next quantity and check for low supply based on threhold criteria (here it is 25)
    next_quantity, alert_message = predict_following_quantity(sorted_values, threshold)
    print("Forecasted next quantity based on trend:", next_quantity)
    
    # Print alert message if there is low supply and send notification to pharmaceutical suppliers 
    if alert_message:
        print(alert_message)

if __name__ == "__main__":
    main()

def predict_car_value(car_data):
    # Dummy logic (replace with real model prediction)
    base_price = 20000
    depreciation = (2025 - car_data['year']) * 1000 + (car_data['mileage'] * 0.05)
    estimated_value = max(base_price - depreciation, 1000)
    return round(estimated_value, 2)

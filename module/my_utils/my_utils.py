def calculate_average(data):
    if not data:
        raise ValueError("datalist cannot be empty")
    return sum(data) / len(data)
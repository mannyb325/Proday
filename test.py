def moving_average(data, window_size):
    """
    Calculate the moving average of a list of numbers.

    Args:
        data (list of float): The input data.
        window_size (int): The size of the moving window.

    Returns:
        list of float: The moving averages.
    """
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if window_size > len(data):
        raise ValueError("Window size must not be greater than data length")

    averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / window_size
        averages.append(avg)
    return averages

# Example usage:
# data = [1, 2, 3, 4, 5, 6]
# print(moving_average(data, 3))  # Output: [2.0, 3.0, 4.0, 5.0]
import random


def pick_random_city():
    """Pick a random city from the given list"""
    cities = ["Pune", "Mumbai", "Ahmedabad", "New Delhi", "Kolkata", "Bengaluru", "Chennai"]
    return random.choice(cities)


def generate_test_data(num_records=5):
    """Generate test data for database operations."""
    test_data = []
    for _ in range(num_records):
        data = {
            'primary_city': pick_random_city(),
            'secondary_city': pick_random_city(),
        }
        test_data.append(data)
    return test_data

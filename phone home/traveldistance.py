# Space Week Day 3: Phone Home (User Input Version)

# Speed of message in km/s
SPEED = 300000  

def message_time(distances):
    """
    This function calculates the total time (in seconds)
    for a message to travel through all satellites to the home planet.
    """
    # 1️⃣ Calculate total distance
    total_distance = sum(distances)

    # 2️⃣ Calculate travel time (distance / speed)
    travel_time = total_distance / SPEED

    # 3️⃣ Each satellite adds 0.5 seconds delay
    delay_time = (len(distances) - 1) * 0.5

    # 4️⃣ Add both travel time and delay time
    total_time = travel_time + delay_time

    # 5️⃣ Round result to 4 decimal places and remove trailing zeros
    final_time = round(total_time, 4)
    result = ('%.4f' % final_time).rstrip('0').rstrip('.')

    # 6️⃣ Return the result
    return result


# ✅ --- MAIN PROGRAM ---

# Ask user to enter distances separated by spaces
# Example input: 100000 200000 150000 300000
user_input = input("Enter distances (in km) separated by spaces: ")

# Convert input string into a list of numbers (floats or ints)
distances = [float(x) for x in user_input.split()]

# Call the function and show result
print("Total time:", message_time(distances), "seconds")

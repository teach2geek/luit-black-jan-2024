import random

# Prompt the user to input their department name and the number of EC2 instances they need names for.
department = input("What is your department? ")
instances = int(input("How many EC2 instances? "))

def generate_ec2_names(department, instances):
    # Initialize an empty set to store unique EC2 instance names.
    unique_names = set()

    # Define a string containing all possible characters for the random part of the name.
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%()'

    # Continue generating names until the set has the required number of unique names.
    while len(unique_names) < instances:
        # Generate a random string of 8 characters from the defined character set.
        random_part = ''.join(random.choices(chars, k=8))

        # Combine the department name and the random string to form the EC2 instance name.
        name = f"{department}-{random_part}"

        # Add the generated name to the set of unique names.
        unique_names.add(name)
    
    # Convert the set of names to a list and return it.
    return list(unique_names)

# Generate EC2 instance names using the provided department and instance count.
ec2_names = generate_ec2_names(department, instances)

# Print each generated EC2 instance name.
for name in ec2_names:
    print(name)

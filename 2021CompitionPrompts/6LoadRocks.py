# The Rockland Quarry stores rocks in bags. The first bag on the shelf has 1 pound of rocks, the next bag has 2 pounds of rocks, the next has 3 pounds of rocks and so on. The quarry has an unlimited number of bags of rocks. In other words, the heaviest bag stored weighs as much as the largest integer value. A customer specifies a weight when ordering rocks. Rocky, the forklift operator, always takes bags from adjacent locations to meet the required weight. He also always takes a minimum of two bags. You must write an application to help Rocky find all the possible combinations of rock bags with consecutive weights that will total the weight the customer ordered. For example, Bobby Stone has ordered 15 pounds of rock. There are 3 combinations of consecutive weights that will add to 15. These are:

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# For some large orders the number of combinations could be quite high and result in a large amount of output. To reduce the amount of output and still prove the application works the owner, Mr. Slate, has agreed to accept two pieces of data instead. The first is the number of combinations that meet the criteria. The second is the sum of the first number in each combination. For an order of 15 pounds the output would be 3 and 12. The 12 was calculated as 1 + 4 + 7.

# Input
# Prompt for and read the weight of rocks on order. The weight of rocks will be a positive integer greater than 2. Data will be entered from console. You do not need to edit the input data. Rerun your application to test each test case.

# Output
# Display the number of bag combinations that will total the order weight followed by the sum of the first number in each combination.





# Read the weight of the order from the user
order_weight = int(input("Enter the weight of the order: "))

# Initialize the number of combinations and the sum of the first numbers
num_combinations = 0
sum_first_numbers = 0

# Loop through all possible values for the first number
for first_number in range(1, order_weight):
    # Initialize the sum of the current combination
    combination_sum = 0

    # Loop through the consecutive numbers starting with the first number
    for i in range(first_number, order_weight):
        # Add the current number to the sum
        combination_sum += i

        # If the sum is equal to the order weight, increment the number of
        # combinations and add the first number to the sum of the first numbers
        if combination_sum == order_weight:
            num_combinations += 1
            sum_first_numbers += first_number
            break

        # If the sum is greater than the order weight, stop looping
        elif combination_sum > order_weight:
            break

# Print the number of combinations and the sum of the first numbers
print("Number of combinations:", num_combinations)
print("Sum of first numbers:", sum_first_numbers)


#Note that this implementation is not optimized and may take a long time to execute for large values of order_weight. You may want to improve the performance of the code by using more efficient algorithms and data structures.

# Assign a value to variable 'x'
x = 10

# Assign 'y' to the same value as 'x'
y = x

# Now, if we change the value of 'y', it will not affect 'x' because 'y' has its own copy of the value.
y = 20

print("x:", x)  # Output: x: 10
print("y:", y)  # Output: y: 20

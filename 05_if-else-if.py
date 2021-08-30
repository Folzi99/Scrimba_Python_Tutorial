# experiment with variables being True or False to see results of Boolean expression
# refer to truth tables for further information on Booleans
is_raining =
is_cold =
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")
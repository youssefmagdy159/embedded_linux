import os

# Get the value of a specific environment variable
variable_name = "MY_ENV_VARIABLE"
if variable_name in os.environ:
    variable_value = os.environ[variable_name]
    print(f"The value of {variable_name} is: {variable_value}")
else:
    print(f"{variable_name} is not set in the environment.")

# List all environment variables
print("\nAll environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

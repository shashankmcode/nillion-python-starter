from nada import Client, Program, IntegerInput, IntegerOutput

# Define your inputs
inputs = {
    "my_int1": IntegerInput(value=5),  # Replace 5 with your desired value
    "my_int2": IntegerInput(value=10)  # Replace 10 with your desired value
}

# Define your program (this should be the name of the function you created)
program = Program(nada_main)

# Create a client to run the program
client = Client()

# Run the program with the defined inputs
outputs = client.run(program, inputs)

# Retrieve the output
output_value = outputs["my_output"].value

# Print the result
print(f"Output value: {output_value}")

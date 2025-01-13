def modify_and_write_file():
    try:
        # Open and read the content of the file
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify the content (e.g., change to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("File successfully modified and written to 'output.txt'")

    except FileNotFoundError:
        print("Error: 'input.txt' not found. Make sure the file exists in the project folder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
modify_and_write_file()

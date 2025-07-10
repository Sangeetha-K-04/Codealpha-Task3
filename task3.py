import re

# Input and output file paths
input_file = "sample.txt"   # Make sure this file exists
output_file = "emails.txt"

# Read file and extract emails
with open(input_file, "r") as file:
    data = file.read()

emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', data)

# Save emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"{len(emails)} email(s) extracted and saved to {output_file}")

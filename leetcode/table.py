import os
import re
import urllib.parse
import easygui as gui
from tabulate import tabulate

# Function to extract question number and name from directory name
def extract_question_info(dir_name):
    match = re.match(r'(\d+)\.\s+(.*)', dir_name)
    if match:
        question_no = match.group(1)
        question_name = match.group(2)
        return question_no, question_name
    return None, None

# Function to find solution files in a directory
def find_solution_files(directory):
    cpp_file = None
    python_file = None
    for file_name in os.listdir(directory):
        if file_name.endswith('.cpp'):
            cpp_file = file_name
        elif file_name.endswith('.py'):
            python_file = file_name
    return cpp_file, python_file

# Main function to generate the table
def generate_table(root_directory, github_repo_url):
    table = []
    for dir_name, _, files in os.walk(root_directory):
        folder_name = os.path.basename(dir_name)
        question_no, question_name = extract_question_info(folder_name)
        if question_no and question_name:
            cpp_file, python_file = find_solution_files(dir_name)
            cpp_solution_link = f"{github_repo_url}/{urllib.parse.quote(folder_name)}/{question_no}.cpp" if cpp_file else ""
            python_solution_link = f"{github_repo_url}/{urllib.parse.quote(folder_name)}/{question_no}.py" if python_file else ""
            row = {
                "Question No.": question_no,
                "Question Name": question_name,
                "Problem Link": f"https://leetcode.com/problems/{question_name.lower().replace(' ', '-')}/",
                "C++ Solution Link": cpp_solution_link,
                "Python Solution Link": python_solution_link
            }
            table.append(row)
    return table

# Specify the root directory where the problem directories are located
root_directory = "./final_solution"
github_repo_url = "https://github.com/astromanish/CP/blob/master/final_solution"

# Generate the table
table = generate_table(root_directory, github_repo_url)

# Format the table as Markdown
table_markdown = tabulate(table, headers="keys", tablefmt="github")

# Write the Markdown content to a file named 'table.md'
with open('table.md', 'w') as file:
    file.write(table_markdown)

# Display a message to confirm the file has been written
gui.msgbox("Table content has been written to 'table.md'")

# # Generate a formatted string representation of the table
# table_text = "\n".join([f"{row['Question No.']} | {row['Question Name']} | {row['Problem Link']} | {row['C++ Solution Link']} | {row['Python Solution Link']}" for row in table])

# # Display the table in an easygui textbox dialog
# gui.textbox(msg="LeetCode Problem Solutions",
#             title="Problem Solutions Table",
#             text=table_text,
#             codebox=True)


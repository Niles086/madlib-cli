# madlib.py

import os

def read_template(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {path}")

def parse_template(template):
    language_parts = []
    parsed_template = template
    # parsed_template_duplicate = parsed_template
    while '{' in parsed_template and '}' in parsed_template:
        start_index = parsed_template.find('{')
        end_index = parsed_template.find('}')
        language_part = parsed_template[start_index + 1:end_index]
        language_parts.append(language_part)
        parsed_template = parsed_template[:start_index] + '[]' + parsed_template[end_index + 1:] 
    parsed_template = parsed_template.replace('[]', ('{}'))

    return parsed_template.strip(), language_parts

def merge(template, words):
    return template.format(*words)

def main():
    print("Welcome to the Madlib game!")
    template_path = input("Enter the path to the Madlib template file: ")

    template = read_template(template_path)
    parsed_template, language_parts = parse_template(template)

    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)

    completed_madlib = merge(parsed_template, user_inputs)

    print("\nCompleted Madlib:")
    print(completed_madlib)

    output_file_path = input("Enter the path to save the completed Madlib: ")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(completed_madlib)

if __name__ == "__main__":
    main()

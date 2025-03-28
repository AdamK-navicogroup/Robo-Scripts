import json
import re

def read_instructions(instructions_file):
    with open(instructions_file, 'r') as file:
        instructions = file.read()

    match_name = re.search(r"Name:\s*(\S+)", instructions)
    name = match_name.group(1) if match_name else "output"

    replace_with_stop_patterns = re.findall(r"REPLACE UNDER HERE\n(.*?)WITH UNDER HERE(.*?)STOP", instructions, re.DOTALL)
    
    replacements = []
    for replace_section, insert_section in replace_with_stop_patterns:
        replace_content = replace_section.strip()
        insert_content = insert_section.strip()
        replacements.append((replace_content, insert_content))

    return name, replacements

def mold_json(json_file, replacements):
    with open(json_file, 'r') as file:
        base_json = file.read()
    
    modified_json_text = base_json

    for replace_content, insert_content in replacements:
        modified_json_text = modified_json_text.replace(replace_content, insert_content)
        print(f"Replaced:\n{replace_content}\nwith:\n{insert_content}\n")
    
    try:
        modified_json = json.loads(modified_json_text)
        return modified_json
    except json.JSONDecodeError as e:
        print(f"Error decoding modified JSON: {e}")
        return None

def write_json(output_file, modified_json):
    with open(output_file, 'w') as file:
        json.dump(modified_json, file, indent=2)

def mold(base_file, mold_instructions):
    name, replacements = read_instructions(mold_instructions)

    molded_json = mold_json(base_file, replacements)
    output_file = f"./generated/{name}.json"
    write_json(output_file, molded_json)
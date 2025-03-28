import json
import os

def build_base_script(base_script_file, config_file, scripts_directory):
    with open(base_script_file, 'w') as base_file:
        json.dump([], base_file, indent=2)

    with open(base_script_file, 'r') as base_file:
        base_script = json.load(base_file)

    with open(config_file, 'r') as config_file:
        config = json.load(config_file)
        scripts = config.get('scripts', [])
        arguments = config.get('arguments', {})

    for script_name in scripts:
        script_file_path = os.path.join(scripts_directory, f"{script_name}.json")
        
        if os.path.exists(script_file_path):
            with open(script_file_path, 'r') as script_file:
                script_content = json.load(script_file)
                base_script.extend(script_content)
        else:
            print(f"{script_file_path} not found")

    with open(base_script_file, 'w') as base_file:
        json.dump(base_script, base_file, indent=2)

    return arguments

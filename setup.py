from script_molder import mold
from script_builder import build_base_script

base_script_file = 'base_script.json'
config_file = 'script_configuration.json'
scripts_directory = 'scripts'

if __name__ == "__main__":
    arguments = build_base_script(base_script_file, config_file, scripts_directory)
    mold_files = arguments.get('mold')
    oem = arguments.get('oem')
    for file in mold_files:
        mold(base_script_file, f"./generator/{oem}_{file}.txt")
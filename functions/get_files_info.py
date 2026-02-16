def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(directory):
        print("f'Error: "{directory}" is not a directory'")
    
    try:
        path = target_dir
        file_list = os.listdir(path)
        for file in file_list:
            
#- README.md: file_size=1032 bytes, is_dir=False
#- src: file_size=128 bytes, is_dir=True
#- package.json: file_size=1234 bytes, is_dir=False


    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Insufficient permissions to access '{path}'.")
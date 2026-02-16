def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(directory):
        print(f'Error: "{directory}" is not a directory')
    
    
    path = target_dir
    file_list = os.listdir(path)
    for file in file_list:
        file_path = os.path.join(path, file)
        try:
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            print(f'  - {file}: file_size={file_size} bytes, is_dir={is_dir}')
        except FileNotFoundError:
            print(f'Error: File "{file}" was not found.')
        except PermissionError:
            print(f'Error: Insufficient permissions to access "{file}".')
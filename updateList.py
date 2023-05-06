def main():
    import os
    import fileinput
    from lvls import __all__

    # Get the absolute path of the script
    script_path = os.path.abspath(__file__)

    # Get the directory containing the script
    script_dir = os.path.dirname(script_path)

    # Specify the path to the user's directory relative to the script's directory
    directory_path = os.path.join(script_dir, "lvls/")

    # Get a list of all the files in the directory, excluding the script itself
    files = os.listdir(directory_path)

    # Check that all the files are in the __all__ list
    init_file_path = os.path.join(directory_path, "__init__.py")
    with fileinput.FileInput(init_file_path, inplace=True) as file:
        found_files = False
        for line in file:
            if line.startswith("__all__"):
                found_files = True
                # Extract the list of files from the line
                line = line.strip()
                line = line.removeprefix("__all__ = ")
                line = line.strip('[" "]')
                all_files = line.split('", "')
                # Add any missing files to the list
                for f in files:
                    f = f.replace(".py", "")
                    if f == "__init__" or f == "__pycache__":
                        continue
                    elif f not in all_files:
                        all_files.append(f)
                for a in all_files:
                    a += ".py"
                    if a not in files:
                        a = a.replace(".py", "")
                        all_files.remove(a)
                # Write the modified __all__ line to the file
                line = "__all__ = [" + ", ".join(f'"{f}"' for f in all_files) + "]\n"
            print(line, end="")
        # If the __all__ line was not found, add it to the end of the file
        if not found_files:
            all_files = [f for f in files]
            line = "__all__ = [" + ", ".join(f'"{f}"' for f in all_files) + "]\n"
            print(line, end="")

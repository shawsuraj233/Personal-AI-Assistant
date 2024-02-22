import os

def create_file_with_index(base_name:str,text:str):
    file_path = f'/home/suraj2000/Desktop/Jarvis/Outputs/{base_name}.txt'
    if os.path.exists(file_path):
        # If the file already exists, create a new file with a suffix
        file_name, file_extension = os.path.splitext(file_path)
        counter = 1
        while True:
            new_file_path = f"{file_name}_{counter}{file_extension}"
            if not os.path.exists(new_file_path):
                with open(new_file_path, "w") as f:
                    f.write(text)  # Creates an empty file
                print(f"Created new file: {new_file_path}")
                break
            counter += 1
    else:
        # If the file doesn't exist, create it
        with open(file_path, "w") as f:
            f.write(text)  # Creates an empty file
        print(f"Created new file: {file_path}")
    print(f"Created file: {file_path}")

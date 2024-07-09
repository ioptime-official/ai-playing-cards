import os
import argparse

# Define the mapping from old class numbers to new class numbers
class_mapping = {
    1: 0
}

def update_class_numbers_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    txt_files = [file for file in files if file.endswith('.txt')]

    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        # Read the original file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Modify the class numbers
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:  # Check if line is not empty
                old_class_num = int(parts[0])
                new_class_num = class_mapping.get(old_class_num, old_class_num)  # Default to old class if not in mapping
                parts[0] = str(new_class_num)
                new_lines.append(' '.join(parts))
            else:
                new_lines.append('\n')  # Preserve empty lines if any

        # Write the modified annotations back to the same file
        with open(file_path, 'w') as file:
            for line in new_lines:
                file.write(line + '\n')

        print(f"Updated {file_name}")

    print("Class numbers updated successfully in all files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update YOLO class numbers in annotation files within a folder.")
    parser.add_argument('folder_path', type=str, help="Path to the folder containing annotation files (.txt).")
    
    args = parser.parse_args()
    update_class_numbers_in_folder(args.folder_path)

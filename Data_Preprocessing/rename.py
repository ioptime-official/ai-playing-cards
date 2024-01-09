import os

def rename_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Sort the files to ensure consistent numbering
    files.sort()

    # Initialize a counter for numbering
    counter = 941 #11227

    # Iterate through the files and rename them
    for file_name in files:
        # Split the file name and extension
        base_name, file_extension = os.path.splitext(file_name)

        # Construct the new file name with a number and the original extension
        new_name = f"{counter:03d}{file_extension}"

        # Build the full paths for old and new names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        # Increment the counter for the next file
        counter += 1

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to your folder containing the files
    folder_path = '/media/ioptime/HDD_11/Cards_Data/labelled_data/Players_detection_data/Data/Augmented/ToSepia/images'

    # Call the function to rename files
    rename_files(folder_path)

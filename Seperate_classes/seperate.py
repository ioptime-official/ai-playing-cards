import os
import argparse

def split_annotations(input_folder):
    # Paths for output folders
    class_0_folder = os.path.join(input_folder, 'class_0')
    class_1_folder = os.path.join(input_folder, 'class_1')

    # Create directories if they don't exist
    os.makedirs(class_0_folder, exist_ok=True)
    os.makedirs(class_1_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_folder, filename)
            
            # Read the input file
            with open(input_file, 'r') as file:
                lines = file.readlines()

            # Split the annotations by class
            class_0_annotations = []
            class_1_annotations = []

            for line in lines:
                if line.startswith('0 '):
                    class_0_annotations.append(line)
                elif line.startswith('1 '):
                    class_1_annotations.append(line)

            # Write the class 0 annotations to a new file
            if class_0_annotations:
                with open(os.path.join(class_0_folder, filename), 'w') as file:
                    file.writelines(class_0_annotations)

            # Write the class 1 annotations to a new file
            if class_1_annotations:
                with open(os.path.join(class_1_folder, filename), 'w') as file:
                    file.writelines(class_1_annotations)

    print("Annotations have been split and saved in the respective folders.")

def main():
    parser = argparse.ArgumentParser(description='Split YOLO annotations by class.')
    parser.add_argument('input_folder', type=str, help='Path to the folder containing the annotation files.')

    args = parser.parse_args()
    split_annotations(args.input_folder)

if __name__ == '__main__':
    main()
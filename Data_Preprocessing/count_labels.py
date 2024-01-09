import os
import csv

def count_classes_in_file(file_path, class_counts):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Extract the class label from each line
        class_label = int(line.split()[0])

        # Update the class count dictionary
        class_counts[class_label] = class_counts.get(class_label, 0) + 1

def count_classes_in_folder(folder_path):
    class_counts = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            count_classes_in_file(file_path, class_counts)

    return class_counts

def save_to_csv(class_counts, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Class', 'Occurrences'])

        for class_label, count in class_counts.items():
            csv_writer.writerow([class_label, count])

# Example usage
folder_path = '/home/ioptime/workfolder/playingCard_detection/split_dataset/train/labels'
output_csv_file = '/home/ioptime/workfolder/playingCard_detection/split_dataset/train/TRAIN_class_counts.csv'

class_counts = count_classes_in_folder(folder_path)
save_to_csv(class_counts, output_csv_file)

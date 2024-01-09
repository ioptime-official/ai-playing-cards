import os
import shutil
import random
from sklearn.model_selection import train_test_split

def create_folders(root_folder):
    for split in ['train', 'valid', 'test']:
        for folder in ['images', 'labels']:
            path = os.path.join(root_folder, split, folder)
            os.makedirs(path, exist_ok=True)

def split_data(images, labels, shuffle_threshold=0.9):
    # Shuffle data randomly if the shuffle threshold is met
    if random.random() <= shuffle_threshold:
        combined = list(zip(images, labels))
        random.shuffle(combined)
        images[:], labels[:] = zip(*combined)

    # Split data into training (70%), validation (20%), and testing (10%)
    train_images = images[:int(0.7 * len(images))]
    test_images = images[int(0.7 * len(images)):]
    train_labels = labels[:int(0.7 * len(labels))]
    test_labels = labels[int(0.7 * len(labels)):]

    valid_images, test_images, valid_labels, test_labels = train_test_split(test_images, test_labels, test_size=1/3, random_state=42)

    return train_images, valid_images, test_images, train_labels, valid_labels, test_labels

def move_data(src_folder, dest_folder, images, labels):
    for image in images:
        shutil.copy(os.path.join(src_folder, 'images', image), os.path.join(dest_folder, 'images'))

    for label in labels:
        shutil.copy(os.path.join(src_folder, 'labels', label), os.path.join(dest_folder, 'labels'))

def main():
    source_folder = '/media/ioptime/HDD_11/Cards_Data/labelled_data/Players_detection_data/Data/Data3/Final'
    root_folder = '/media/ioptime/HDD_11/Cards_Data/labelled_data/Players_detection_data/Data/Data3/split'

    # Create destination folders
    create_folders(root_folder)

    # Get list of images and labels
    images = os.listdir(os.path.join(source_folder, 'images'))
    labels = os.listdir(os.path.join(source_folder, 'labels'))

    # Split and shuffle data with a shuffle threshold of 0.7
    train_images, valid_images, test_images, train_labels, valid_labels, test_labels = split_data(images, labels, shuffle_threshold=0.7)

    # Move data to destination folders
    move_data(source_folder, os.path.join(root_folder, 'train'), train_images, train_labels)
    move_data(source_folder, os.path.join(root_folder, 'valid'), valid_images, valid_labels)
    move_data(source_folder, os.path.join(root_folder, 'test'), test_images, test_labels)

    print("Data split, shuffled, and moved successfully!")

if __name__ == "__main__":
    main()


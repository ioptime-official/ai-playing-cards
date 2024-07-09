# AI PLaying Cards Custom Object Detection Using YOLOv5

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [Training the Model](#training-the-model)
- [Inference](#inference)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction

This project aims to detect and classify playing cards using the YOLOv5 object detection algorithm. YOLOv5 (You Only Look Once) is a state-of-the-art real-time object detection system. The goal is to create a custom model that can accurately identify different playing cards from images or video feeds.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ioptime-official/ai-playing-cards
    cd ai-playing-cards
    ```

2. Create a virtual environment and activate it:
    ```bash
    conda create -n card_mobile_game python=3.11
    conda activate card_mobile_game
    ```

3. Install the required dependencies:
    ```bash
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    pip install ultralytics
    pip install albumentations
    ```
4. Helping Scripts:
    This Repository has 4 Helping Scripts which can be used for multiple tasks and there details are given in their respective folders
    - [Augmentation(Albumentations)](https://github.com/ioptime-official/ai-playing-cards/tree/main/Augmentation(Albumentation)) for image augmentation
    - [Draw_BBOX ](https://github.com/ioptime-official/ai-playing-cards/tree/main/Augmentation(Albumentation)](https://github.com/ioptime-official/ai-playing-cards/tree/main/Draw_BBOX))for BBOX visualization on images
    - Class sepreation script is in [Seperate_classes](https://github.com/ioptime-official/ai-playing-cards/tree/main/Seperate_classes)
    - [class_mapping](https://github.com/ioptime-official/ai-playing-cards/tree/main/class_mapping) maps the classes to whatever class number you want
## Dataset Preparation

1. Collect images of playing cards and annotate them using tools like LabelImg or Roboflow.
2. Ensure the annotations are in the YOLO format (text files with bounding box coordinates).
3. Organize the dataset into the following structure:
    ```
    data/
        images/
            train/
            test/
            valid/
        labels/
            train/
            test/
            valid/
    ```

4. Update the `data.yaml` file to reflect the dataset structure:
    ```yaml
    train: data/images/train
    val: data/images/val

    nc: 52  # Number of classes (52 for a standard deck of cards)
    names: ['10C', '10D', ..., 'AS']
    ```

## Training the Model

1. Train the model using your custom dataset:
    ```bash
    python train.py --img 640 --batch 128 --epochs 200 --data data.yaml --weights yolov5s.pt
    ```

## Inference

1. After training, use the trained model to perform inference on new images or videos:
    ```bash
    python detect.py --weights best.pt --img 640 --conf 0.25 --source path/to/your/image_or_video
    ```

2. The results will be saved in the `runs/detect` directory.


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## Acknowledgments

- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)
- [LabelImg](https://github.com/tzutalin/labelImg)
- [Roboflow](https://roboflow.com)

---

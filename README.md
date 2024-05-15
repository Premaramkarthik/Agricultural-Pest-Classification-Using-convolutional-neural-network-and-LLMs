# Pest Classification Using Deep Learning

## Project Overview:

The "Pest Classification Using Deep Learning" project aims to develop an efficient and accurate system for identifying pests in agricultural settings using advanced convolutional neural networks (CNNs). The project addresses the critical need for effective pest control in agriculture by leveraging state-of-the-art deep learning techniques.

## Training and Performance Monitoring:

### Models Evaluated:
- ResNet50
- ResNet-101v4
- MobileNetv2
- YOLOv8
- EfficientNet

### Training Approach:
- Rigorous training with labeled datasets.
- Implementation of early stopping for ResNet50, ResNet-101v4, MobileNetv2, and EfficientNet to prevent overfitting.
- Continuous performance monitoring for YOLOv8 without early stopping.

## Performance Metrics and Model Selection:

### Evaluation Metrics:
- Confusion matrices
- Classification reports
- Metrics tracked: accuracy, precision, recall, specificity, F1-score

### Model Selection Criteria:
- Balance between accuracy and computational efficiency
- Comprehensive analysis of performance metrics for each model and pest class

## Deployment with Flask:

### Deployment Process:
- Development of a Flask application
- Creation of an API endpoint for real-time pest identification






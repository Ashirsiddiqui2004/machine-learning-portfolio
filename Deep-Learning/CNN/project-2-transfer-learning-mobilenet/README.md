## Cats vs Dogs – Transfer Learning (MobileNetV2)

This project uses transfer learning with a pretrained MobileNetV2
model to classify images of cats and dogs.

### Dataset
Cats vs Dogs dataset loaded using TensorFlow Datasets (tfds).

### Approach
- Pretrained MobileNetV2 as a frozen feature extractor
- Custom classification head
- Efficient training with minimal epochs

### Concepts Covered
- Transfer learning
- Feature reuse
- Overfitting reduction
- Binary image classification

import numpy as np

# -----------------------------
# Simple dataset (2 features)
# -----------------------------
X = np.array([
    [2, 3],
    [1, 5],
    [2, 8],
    [5, 2],
    [6, 3]
])

# Labels (0 = fail, 1 = pass)
y = np.array([[0], [0], [0], [1], [1]])

# -----------------------------
# Initialize parameters
# -----------------------------
np.random.seed(42)
weights = np.random.randn(2, 1)
bias = 0.0
learning_rate = 0.1

# -----------------------------
# Activation function
# -----------------------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# -----------------------------
# Loss function
# -----------------------------
def binary_cross_entropy(y_true, y_pred):
    return -np.mean(
        y_true * np.log(y_pred + 1e-8) +
        (1 - y_true) * np.log(1 - y_pred + 1e-8)
    )

# -----------------------------
# Training loop
# -----------------------------
epochs = 1000

for epoch in range(epochs):
    # Forward pass
    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)

    # Loss
    loss = binary_cross_entropy(y, y_pred)

    # Backpropagation
    dz = y_pred - y
    dw = np.dot(X.T, dz) / len(X)
    db = np.mean(dz)

    # Update weights
    weights -= learning_rate * dw
    bias -= learning_rate * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# -----------------------------
# Final predictions
# -----------------------------
predictions = (y_pred >= 0.5).astype(int)
print("\nFinal Predictions:")
print(predictions)



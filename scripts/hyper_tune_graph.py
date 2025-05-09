# -*- coding: utf-8 -*-
"""Hyperparameter_Tuning_graph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aO1X_BA-B1WhXUh8DWdHnL9cXofct2mF
"""
# Took assistence from chatgpt
# Imported all the important libraries
import matplotlib.pyplot as plt

# Full trial data
trials = [
    {
        'trial': 0,
        'best_val_loss': 0.5881,
        'best_accuracy': 0.7503,
        'val_losses': [0.6523, 0.6276, 0.6104, 0.5960, 0.5881]
    },
    {
        'trial': 1,
        'best_val_loss': 0.6019,
        'best_accuracy': 0.6595,
        'val_losses': [0.6558, 0.6371, 0.6209, 0.6134, 0.6019]
    },
    {
        'trial': 2,
        'best_val_loss': 0.5190,
        'best_accuracy': 0.7512,
        'val_losses': [0.6112, 0.5826, 0.5597, 0.5273, 0.5190]
    },
    {
        'trial': 3,
        'best_val_loss': 0.4552,
        'best_accuracy': 0.8469,
        'val_losses': [0.5818, 0.6043, 0.5654, 0.5187, 0.4552]
    },
    {
        'trial': 4,
        'best_val_loss': 0.2728,
        'best_accuracy': 0.8966,
        'val_losses': [0.4812, 0.4116, 0.3357, 0.2824, 0.2728]
    },
    {
        'trial': 5,
        'best_val_loss': 0.3388,
        'best_accuracy': 0.8926,
        'val_losses': [0.4949, 0.4139, 0.3916, 0.3468, 0.3388]
    },
    {
        'trial': 6,
        'best_val_loss': 0.2630,
        'best_accuracy': 0.9010,
        'val_losses': [0.4743, 0.4767, 0.3141, 0.2715, 0.2630]
    },
    {
        'trial': 7,
        'best_val_loss': 0.3275,
        'best_accuracy': 0.8995,
        'val_losses': [0.4516, 0.4183, 0.3719, 0.3477, 0.3275]
    },
    {
        'trial': 8,
        'best_val_loss': 0.6417,
        'best_accuracy': 0.7041,
        'val_losses': [0.6923, 0.6775, 0.6673, 0.6557, 0.6417]
    },
    {
        'trial': 9,
        'best_val_loss': 0.4627,
        'best_accuracy': 0.7908,
        'val_losses': [0.5142, 0.4627, 0.4842, 0.4659]  # Only 4 values
    }
]

# Plot: Validation Loss Over Epochs by Trial
plt.figure(figsize=(12, 8))
for trial in trials:
    epochs = range(1, len(trial['val_losses']) + 1)
    plt.plot(epochs, trial['val_losses'], label=f"Trial {trial['trial']}", marker='o')

plt.xlabel('Epoch')
plt.ylabel('Validation Loss')
plt.title('Validation Loss Over Epochs by Trial')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('val_loss_over_epochs.png')
plt.close()

print("Plot saved: 'val_loss_over_epochs.png'")

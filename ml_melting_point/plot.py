import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV files
lr_data = pd.read_csv('predicted_melting_points_lr.csv')
rf_data = pd.read_csv('predicted_melting_points_rf.csv')
mlp_data = pd.read_csv('predicted_melting_points_mlp.csv')
null_data = pd.read_csv('predicted_melting_points_null.csv')

min_mp=min(lr_data['Target_MP'])
max_mp=max(lr_data['Target_MP'])


# Create a 1:1 correlation line data
x = y = lr_data['Target_MP']

# Plot correlation heatmaps with adjusted dimensions
plt.figure(figsize=(14, 10))

# Linear Regression Model
plt.subplot(221)
plt.hist2d(lr_data['Target_MP'], lr_data['Predicted_MP'], bins=(100, 100), norm=mpl.colors.LogNorm(), cmap='YlOrRd',  range=[ [min_mp, max_mp], [min_mp, max_mp] ])
plt.plot(x, y, color='blue')  # 1:1 correlation line                                                                                                                                               
plt.title('Linear Regression')
plt.xlabel('True Melting Point (K)')
plt.ylabel('Predicted Melting Point (K)')

# Random Forest Model
plt.subplot(222)
plt.hist2d(rf_data['Target_MP'], rf_data['Predicted_MP'], bins=(100, 100), norm=mpl.colors.LogNorm(), cmap='YlOrRd',  range=[ [min_mp, max_mp], [min_mp, max_mp] ])
plt.plot(x, y, color='blue')  # 1:1 correlation line
plt.title('Random Forest')
plt.xlabel('True Melting Point (K)')
plt.ylabel('Predicted Melting Point (K)')

# MLP Regression Model
plt.subplot(223)
plt.hist2d(mlp_data['Target_MP'], mlp_data['Predicted_MP'], bins=(100, 100), norm=mpl.colors.LogNorm(), cmap='YlOrRd',  range=[ [min_mp, max_mp], [min_mp, max_mp] ])
plt.plot(x, y, color='blue')  # 1:1 correlation line
plt.title('MLP Regression')
plt.xlabel('True Melting Point (K)')
plt.ylabel('Predicted Melting Point (K)')

# Null Model
plt.subplot(224)
plt.hist2d(null_data['Target_MP'], null_data['Predicted_MP'], bins=(100, 100), norm=mpl.colors.LogNorm(), cmap='YlOrRd',  range=[ [min_mp, max_mp], [min_mp, max_mp] ])
plt.plot(x, y, color='blue')  # 1:1 correlation line
plt.title('Null Model')
plt.xlabel('True Melting Point (K)')
plt.ylabel('Predicted Melting Point (K)')

# Adjust layout
plt.tight_layout()

# Save the plot as PNG file
plt.savefig('ml_correlation.pdf')
plt.savefig('mp_correlation.png')

# Show the plot
plt.show()

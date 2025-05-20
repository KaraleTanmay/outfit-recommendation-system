import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set style for visualizations
sns.set(style="whitegrid")
plt.rcParams['font.size'] = 12

# Create output directory
output_dir = "preferences_visualisations"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("outfit_dataset.csv")

# Formality-Fit mapping
formality_fit = {
    "Formal": ["Slim Fit", "Regular Fit"],
    "Semi-Formal": ["Slim Fit", "Regular Fit", "Athletic Fit"],
    "Smart Casual": ["Slim Fit", "Regular Fit", "Relaxed Fit", "Athletic Fit"],
    "Casual": ["Slim Fit", "Regular Fit", "Relaxed Fit", "Oversized", "Athletic Fit"]
}

# Define heatmap combinations
heatmap_combinations = [
    ('Occasion', 'Style', 'heatmap_occasion_style.png', 'Occasion vs. Style'),
    ('Occasion', 'Venue', 'heatmap_occasion_venue.png', 'Occasion vs. Venue'),
    ('Occasion', 'Fit', 'heatmap_occasion_fit.png', 'Occasion vs. Fit'),
    ('Occasion', 'Formality Level', 'heatmap_occasion_formality.png', 'Occasion vs. Formality Level'),
    ('Weather', 'Style', 'heatmap_weather_style.png', 'Weather vs. Style'),
    ('Weather', 'Fit', 'heatmap_weather_fit.png', 'Weather vs. Fit'),
    ('Style', 'Venue', 'heatmap_style_venue.png', 'Style vs. Venue'),
    ('Style', 'Formality Level', 'heatmap_style_formality.png', 'Style vs. Formality Level'),
    ('Style', 'Fit', 'heatmap_style_fit.png', 'Style vs. Fit'),
    ('Venue', 'Fit', 'heatmap_venue_fit.png', 'Venue vs. Fit'),
    ('Venue', 'Formality Level', 'heatmap_venue_formality.png', 'Venue vs. Formality Level'),
    ('Fit', 'Formality Level', 'heatmap_fit_formality.png', 'Fit vs. Formality Level')
]


# Function to plot heatmap
def plot_heatmap(data, row_col, col_col, title, filename, figsize=(12, 8)):
    pivot = pd.crosstab(data[row_col], data[col_col])
    plt.figure(figsize=figsize)
    sns.heatmap(pivot, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Count'})
    plt.title(title)
    plt.xlabel(col_col)
    plt.ylabel(row_col)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()


# Generate heatmaps
for row_col, col_col, filename, title in heatmap_combinations:
    plot_heatmap(df, row_col, col_col, title, filename, figsize=(14, 10) if col_col in ['Style', 'Venue'] else (12, 8))





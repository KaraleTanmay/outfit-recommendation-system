import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set style for visualizations
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams['font.size'] = 12

# Create output directory
output_dir = "outfit_visualizations"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("outfit_dataset.csv")

# Split by gender
df_male = df[df['Gender'] == 'Male'].copy()
df_female = df[df['Gender'] == 'Female'].copy()

# Valid Occasion-Venue-Formality-Style combinations (from dataset rules)
valid_combinations = [
    {"Occasion": "Business Meeting", "Venue": ["Office", "Restaurant"], "Formality Level": ["Formal", "Semi-Formal"],
     "Style": ["Classic"]},
    {"Occasion": "Party", "Venue": ["Club", "Restaurant", "Beach"], "Formality Level": ["Smart Casual", "Casual"],
     "Style": ["Streetwear", "Bold", "Vintage", "Vacation"]},
    {"Occasion": "Wedding", "Venue": ["Wedding Hall", "Temple"], "Formality Level": ["Formal", "Semi-Formal"],
     "Style": ["Classic", "Traditional"]},
    {"Occasion": "Date", "Venue": ["Restaurant", "Club", "Shopping Mall"],
     "Formality Level": ["Semi-Formal", "Smart Casual"], "Style": ["Classic", "Vintage", "Bold"]},
    {"Occasion": "Outdoor", "Venue": ["Beach", "Mountain"], "Formality Level": ["Casual"],
     "Style": ["Sporty", "Vacation"]},
    {"Occasion": "Sports", "Venue": ["Gym", "Beach", "Mountain"], "Formality Level": ["Casual"], "Style": ["Sporty"]},
    {"Occasion": "Vacation", "Venue": ["Beach", "Mountain", "Shopping Mall"],
     "Formality Level": ["Smart Casual", "Casual"], "Style": ["Vacation", "Streetwear"]},
    {"Occasion": "Cultural Event", "Venue": ["Temple", "Wedding Hall", "College"],
     "Formality Level": ["Formal", "Semi-Formal", "Smart Casual"], "Style": ["Traditional", "Classic"]},
    {"Occasion": "Cultural Event", "Venue": ["College"], "Formality Level": ["Smart Casual", "Casual"],
     "Style": ["Streetwear", "Vintage"]}
]

# 1. Heatmaps for Occasion-Based Combinations (Venue vs. Formality Level)
occasions = ["Business Meeting", "Party", "Wedding", "Date", "Outdoor", "Sports", "Vacation", "Cultural Event"]

for occasion in occasions:
    # Filter dataset for the occasion and valid combinations
    valid_combos = [c for c in valid_combinations if c["Occasion"] == occasion]
    valid_venues = set()
    valid_formalities = set()
    valid_styles = set()
    for combo in valid_combos:
        valid_venues.update(combo["Venue"])
        valid_formalities.update(combo["Formality Level"])
        valid_styles.update(combo["Style"])

    df_occasion = df[(df['Occasion'] == occasion) &
                     (df['Venue'].isin(valid_venues)) &
                     (df['Formality Level'].isin(valid_formalities)) &
                     (df['Style'].isin(valid_styles))]

    # Create pivot table for heatmap
    pivot = pd.crosstab(df_occasion['Venue'], df_occasion['Formality Level'])

    # Plot heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'})
    plt.title(f'Venue vs. Formality Level for {occasion}')
    plt.xlabel('Formality Level')
    plt.ylabel('Venue')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'heatmap_occasion_{occasion.lower().replace(" ", "_")}_venue_formality.png'))
    plt.close()


# 2. Pie Charts for Outfit Attributes
def plot_pie_chart(data, column, title, filename, threshold=0.02):
    counts = data[column].value_counts(normalize=True)
    # Group values below threshold into 'Other'
    other = counts[counts < threshold].sum()
    counts = counts[counts >= threshold]
    if other > 0:
        counts['Other'] = other
    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90,
            colors=sns.color_palette('pastel', len(counts)))
    plt.title(title)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()


# Define attributes to visualize
attributes = [
    ('Topwear Type', 'pie_{gender}_topwear_type.png', 'Topwear Type Distribution ({gender})'),
    ('Bottomwear Type', 'pie_{gender}_bottomwear_type.png', 'Bottomwear Type Distribution ({gender})'),
    ('One-Piece Type', 'pie_{gender}_one_piece_type.png', 'One-Piece Type Distribution ({gender})'),
    ('Footwear Type', 'pie_{gender}_footwear_type.png', 'Footwear Type Distribution ({gender})'),
    ('Topwear Color', 'pie_{gender}_topwear_color.png', 'Topwear Color Distribution ({gender})'),
    ('Bottomwear Color', 'pie_{gender}_bottomwear_color.png', 'Bottomwear Color Distribution ({gender})'),
    ('One-Piece Color', 'pie_{gender}_one_piece_color.png', 'One-Piece Color Distribution ({gender})'),
    ('Footwear Color', 'pie_{gender}_footwear_color.png', 'Footwear Color Distribution ({gender})'),
    ('Topwear Fabric', 'pie_{gender}_topwear_fabric.png', 'Topwear Fabric Distribution ({gender})'),
    ('Bottomwear Fabric', 'pie_{gender}_bottomwear_fabric.png', 'Bottomwear Fabric Distribution ({gender})'),
    ('One-Piece Fabric', 'pie_{gender}_one_piece_fabric.png', 'One-Piece Fabric Distribution ({gender})'),
    ('Bottomwear Length', 'pie_{gender}_bottomwear_length.png', 'Bottomwear Length Distribution ({gender})'),
    ('One-Piece Length', 'pie_{gender}_one_piece_length.png', 'One-Piece Length Distribution ({gender})')
]

for gender, df_gender in [('Male', df_male), ('Female', df_female)]:
    for attr, filename_template, title_template in attributes:
        # Skip empty or irrelevant entries
        df_filtered = df_gender[df_gender[attr].notna() & (df_gender[attr] != '')]
        if len(df_filtered) == 0:
            continue
        plot_pie_chart(
            df_filtered,
            attr,
            title_template.format(gender=gender),
            filename_template.format(gender=gender.lower()),
            threshold=0.02
        )


# 3. Heatmaps for Outfit Combinations
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


# Combinations to visualize
combinations = [
    ('Topwear Type', 'Bottomwear Type', 'heatmap_{gender}_topwear_bottomwear.png',
     'Topwear Type vs. Bottomwear Type ({gender})'),
    ('Bottomwear Type', 'Footwear Type', 'heatmap_{gender}_bottomwear_footwear.png',
     'Bottomwear Type vs. Footwear Type ({gender})'),
    ('Topwear Type', 'Topwear Color', 'heatmap_{gender}_topwear_type_color.png',
     'Topwear Type vs. Topwear Color ({gender})'),
    ('Bottomwear Type', 'Bottomwear Color', 'heatmap_{gender}_bottomwear_type_color.png',
     'Bottomwear Type vs. Bottomwear Color ({gender})'),
    ('Footwear Type', 'Footwear Color', 'heatmap_{gender}_footwear_type_color.png',
     'Footwear Type vs. Footwear Color ({gender})')
]

for gender, df_gender in [('Male', df_male), ('Female', df_female)]:
    for row_col, col_col, filename_template, title_template in combinations:
        # Filter non-empty entries
        df_filtered = df_gender[(df_gender[row_col].notna()) & (df_gender[row_col] != '') &
                                (df_gender[col_col].notna()) & (df_gender[col_col] != '')]
        if len(df_filtered) == 0:
            continue
        plot_heatmap(
            df_filtered,
            row_col,
            col_col,
            title_template.format(gender=gender),
            filename_template.format(gender=gender.lower()),
            figsize=(14, 10) if 'Color' in col_col else (12, 8)
        )

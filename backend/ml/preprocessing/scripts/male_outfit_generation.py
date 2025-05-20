import csv
import random
from collections import Counter

# Define male parameter values with updated footwear
parameters = {
    "Gender": ["Male"],
    "Occasion": ["Business Meeting", "Party", "Wedding", "Date", "Outdoor", "Sports", "Vacation", "Cultural Event"],
    "Weather": ["Dry", "Humid", "Rainy", "Windy", "Snowy", "Mild"],
    "Style": ["Classic", "Sporty", "Streetwear", "Traditional", "Vintage", "Bold", "Vacation"],
    "Venue": ["Office", "Club", "Wedding Hall", "Restaurant", "Beach", "Mountain", "Gym", "Temple", "College",
              "Shopping Mall"],
    "Fit": ["Slim Fit", "Regular Fit", "Relaxed Fit", "Oversized", "Athletic Fit"],
    "Formality Level": ["Formal", "Semi-Formal", "Smart Casual", "Casual"],
    "Skin Tone": ["Fair", "Light", "Medium", "Tan", "Dark"],
    "Topwear Type": ["Shirt", "T-Shirt", "Sweatshirt", "Hoodie", "Polo Shirt", "Sweater", "Tank Top", "Kurta", "Jersey",
                     ""],
    "Topwear Neck Type": ["Round Neck", "V-Neck", "Crew Neck", "Collared", "Button-Down Collar", "Turtle Neck",
                          "Chinese Collar", ""],
    "Sleeve Type": ["Sleeveless", "Short Sleeve", "Long Sleeve", "Roll-Up Sleeve", "3/4 Sleeve", "Rolled-up Sleeve",
                    ""],
    "Topwear Pattern": ["Solid", "Striped", "Checked", "Colorblock", "Graphic Print", "Gradient", "Houndstooth",
                        "Argyle", "Pinstripe", "Camouflage", ""],
    "Topwear Fabric": ["Cotton", "Linen", "Denim", "Polyester", "Silk", "Wool", "Velvet", "Knitted", "Leather", ""],
    "Topwear Color": ["White", "Black", "Navy Blue", "Sky Blue", "Beige", "Grey", "Brown", "Olive Green", "Red/Maroon",
                      "Pink", "Yellow", "Purple", "Khaki", "Teal", "Metallic", ""],
    "Bottomwear Type": ["Jeans", "Trousers", "Shorts", "Joggers", "Cargo Pants", "Pajamas", "Chinos", "Formal Pants",
                        "Bermudas", "Lungis/Dhoti", ""],
    "Bottomwear Length": ["Full Length", "Cropped", "Knee-Length", "Above Knee", "3/4 Length", "Ankle-Length", ""],
    "Bottomwear Pattern": ["Solid", "Striped", "Checkered", "Denim Wash", "Camouflage", ""],
    "Bottomwear Fabric": ["Cotton", "Denim", "Linen", "Polyester", "Wool", "Leather", "Velvet", ""],
    "Bottomwear Color": ["White", "Black", "Navy Blue", "Sky Blue", "Beige", "Grey", "Brown", "Olive Green", "Maroon",
                         "Pink", "Mustard", "Lavender", "Khaki", "Teal", "Metallic", ""],
    "Footwear Type": ["Formal Shoes", "Loafers", "Sneakers", "Boots", "Sports Shoes", "Sandals"],
    "Footwear Color": ["Black", "White", "Brown", "Navy", "Grey", "Maroon", "Olive Green", "Metallic"],
    "One-Piece Type": ["Kurta Set", "Sherwani", "Bandhgala", "Pathani Suit", "Jumpsuit", ""],
    "One-Piece Length": ["Full-Length", "Knee-Length", "Calf-Length", "Ankle-Length", ""],
    "One-Piece Fabric": ["Cotton", "Silk", "Linen", "Velvet", "Khadi", "Jacquard", ""],
    "One-Piece Color": ["White", "Black", "Navy Blue", "Sky Blue", "Beige", "Grey", "Brown", "Olive Green",
                        "Red/Maroon", "Pink", "Mustard", "Lavender", "Khaki", "Teal", "Metallic", ""],
    "One-Piece Pattern": ["Solid", "Embroidered", "Zari", "Brocade", "Paisley", "Textured Weave", ""],
    "Layering Type": ["Blazer", "Jacket", "Hoodie", "Cardigan", "Sweater", "Overcoat", "Windcheater", "Raincoat",
                      "Waistcoat", "Nehru Jacket", "Bomber Jacket", "Trench Coat", ""],
    "Layering Pattern": ["Solid", "Striped", "Checked", "Houndstooth", "Gradient", "Embroidered", ""],
    "Layering Fabric": ["Cotton", "Wool", "Polyester", "Denim", "Leather", "Knitted", "Nylon", "Fleece", "Silk",
                        "Velvet", "Khadi", "Tweed", ""],
    "Layering Color": ["Black", "White", "Gray", "Navy", "Brown", "Beige", "Olive Green", "Maroon", "Pastel Pink",
                       "Mustard Yellow", "Teal", "Khaki", "Gold", "Silver", "Red", "Royal Blue", "Emerald Green", ""],
    "Watch Type": ["Analog", "Digital", "Smartwatch", ""],
    "Watch Strap Type": ["Leather", "Metal", "Silicone", "Nylon", ""],
    "Watch Color": ["Black", "Brown", "Silver", "Gold", "White", ""],
    "Belt Material": ["Leather", "Canvas", "Braided Fabric", "Ethnic Fabric", ""],
    "Belt Color": ["Black", "Brown", "Tan", "White", "Navy", "Patterned", ""],
    "Hat Type": ["Baseball Cap", "Beanie", "Bucket Hat", "Turban", "Beret", "Sunhat", ""],
    "Cap/Hat Color": ["Black", "White", "Navy", "Brown", "Olive Green", "Khaki", "Patterned", ""],
    "Neck/Bow/Tie": ["Tie", "Bow Tie", "Scarf", "Necklace – Minimal", "Chain", "Traditional", ""],
    "Earrings": ["Studs", ""],
    "Fragrance": ["Fresh/Citrus", "Woody", "Spicy", "Musky", "Oriental", "Aquatic", ""]
}

# Predefined valid Occasion-Venue-Formality-Style combinations with updated College rule
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

# Weather-Fabric mapping
weather_fabric = {
    "Humid": ["Cotton", "Linen", "Polyester"],
    "Rainy": ["Polyester", "Nylon"],
    "Snowy": ["Wool", "Fleece"],
    "Windy": ["Denim", "Wool"],
    "Dry": [f for f in parameters["Topwear Fabric"] if f != ""],
    "Mild": [f for f in parameters["Topwear Fabric"] if f != ""]
}

# Formality-Fit mapping
formality_fit = {
    "Formal": ["Slim Fit", "Regular Fit"],
    "Semi-Formal": ["Slim Fit", "Regular Fit", "Athletic Fit"],
    "Smart Casual": ["Slim Fit", "Regular Fit", "Relaxed Fit", "Athletic Fit"],
    "Casual": parameters["Fit"]
}

# Formality-Footwear mapping with updated types
formality_footwear = {
    "Formal": ["Formal Shoes"],
    "Semi-Formal": ["Formal Shoes", "Loafers"],
    "Smart Casual": ["Loafers", "Sneakers"],
    "Casual": ["Sneakers", "Boots", "Sports Shoes", "Sandals"]
}


# Color matching based on skin tone
def get_valid_colors(skin_tone, item_type):
    color_options = parameters[f"{item_type} Color"]
    color_options = [c for c in color_options if c != ""]
    if skin_tone == "Fair":
        return [c for c in color_options if c not in ["White", "Beige"]]
    elif skin_tone == "Light":
        return [c for c in color_options if c not in ["Yellow", "Pink"]]
    elif skin_tone == "Medium":
        return color_options
    elif skin_tone == "Tan":
        return [c for c in color_options if c not in ["Pastel Pink", "Lavender"]]
    elif skin_tone == "Dark":
        return [c for c in color_options if c not in ["Grey", "Brown"]]
    return color_options


# Generate a single valid row
def generate_valid_row(triplet_counter):
    # Select a valid combination
    combo = random.choice(valid_combinations)
    row = {
        "Gender": "Male",
        "Occasion": combo["Occasion"],
        "Venue": random.choice(combo["Venue"]),
        "Formality Level": random.choice(combo["Formality Level"]),
        "Style": random.choice(combo["Style"])
    }

    # Check if this triplet is underrepresented
    triplet = (row["Occasion"], row["Venue"], row["Formality Level"])
    if triplet_counter.get(triplet, 0) >= 25:
        # Try another combination to prioritize underrepresented triplets
        for _ in range(10):  # Limit retries to avoid infinite loops
            combo = random.choice(valid_combinations)
            row["Venue"] = random.choice(combo["Venue"])
            row["Formality Level"] = random.choice(combo["Formality Level"])
            row["Style"] = random.choice(combo["Style"])
            triplet = (row["Occasion"], row["Venue"], row["Formality Level"])
            if triplet_counter.get(triplet, 0) < 25:
                break

    # Weather and Skin Tone
    row["Weather"] = random.choice(parameters["Weather"])
    row["Skin Tone"] = random.choice(parameters["Skin Tone"])

    # Fit
    row["Fit"] = random.choice(formality_fit[row["Formality Level"]])

    # Decide if this is a one-piece outfit
    is_one_piece = (row["Occasion"] in ["Cultural Event", "Wedding"] and random.random() < 0.5) or \
                   (row["Style"] == "Traditional" and random.random() < 0.7) or \
                   (row["Formality Level"] in ["Formal", "Semi-Formal"] and random.random() < 0.3)

    if is_one_piece:
        # One-Piece outfit: clear topwear and bottomwear
        row["Topwear Type"] = row["Topwear Neck Type"] = row["Sleeve Type"] = \
            row["Topwear Pattern"] = row["Topwear Fabric"] = row["Topwear Color"] = ""
        row["Bottomwear Type"] = row["Bottomwear Length"] = row["Bottomwear Pattern"] = \
            row["Bottomwear Fabric"] = row["Bottomwear Color"] = ""

        # Set one-piece properties
        one_piece_types = ["Kurta Set", "Sherwani", "Bandhgala", "Pathani Suit", "Jumpsuit"]
        row["One-Piece Type"] = random.choice(one_piece_types)
        row["One-Piece Length"] = random.choice([t for t in parameters["One-Piece Length"] if t != ""])
        row["One-Piece Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["One-Piece Color"] = random.choice(get_valid_colors(row["Skin Tone"], "One-Piece"))
        row["One-Piece Pattern"] = random.choice(["Embroidered", "Zari", "Brocade"]) if row["One-Piece Type"] in [
            "Sherwani", "Bandhgala"] else \
            random.choice([t for t in parameters["One-Piece Pattern"] if t != ""])
    else:
        # Non-one-piece outfit: set topwear and bottomwear
        row["One-Piece Type"] = row["One-Piece Length"] = row["One-Piece Fabric"] = \
            row["One-Piece Color"] = row["One-Piece Pattern"] = ""

        # Topwear
        topwear_types = ["Shirt"] if row["Formality Level"] in ["Formal", "Semi-Formal"] else \
            [t for t in parameters["Topwear Type"] if t != ""]
        row["Topwear Type"] = random.choice(topwear_types)
        row["Topwear Neck Type"] = "Collared" if row["Topwear Type"] == "Shirt" else \
            random.choice([t for t in parameters["Topwear Neck Type"] if t != ""])
        row["Sleeve Type"] = random.choice([t for t in parameters["Sleeve Type"] if t != ""])
        row["Topwear Pattern"] = random.choice(["Solid", "Striped", "Pinstripe"]) if row[
                                                                                         "Formality Level"] == "Formal" else \
            random.choice([t for t in parameters["Topwear Pattern"] if t != ""])
        row["Topwear Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["Topwear Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Topwear"))

        # Bottomwear
        bottomwear_types = ["Formal Pants", "Trousers"] if row["Formality Level"] == "Formal" else \
            [t for t in parameters["Bottomwear Type"] if t != ""]
        row["Bottomwear Type"] = random.choice(bottomwear_types)
        row["Bottomwear Length"] = "Full Length" if row["Formality Level"] in ["Formal", "Semi-Formal"] else \
            random.choice([t for t in parameters["Bottomwear Length"] if t != ""])
        row["Bottomwear Pattern"] = "Solid" if row["Topwear Pattern"] in ["Striped", "Checked", "Graphic Print"] else \
            random.choice([t for t in parameters["Bottomwear Pattern"] if t != ""])
        row["Bottomwear Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["Bottomwear Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Bottomwear"))

        # Ensure color coordination
        neutral_colors = ["Black", "White", "Grey", "Navy Blue", "Beige"]
        if row["Topwear Color"] not in neutral_colors:
            row["Bottomwear Color"] = random.choice(neutral_colors)

    # Footwear (always included, updated types and colors)
    row["Footwear Type"] = random.choice(formality_footwear[row["Formality Level"]])
    row["Footwear Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Footwear"))

    # Layering (optional, 50% chance)
    if row["Weather"] not in ["Humid", "Rainy"] and row["Occasion"] not in ["Sports"] and random.random() < 0.5:
        layering_types = ["Blazer", "Waistcoat"] if row["Formality Level"] == "Formal" else \
            [t for t in parameters["Layering Type"] if t != ""]
        row["Layering Type"] = random.choice(layering_types)
        row["Layering Pattern"] = random.choice([t for t in parameters["Layering Pattern"] if t != ""])
        row["Layering Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["Layering Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Layering"))
    else:
        row["Layering Type"] = row["Layering Pattern"] = row["Layering Fabric"] = row["Layering Color"] = ""

    # Accessories (optional)
    if row["Occasion"] not in ["Sports", "Outdoor"] and random.random() < 0.9:
        row["Watch Type"] = random.choice([t for t in parameters["Watch Type"] if t != ""])
        row["Watch Strap Type"] = "Leather" if row["Formality Level"] == "Formal" else \
            random.choice([t for t in parameters["Watch Strap Type"] if t != ""])
        row["Watch Color"] = random.choice([t for t in parameters["Watch Color"] if t != ""])
    else:
        row["Watch Type"] = row["Watch Strap Type"] = row["Watch Color"] = ""

    if row["Occasion"] not in ["Sports", "Outdoor"] and random.random() < 0.9:
        row["Belt Material"] = "Leather" if row["Formality Level"] == "Formal" else \
            random.choice([t for t in parameters["Belt Material"] if t != ""])
        row["Belt Color"] = row["Footwear Color"] if row["Formality Level"] in ["Formal", "Semi-Formal"] else \
            random.choice([t for t in parameters["Belt Color"] if t != ""])
    else:
        row["Belt Material"] = row["Belt Color"] = ""

    if row["Occasion"] in ["Outdoor", "Vacation"] and random.random() < 0.3:
        row["Hat Type"] = random.choice([t for t in parameters["Hat Type"] if t != ""])
        row["Cap/Hat Color"] = random.choice([t for t in parameters["Cap/Hat Color"] if t != ""])
    else:
        row["Hat Type"] = row["Cap/Hat Color"] = ""

    if row["Formality Level"] == "Formal":
        row["Neck/Bow/Tie"] = random.choice(["Tie", "Bow Tie"])
    elif row["Occasion"] == "Cultural Event" and random.random() < 0.6:
        row["Neck/Bow/Tie"] = "Traditional"
    elif random.random() < 0.3:
        row["Neck/Bow/Tie"] = random.choice(["Scarf", "Necklace – Minimal", "Chain"])
    else:
        row["Neck/Bow/Tie"] = ""

    row["Earrings"] = "Studs" if row["Style"] in ["Streetwear", "Bold"] and random.random() < 0.15 else ""

    row["Fragrance"] = random.choice(["Woody", "Musky"]) if row["Formality Level"] == "Formal" else \
        random.choice([t for t in parameters["Fragrance"] if t != ""]) if random.random() < 0.8 else ""

    return row, triplet


# Generate 3000 entries
dataset = []
triplet_counter = Counter()
target_entries = 3000

while len(dataset) < target_entries:
    row, triplet = generate_valid_row(triplet_counter)
    triplet_counter[triplet] += 1
    dataset.append(row)

# Write to CSV
fieldnames = list(parameters.keys())
with open("male_outfit_dataset_3000.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in dataset:
        writer.writerow(row)


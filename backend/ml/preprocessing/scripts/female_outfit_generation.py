import csv
import random
from collections import Counter

# Define female parameters
female_parameters = {
    "Gender": ["Female"],
    "Occasion": ["Business Meeting", "Party", "Wedding", "Date", "Outdoor", "Sports", "Vacation", "Cultural Event"],
    "Weather": ["Dry", "Humid", "Rainy", "Windy", "Snowy", "Mild"],
    "Style": ["Classic", "Sporty", "Streetwear", "Traditional", "Vintage", "Bold", "Vacation"],
    "Venue": ["Office", "Club", "Wedding Hall", "Restaurant", "Beach", "Mountain", "Gym", "Temple", "College",
              "Shopping Mall"],
    "Fit": ["Slim Fit", "Regular Fit", "Relaxed Fit", "Oversized", "Athletic Fit"],
    "Formality Level": ["Formal", "Semi-Formal", "Smart Casual", "Casual"],
    "Skin Tone": ["Fair", "Light", "Medium", "Tan", "Dark"],
    "Topwear Type": ["Blouse", "T-Shirt", "Crop Top", "Shirt", "Sweatshirt", "Hoodie", "Polo Shirt", "Tunic",
                     "Tank Top", ""],
    "Topwear Neck Type": ["Round Neck", "V-Neck", "Scoop Neck", "Collared", "Off-Shoulder", "Boat Neck", "Halter Neck",
                          ""],
    "Sleeve Type": ["Sleeveless", "Short Sleeve", "Long Sleeve", "3/4 Sleeve", "Bell Sleeve", "Puff Sleeve", ""],
    "Topwear Pattern": ["Solid", "Striped", "Checked", "Floral", "Graphic Print", "Polka Dot", "Houndstooth",
                        "Pinstripe", "Animal Print", "Geometric", ""],
    "Topwear Fabric": ["Cotton", "Linen", "Silk", "Polyester", "Chiffon", "Wool", "Velvet", "Knitted", "Lace", ""],
    "Topwear Color": ["White", "Black", "Navy Blue", "Sky Blue", "Beige", "Grey", "Brown", "Olive Green", "Red/Maroon",
                      "Pink", "Yellow", "Purple", "Khaki", "Teal", "Metallic", ""],
    "Bottomwear Type": ["Skirt", "Jeans", "Trousers", "Leggings", "Palazzo Pants", "Shorts", "Chinos", "Formal Pants",
                        "Joggers", "Dhoti Pants", ""],
    "Bottomwear Length": ["Full Length", "Cropped", "Knee-Length", "Above Knee", "Ankle-Length", "Midi", ""],
    "Bottomwear Pattern": ["Solid", "Striped", "Floral", "Polka Dot", "Animal Print", ""],
    "Bottomwear Fabric": ["Cotton", "Denim", "Linen", "Polyester", "Silk", "Wool", "Chiffon", ""],
    "Bottomwear Color": ["White", "Black", "Navy Blue", "Sky Blue", "Beige", "Grey", "Brown", "Olive Green", "Maroon",
                         "Pink", "Mustard", "Lavender", "Khaki", "Teal", "Metallic", ""],
    "Footwear Type": ["Heels", "Flats", "Sneakers", "Boots", "Sandals", "Wedges", "Ballet Flats"],
    "Footwear Color": ["Black", "White", "Navy", "Beige", "Grey", "Maroon", "Pink", "Mustard", "Khaki", "Teal",
                       "Metallic", "Gold", "Silver", "Red"],
    "One-Piece Type": ["Dress", "Saree", "Lehenga", "Anarkali Suit", "Kurta Set", "Jumpsuit", ""],
    "One-Piece Length": ["Full-Length", "Knee-Length", "Midi", "Ankle-Length", ""],
    "One-Piece Fabric": ["Cotton", "Silk", "Chiffon", "Georgette", "Velvet", "Linen", ""],
    "One-Piece Color": ["White", "Black", "Navy Blue", "Sky Blue", "Beige", "Grey", "Brown", "Olive Green",
                        "Red/Maroon", "Pink", "Mustard", "Lavender", "Khaki", "Teal", "Metallic", ""],
    "One-Piece Pattern": ["Solid", "Embroidered", "Floral", "Zari", "Printed", "Sequined", ""],
    "Layering Type": ["Blazer", "Cardigan", "Shrug", "Jacket", "Sweater", "Shawl", "Kimono", "Cape", "Trench Coat",
                      "Denim Jacket", ""],
    "Layering Pattern": ["Solid", "Striped", "Checked", "Floral", "Houndstooth", "Polka Dot", ""],
    "Layering Fabric": ["Cotton", "Wool", "Polyester", "Denim", "Silk", "Knitted", "Chiffon", "Linen", "Velvet", ""],
    "Layering Color": ["Black", "White", "Gray", "Navy", "Beige", "Olive Green", "Maroon", "Pastel Pink",
                       "Mustard Yellow", "Teal", "Khaki", "Red", "Royal Blue", "Emerald Green", ""],
    "Watch Type": ["Analog", "Digital", "Smartwatch", ""],
    "Watch Strap Type": ["Leather", "Metal", "Silicone", "Mesh", ""],
    "Watch Color": ["Black", "Brown", "Silver", "Gold", "Rose Gold", ""],
    "Belt Material": ["Leather", "Fabric", "Chain", ""],
    "Belt Color": ["Black", "Brown", "White", "Gold", "Silver", "Patterned", ""],
    "Hat Type": ["Sunhat", "Beanie", "Beret", "Cap", "Headscarf", ""],
    "Cap/Hat Color": ["Black", "White", "Navy", "Beige", "Pink", "Patterned", ""],
    "Neck/Bow/Tie": ["Scarf", "Statement Necklace", "Choker", "Pendant", ""],
    "Earrings": ["Studs", "Hoops", "Danglers", "Chandelier", ""],
    "Bangles": ["Metal Bangles", "Beaded Bracelets", "Cuff", ""],
    "Fragrance": ["Floral", "Fruity", "Woody", "Musky", "Citrus", "Oriental", ""]
}

# Updated valid_combinations with adjusted Formality and Style rules
valid_combinations = [
    # Business Meeting: Office (Formal, Classic) or Restaurant (Semi-Formal, Classic)
    {"Occasion": "Business Meeting", "Venue": ["Office"], "Formality Level": ["Formal"], "Style": ["Classic"]},
    {"Occasion": "Business Meeting", "Venue": ["Restaurant"], "Formality Level": ["Semi-Formal"], "Style": ["Classic"]},
    # Party: Club (Smart Casual, Streetwear/Bold), Restaurant (Semi-Formal/Smart Casual/Casual, Bold/Vintage)
    {"Occasion": "Party", "Venue": ["Club"], "Formality Level": ["Smart Casual"], "Style": ["Streetwear", "Bold"]},
    {"Occasion": "Party", "Venue": ["Restaurant"], "Formality Level": ["Semi-Formal"], "Style": ["Bold", "Vintage"]},
    {"Occasion": "Party", "Venue": ["Restaurant"], "Formality Level": ["Smart Casual", "Casual"],
     "Style": ["Bold", "Vintage"]},
    # Wedding: Wedding Hall (Formal, Classic/Traditional) or Temple (Formal/Semi-Formal, Traditional)
    {"Occasion": "Wedding", "Venue": ["Wedding Hall"], "Formality Level": ["Formal"],
     "Style": ["Classic", "Traditional"]},
    {"Occasion": "Wedding", "Venue": ["Temple"], "Formality Level": ["Formal", "Semi-Formal"],
     "Style": ["Traditional"]},
    # Date: Restaurant (Semi-Formal, Classic/Vintage), Club (Smart Casual, Bold), Shopping Mall (Smart Casual/Casual, Streetwear/Vintage)
    {"Occasion": "Date", "Venue": ["Restaurant"], "Formality Level": ["Semi-Formal"], "Style": ["Classic", "Vintage"]},
    {"Occasion": "Date", "Venue": ["Club"], "Formality Level": ["Smart Casual"], "Style": ["Bold"]},
    {"Occasion": "Date", "Venue": ["Shopping Mall"], "Formality Level": ["Smart Casual", "Casual"],
     "Style": ["Streetwear", "Vintage"]},
    # Outdoor: Beach (Casual/Smart Casual, Vacation/Streetwear), Mountain (Casual/Smart Casual, Sporty/Streetwear)
    {"Occasion": "Outdoor", "Venue": ["Beach"], "Formality Level": ["Casual"], "Style": ["Vacation"]},
    {"Occasion": "Outdoor", "Venue": ["Beach"], "Formality Level": ["Smart Casual"], "Style": ["Streetwear"]},
    {"Occasion": "Outdoor", "Venue": ["Mountain"], "Formality Level": ["Casual"], "Style": ["Sporty"]},
    {"Occasion": "Outdoor", "Venue": ["Mountain"], "Formality Level": ["Smart Casual"], "Style": ["Streetwear"]},
    # Sports: Gym/Beach/Mountain (Casual, Sporty/Streetwear)
    {"Occasion": "Sports", "Venue": ["Gym"], "Formality Level": ["Casual"], "Style": ["Sporty", "Streetwear"]},
    {"Occasion": "Sports", "Venue": ["Beach"], "Formality Level": ["Casual"], "Style": ["Sporty", "Streetwear"]},
    {"Occasion": "Sports", "Venue": ["Mountain"], "Formality Level": ["Casual"], "Style": ["Sporty", "Streetwear"]},
    # Vacation: Beach (Casual, Vacation), Mountain (Casual, Vacation), Shopping Mall (Smart Casual, Streetwear)
    {"Occasion": "Vacation", "Venue": ["Beach"], "Formality Level": ["Casual"], "Style": ["Vacation"]},
    {"Occasion": "Vacation", "Venue": ["Mountain"], "Formality Level": ["Casual"], "Style": ["Vacation"]},
    {"Occasion": "Vacation", "Venue": ["Shopping Mall"], "Formality Level": ["Smart Casual"], "Style": ["Streetwear"]},
    # Cultural Event: Temple (Formal, Traditional), Wedding Hall (Semi-Formal, Traditional/Classic), College (Smart Casual/Casual, Traditional/Classic/Vintage)
    {"Occasion": "Cultural Event", "Venue": ["Temple"], "Formality Level": ["Formal"], "Style": ["Traditional"]},
    {"Occasion": "Cultural Event", "Venue": ["Wedding Hall"], "Formality Level": ["Semi-Formal"],
     "Style": ["Traditional", "Classic"]},
    {"Occasion": "Cultural Event", "Venue": ["College"], "Formality Level": ["Smart Casual", "Casual"],
     "Style": ["Traditional", "Classic", "Vintage"]}
]

# Weather-Fabric mappings
weather_fabric = {
    "Humid": ["Cotton", "Linen", "Chiffon", "Polyester"],
    "Rainy": ["Polyester"],
    "Snowy": ["Wool", "Knitted"],
    "Windy": ["Denim", "Wool"],
    "Dry": [f for f in female_parameters["Topwear Fabric"] if f != ""],
    "Mild": [f for f in female_parameters["Topwear Fabric"] if f != ""]
}

# Formality-Fit mapping
formality_fit = {
    "Formal": ["Slim Fit", "Regular Fit"],
    "Semi-Formal": ["Slim Fit", "Regular Fit", "Athletic Fit"],
    "Smart Casual": ["Slim Fit", "Regular Fit", "Relaxed Fit", "Athletic Fit"],
    "Casual": [f for f in female_parameters["Fit"]]
}

# Formality-Footwear mappings
formality_footwear = {
    "Formal": ["Heels", "Flats", "Wedges"],
    "Semi-Formal": ["Heels", "Flats", "Wedges", "Ballet Flats"],
    "Smart Casual": ["Flats", "Sneakers", "Ballet Flats"],
    "Casual": ["Sneakers", "Sandals", "Boots", "Ballet Flats"]
}


# Color matching based on skin tone
def get_valid_colors(skin_tone, item_type, parameters):
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
        "Gender": "Female",
        "Occasion": combo["Occasion"],
        "Venue": random.choice(combo["Venue"]),
        "Formality Level": random.choice(combo["Formality Level"]),
        "Style": random.choice(combo["Style"])
    }

    # Check if this triplet is underrepresented
    triplet = (row["Occasion"], row["Venue"], row["Formality Level"])
    if triplet_counter.get(triplet, 0) >= 38:  # Cap at ~38 entries per combination for diversity
        for _ in range(10):  # Limit retries
            combo = random.choice(valid_combinations)
            row["Occasion"] = combo["Occasion"]
            row["Venue"] = random.choice(combo["Venue"])
            row["Formality Level"] = random.choice(combo["Formality Level"])
            row["Style"] = random.choice(combo["Style"])
            triplet = (row["Occasion"], row["Venue"], row["Formality Level"])
            if triplet_counter.get(triplet, 0) < 38:
                break

    # Weather and Skin Tone
    row["Weather"] = random.choice(female_parameters["Weather"])
    row["Skin Tone"] = random.choice(female_parameters["Skin Tone"])

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
        one_piece_types = ["Saree", "Lehenga", "Anarkali Suit"] if row["Occasion"] in ["Wedding", "Cultural Event"] else \
            ["Dress", "Jumpsuit", "Kurta Set"]
        row["One-Piece Type"] = random.choice(one_piece_types)
        row["One-Piece Length"] = random.choice(["Full-Length", "Midi"]) if row["One-Piece Type"] in ["Saree",
                                                                                                      "Lehenga"] else \
            random.choice([t for t in female_parameters["One-Piece Length"] if t != ""])
        row["One-Piece Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["One-Piece Color"] = random.choice(get_valid_colors(row["Skin Tone"], "One-Piece", female_parameters))
        row["One-Piece Pattern"] = random.choice(["Embroidered", "Zari", "Sequined"]) if row["One-Piece Type"] in [
            "Saree", "Lehenga"] else \
            random.choice([t for t in female_parameters["One-Piece Pattern"] if t != ""])
    else:
        # Non-one-piece outfit: set topwear and bottomwear
        row["One-Piece Type"] = row["One-Piece Length"] = row["One-Piece Fabric"] = \
            row["One-Piece Color"] = row["One-Piece Pattern"] = ""

        # Topwear
        topwear_types = ["Blouse", "Shirt"] if row["Formality Level"] in ["Formal", "Semi-Formal"] else \
            [t for t in female_parameters["Topwear Type"] if t != ""]
        row["Topwear Type"] = random.choice(topwear_types)
        row["Topwear Neck Type"] = "Collared" if row["Topwear Type"] == "Shirt" else \
            "Off-Shoulder" if row["Style"] in ["Bold", "Vintage"] and random.random() < 0.3 else \
                random.choice([t for t in female_parameters["Topwear Neck Type"] if t != ""])
        row["Sleeve Type"] = random.choice([t for t in female_parameters["Sleeve Type"] if t != ""])
        row["Topwear Pattern"] = random.choice(["Solid", "Striped", "Pinstripe"]) if row[
                                                                                         "Formality Level"] == "Formal" else \
            random.choice([t for t in female_parameters["Topwear Pattern"] if t != ""])
        row["Topwear Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["Topwear Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Topwear", female_parameters))

        # Bottomwear
        bottomwear_types = ["Formal Pants", "Trousers", "Skirt"] if row["Formality Level"] == "Formal" else \
            [t for t in female_parameters["Bottomwear Type"] if t != ""]
        row["Bottomwear Type"] = random.choice(bottomwear_types)
        row["Bottomwear Length"] = "Full Length" if row["Formality Level"] in ["Formal", "Semi-Formal"] else \
            random.choice([t for t in female_parameters["Bottomwear Length"] if t != ""])
        row["Bottomwear Pattern"] = "Solid" if row["Topwear Pattern"] in ["Striped", "Checked", "Floral",
                                                                          "Graphic Print"] else \
            random.choice([t for t in female_parameters["Bottomwear Pattern"] if t != ""])
        row["Bottomwear Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["Bottomwear Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Bottomwear", female_parameters))

        # Ensure color coordination
        neutral_colors = ["Black", "White", "Grey", "Navy Blue", "Beige"]
        if row["Topwear Color"] not in neutral_colors:
            row["Bottomwear Color"] = random.choice(neutral_colors)

    # Footwear (always included)
    row["Footwear Type"] = random.choice(formality_footwear[row["Formality Level"]])
    row["Footwear Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Footwear", female_parameters))

    # Layering (optional, 50% chance)
    if row["Weather"] not in ["Humid", "Rainy"] and row["Occasion"] not in ["Sports"] and random.random() < 0.5:
        layering_types = ["Blazer", "Shawl"] if row["Formality Level"] == "Formal" else \
            [t for t in female_parameters["Layering Type"] if t != ""]
        row["Layering Type"] = random.choice(layering_types)
        row["Layering Pattern"] = random.choice([t for t in female_parameters["Layering Pattern"] if t != ""])
        row["Layering Fabric"] = random.choice(weather_fabric[row["Weather"]])
        row["Layering Color"] = random.choice(get_valid_colors(row["Skin Tone"], "Layering", female_parameters))
    else:
        row["Layering Type"] = row["Layering Pattern"] = row["Layering Fabric"] = row["Layering Color"] = ""

    # Accessories (optional)
    if row["Occasion"] not in ["Sports", "Outdoor"] and random.random() < 0.9:
        row["Watch Type"] = random.choice([t for t in female_parameters["Watch Type"] if t != ""])
        row["Watch Strap Type"] = "Metal" if row["Formality Level"] == "Formal" else \
            random.choice([t for t in female_parameters["Watch Strap Type"] if t != ""])
        row["Watch Color"] = random.choice([t for t in female_parameters["Watch Color"] if t != ""])
    else:
        row["Watch Type"] = row["Watch Strap Type"] = row["Watch Color"] = ""

    if row["Occasion"] not in ["Sports", "Outdoor"] and random.random() < 0.9:
        row["Belt Material"] = random.choice([t for t in female_parameters["Belt Material"] if t != ""])
        row["Belt Color"] = row["Footwear Color"] if row["Formality Level"] in ["Formal", "Semi-Formal"] else \
            random.choice([t for t in female_parameters["Belt Color"] if t != ""])
    else:
        row["Belt Material"] = row["Belt Color"] = ""

    if row["Occasion"] in ["Outdoor", "Vacation"] and random.random() < 0.3:
        row["Hat Type"] = random.choice([t for t in female_parameters["Hat Type"] if t != ""])
        row["Cap/Hat Color"] = random.choice([t for t in female_parameters["Cap/Hat Color"] if t != ""])
    else:
        row["Hat Type"] = row["Cap/Hat Color"] = ""

    if row["Formality Level"] == "Formal":
        row["Neck/Bow/Tie"] = "Scarf"
    elif row["Occasion"] == "Cultural Event" and random.random() < 0.6:
        row["Neck/Bow/Tie"] = "Statement Necklace"
    elif random.random() < 0.4:
        row["Neck/Bow/Tie"] = random.choice(["Choker", "Pendant"])
    else:
        row["Neck/Bow/Tie"] = ""

    row["Earrings"] = random.choice(["Studs", "Hoops", "Danglers"]) if row["Style"] in ["Streetwear", "Bold",
                                                                                        "Traditional"] and random.random() < 0.2 else ""
    row["Bangles"] = random.choice(["Metal Bangles", "Beaded Bracelets"]) if row["Occasion"] in ["Wedding",
                                                                                                 "Cultural Event",
                                                                                                 "Party"] and random.random() < 0.3 else ""

    row["Fragrance"] = random.choice(["Floral", "Fruity"]) if row["Formality Level"] == "Formal" else \
        random.choice([t for t in female_parameters["Fragrance"] if t != ""]) if random.random() < 0.8 else ""

    return row, triplet


# Generate 3000 female entries
dataset = []
triplet_counter = Counter()
target_entries = 3000

while len(dataset) < target_entries:
    row, triplet = generate_valid_row(triplet_counter)
    triplet_counter[triplet] += 1
    dataset.append(row)

# Write to CSV
fieldnames = list(female_parameters.keys())
with open("female_outfit_dataset_3000.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in dataset:
        writer.writerow(row)

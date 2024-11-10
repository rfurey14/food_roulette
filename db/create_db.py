import sqlite3

# Connect to SQLite database (it will create a new file if it doesn't exist)
conn = sqlite3.connect('food_dishes.db')
cursor = conn.cursor() #creates a cursor 

# Create the tables and insert data
cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    dish_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    description TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS allergens (
    allergen_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dish_ingredients (
    dish_id INTEGER,
    ingredient_id INTEGER,
    PRIMARY KEY (dish_id, ingredient_id),
    FOREIGN KEY (dish_id) REFERENCES dishes(dish_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredient_allergens (
    ingredient_id INTEGER,
    allergen_id INTEGER,
    PRIMARY KEY (ingredient_id, allergen_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id),
    FOREIGN KEY (allergen_id) REFERENCES allergens(allergen_id)
)''')

# Insert data into dishes
cursor.executemany('''
INSERT INTO dishes (name, country, description) VALUES (?, ?, ?)
''', [
    ('Pad Thai', 'Thailand', 'A stir-fried noodle dish with shrimp, tofu, and peanuts'),
    ('Tacos', 'Mexico', 'Traditional Mexican dish with tortillas and fillings'),
    ('Sushi', 'Japan', 'Rice with raw fish and other ingredients'),
])

# Insert data into ingredients
cursor.executemany('''
INSERT INTO ingredients (name) VALUES (?)
''', [
    ('Rice',), 
    ('Shrimp',), 
    ('Tofu',),
    ('Peanuts',),
    ('Tortilla',), 
    ('Fish',), 
    ('Seaweed',),
])

# Insert data into allergens
cursor.executemany('''
INSERT INTO allergens (name) VALUES (?)
''', [
    ('Shellfish',), ('Peanuts',), ('Soy',), ('Gluten',), ('Fish',)
])

# Relate dishes and ingredients
cursor.executemany('''
INSERT INTO dish_ingredients (dish_id, ingredient_id) VALUES (?, ?)
''', [
    (1, 2), 
    (1, 3),
    (1, 4),  # Pad Thai ingredients
    (2, 5),  # Tacos ingredients
    (3, 1), #sushi ingredients
    (3, 6), 
    (3, 7), 
])

# Relate ingredients to allergens
cursor.executemany('''
INSERT INTO ingredient_allergens (ingredient_id, allergen_id) VALUES (?, ?)
''', [
    (2, 1),  # Shrimp contains Shellfish allergen
    (3, 3),  # Tofu contains Soy allergen
    (4, 2),  # Peanuts contain Peanut allergen
    (6, 5),  # Fish contains Fish allergen
])

# Commit and close the connection
conn.commit()
conn.close()

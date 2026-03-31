# Anime character dictionary
anime_characters = {
    "Naruto": "Naruto Uzumaki",
    "One Piece": "Monkey D. Luffy",
    "Dragon Ball": "Goku",
    "Attack on Titan": "Eren Yeager",
    "Jujutsu Kaisen": "Gojo Satoru"
}

# Show all anime characters
print("Anime Characters List:\n")

for anime, character in anime_characters.items():
    print(f"{anime} -> {character}")

# Ask user to search
search = input("\nEnter anime name to find main character: ")

if search in anime_characters:
    print("Main character is:", anime_characters[search])
else:
    print("Anime not found!")
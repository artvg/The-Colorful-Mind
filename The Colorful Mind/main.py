from colors import COLOR_DATA # color import
from zodiac import ZODIAC_DATA # zodiac import
from poems import POETRY_QUOTES # quote import

def main():
    welcome()

    while True:
        # Ask the user to choose a color
        color = get_color_choice()

        # Show what the color means
        emotion = get_emotion(color)
        print(f"\n🧠 The color {color.capitalize()} is often linked to: {emotion}.")

        #Show a fun zodiac fact for that color
        print(f"\n{get_zodiac_fact(color)}")

        # Show a quote by Sor Juana that fits the color       
        print("\n📜 Here’s a beautiful quote by Sor Juana that reflects this color:\n")
        print(get_poetry(color))

        # Ask if the user wants to play again
        if input("\nWould you like to explore another color? (yes/no): ").strip().lower() != "yes":
            print("\n🌈 Tank you for exploring The Colorful Mind.")
            break

# Welcome message
def welcome():
    print("Welcome to The Colorful Mind. Did you know that many emotions are connected to colors?")
    print("Choose one of the following to learn what it reveals...")

# Asks for color
def get_color_choice():
    print("\nWhat color would you like to know about?")
    print("Available colors:")
    for color in COLOR_DATA:
        print(f"- {color.capitalize()}")

    # Get user's input and make sure it's valid
    color = input("\nType a color from the list above: ").lower()
    while color not in COLOR_DATA:
        print("Sorry, I don't recognize that color.")
        color = input("Please enter a valid color: ").lower()
    return color

# Get emotion
def get_emotion(color):
    return COLOR_DATA[color]["emotions"]

# Get poetry
def get_poetry(color):
    # Look up Sor Juana'squote for the color
    if color in POETRY_QUOTES:
        quote = POETRY_QUOTES[color]
        return f'"{quote}"\n– Sor Juana Inés de la Cruz (Public Domain)\n'
    else:
        return "No poetry found for this color."

# Get the zodiac fact
def get_zodiac_fact(color):
    # Look up the zodiac linked to the color
    if color in ZODIAC_DATA:
        zodiac = ZODIAC_DATA[color]
        return (f"✨ Fun Fact:\nDid you know that {color} is also linked to the zodiac sign {zodiac['sign']}?\n"
                f"People born under {zodiac['sign']} are known for being {zodiac['traits']} — just like the color you chose.")
    return ""

if __name__ == "__main__":
    main()

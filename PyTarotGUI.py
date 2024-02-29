import os
import secrets
from tkinter import Tk, Frame, Text
from tkinter import ttk
from PIL import Image, ImageTk

import os
import sys

def get_executable_dir():
    # Get the directory containing the executable.
    if getattr(sys, 'frozen', False):
        # If the script is frozen (compiled into an executable)
        return os.path.dirname(sys.executable)
    else:
        # If the script is running in a Python interpreter
        return os.path.dirname(os.path.abspath(__file__))

def get_image_path(filename):
    executable_dir = get_executable_dir()
    image_path = os.path.join(executable_dir, "images", filename)
    return image_path

# Define the directory containing the images
images_dir = os.path.join(get_executable_dir(), "images")

# Define the paths to the images of the tarot cards
CARD_IMAGES = {
    "The Fool": get_image_path("The_Fool.jpg"),
    "The Magician": get_image_path("The_Magician.jpg"),
    "The High Priestess": get_image_path("The_High_Priestess.jpg"),
    "The Empress": get_image_path("The_Empress.jpg"),
    "The Emperor": get_image_path("The_Emperor.jpg"),
    "The Hierophant": get_image_path("The_Hierophant.jpg"),
    "The Lovers": get_image_path("The_Lovers.jpg"),
    "The Chariot": get_image_path("The_Chariot.jpg"),
    "Strength": get_image_path("Strength.jpg"),
    "The Hermit": get_image_path("The_Hermit.jpg"),
    "Wheel of Fortune": get_image_path("Wheel_of_Fortune.jpg"),
    "Justice": get_image_path("Justice.jpg"),
    "The Hanged Man": get_image_path("The_Hanged_Man.jpg"),
    "Death": get_image_path("Death.jpg"),
    "Temperance": get_image_path("Temperance.jpg"),
    "The Devil": get_image_path("The_Devil.jpg"),
    "The Tower": get_image_path("The_Tower.jpg"),
    "The Star": get_image_path("The_Star.jpg"),
    "The Moon": get_image_path("The_Moon.jpg"),
    "The Sun": get_image_path("The_Sun.jpg"),
    "Judgement": get_image_path("Judgement.jpg"),
    "The World": get_image_path("The_World.jpg"),
    "Ace of Cups": get_image_path("Ace_of_Cups.jpg"),
    "Two of Cups": get_image_path("Two_of_Cups.jpg"),
    "Three of Cups": get_image_path("Three_of_Cups.jpg"),
    "Four of Cups": get_image_path("Four_of_Cups.jpg"),
    "Five of Cups": get_image_path("Five_of_Cups.jpg"),
    "Six of Cups": get_image_path("Six_of_Cups.jpg"),
    "Seven of Cups": get_image_path("Seven_of_Cups.jpg"),
    "Eight of Cups": get_image_path("Eight_of_Cups.jpg"),
    "Nine of Cups": get_image_path("Nine_of_Cups.jpg"),
    "Ten of Cups": get_image_path("Ten_of_Cups.jpg"),
    "Page of Cups": get_image_path("Page_of_Cups.jpg"),
    "Knight of Cups": get_image_path("Knight_of_Cups.jpg"),
    "Queen of Cups": get_image_path("Queen_of_Cups.jpg"),
    "King of Cups": get_image_path("King_of_Cups.jpg"),
    "Ace of Swords": get_image_path("Ace_of_Swords.jpg"),
    "Two of Swords": get_image_path("Two_of_Swords.jpg"),
    "Three of Swords": get_image_path("Three_of_Swords.jpg"),
    "Four of Swords": get_image_path("Four_of_Swords.jpg"),
    "Five of Swords": get_image_path("Five_of_Swords.jpg"),
    "Six of Swords": get_image_path("Six_of_Swords.jpg"),
    "Seven of Swords": get_image_path("Seven_of_Swords.jpg"),
    "Eight of Swords": get_image_path("Eight_of_Swords.jpg"),
    "Nine of Swords": get_image_path("Nine_of_Swords.jpg"),
    "Ten of Swords": get_image_path("Ten_of_Swords.jpg"),
    "Page of Swords": get_image_path("Page_of_Swords.jpg"),
    "Knight of Swords": get_image_path("Knight_of_Swords.jpg"),
    "Queen of Swords": get_image_path("Queen_of_Swords.jpg"),
    "King of Swords": get_image_path("King_of_Swords.jpg"),
    "Ace of Wands": get_image_path("Ace_of_Wands.jpg"),
    "Two of Wands": get_image_path("Two_of_Wands.jpg"),
    "Three of Wands": get_image_path("Three_of_Wands.jpg"),
    "Four of Wands": get_image_path("Four_of_Wands.jpg"),
    "Five of Wands": get_image_path("Five_of_Wands.jpg"),
    "Six of Wands": get_image_path("Six_of_Wands.jpg"),
    "Seven of Wands": get_image_path("Seven_of_Wands.jpg"),
    "Eight of Wands": get_image_path("Eight_of_Wands.jpg"),
    "Nine of Wands": get_image_path("Nine_of_Wands.jpg"),
    "Ten of Wands": get_image_path("Ten_of_Wands.jpg"),
    "Page of Wands": get_image_path("Page_of_Wands.jpg"),
    "Knight of Wands": get_image_path("Knight_of_Wands.jpg"),
    "Queen of Wands": get_image_path("Queen_of_Wands.jpg"),
    "King of Wands": get_image_path("King_of_Wands.jpg"),
    "Ace of Pentacles": get_image_path("Ace_of_Pentacles.jpg"),
    "Two of Pentacles": get_image_path("Two_of_Pentacles.jpg"),
    "Three of Pentacles": get_image_path("Three_of_Pentacles.jpg"),
    "Four of Pentacles": get_image_path("Four_of_Pentacles.jpg"),
    "Five of Pentacles": get_image_path("Five_of_Pentacles.jpg"),
    "Six of Pentacles": get_image_path("Six_of_Pentacles.jpg"),
    "Seven of Pentacles": get_image_path("Seven_of_Pentacles.jpg"),
    "Eight of Pentacles": get_image_path("Eight_of_Pentacles.jpg"),
    "Nine of Pentacles": get_image_path("Nine_of_Pentacles.jpg"),
    "Ten of Pentacles": get_image_path("Ten_of_Pentacles.jpg"),
    "Page of Pentacles": get_image_path("Page_of_Pentacles.jpg"),
    "Knight of Pentacles": get_image_path("Knight_of_Pentacles.jpg"),
    "Queen of Pentacles": get_image_path("Queen_of_Pentacles.jpg"),
    "King of Pentacles": get_image_path("King_of_Pentacles.jpg")
}

# Define the meanings of the cards
CARD_MEANINGS = {
    "The Fool": "New beginnings, innocence, spontaneity",
    "The Magician": "Manifestation, resourcefulness, power",
    "The High Priestess": "Intuition, subconscious, mystery",
    "The Empress": "Fertility, nurturing, abundance",
    "The Emperor": "Authority, control, structure",
    "The Hierophant": "Tradition, conformity, beliefs",
    "The Lovers": "Relationships, choices, alignment",
    "The Chariot": "Drive, determination, success",
    "Strength": "Courage, inner strength, compassion",
    "The Hermit": "Soul-searching, introspection, guidance",
    "Wheel of Fortune": "Change, cycles, destiny",
    "Justice": "Fairness, truth, balance",
    "The Hanged Man": "Sacrifice, release, perspective",
    "Death": "Endings, transformation, renewal",
    "Temperance": "Balance, moderation, harmony",
    "The Devil": "Materialism, bondage, ignorance",
    "The Tower": "Disruption, chaos, revelation",
    "The Star": "Hope, inspiration, serenity",
    "The Moon": "Illusion, fear, subconscious",
    "The Sun": "Joy, success, vitality",
    "Judgement": "Judgement, rebirth, inner calling",
    "The World": "Completion, integration, accomplishment",
    "Ace of Cups": "New feelings, intuition, blessings",
    "Two of Cups": "Partnership, connection, mutual attraction",
    "Three of Cups": "Celebration, friendship, community",
    "Four of Cups": "Apathy, contemplation, missed opportunity",
    "Five of Cups": "Loss, grief, disappointment",
    "Six of Cups": "Nostalgia, innocence, memories",
    "Seven of Cups": "Illusion, choices, fantasy",
    "Eight of Cups": "Walking away, disillusionment, leaving behind",
    "Nine of Cups": "Satisfaction, emotional fulfillment, gratitude",
    "Ten of Cups": "Harmony, happiness, alignment",
    "Page of Cups": "Creativity, intuition, sensitivity",
    "Knight of Cups": "Romance, charm, idealism",
    "Queen of Cups": "Compassion, empathy, emotional support",
    "King of Cups": "Emotional balance, control, generosity",
    "Ace of Swords": "Clarity, truth, mental power",
    "Two of Swords": "Indecision, choices, stalemate",
    "Three of Swords": "Heartbreak, sorrow, grief",
    "Four of Swords": "Rest, relaxation, recuperation",
    "Five of Swords": "Conflict, tension, defeat",
    "Six of Swords": "Transition, moving on, peace",
    "Seven of Swords": "Deception, dishonesty, stealth",
    "Eight of Swords": "Limitation, restriction, isolation",
    "Nine of Swords": "Anxiety, fear, nightmares",
    "Ten of Swords": "Betrayal, endings, loss",
    "Page of Swords": "Curiosity, intellect, vigilance",
    "Knight of Swords": "Ambition, action, assertiveness",
    "Queen of Swords": "Independence, clarity, truth",
    "King of Swords": "Intellect, authority, truth",
    "Ace of Wands": "Inspiration, new opportunities, growth",
    "Two of Wands": "Planning, decisions, potential",
    "Three of Wands": "Expansion, foresight, progress",
    "Four of Wands": "Celebration, harmony, homecoming",
    "Five of Wands": "Competition, conflict, rivalry",
    "Six of Wands": "Victory, success, recognition",
    "Seven of Wands": "Challenge, perseverance, defensiveness",
    "Eight of Wands": "Speed, action, movement",
    "Nine of Wands": "Resilience, determination, perseverance",
    "Ten of Wands": "Burden, responsibility, hard work",
    "Page of Wands": "Exploration, discovery, excitement",
    "Knight of Wands": "Energy, passion, adventure",
    "Queen of Wands": "Courage, confidence, leadership",
    "King of Wands": "Vision, leadership, charisma",
    "Ace of Pentacles": "Opportunity, prosperity, potential",
    "Two of Pentacles": "Balance, adaptability, time management",
    "Three of Pentacles": "Teamwork, collaboration, competence",
    "Four of Pentacles": "Security, control, conservatism",
    "Five of Pentacles": "Hard times, poverty, lack",
    "Six of Pentacles": "Generosity, charity, giving and receiving",
    "Seven of Pentacles": "Patience, investment, long-term view",
    "Eight of Pentacles": "Diligence, craftsmanship, mastery",
    "Nine of Pentacles": "Luxury, self-sufficiency, financial independence",
    "Ten of Pentacles": "Legacy, inheritance, establishment",
    "Page of Pentacles": "Manifestation, new beginnings, learning",
    "Knight of Pentacles": "Hard work, reliability, responsibility",
    "Queen of Pentacles": "Nurturing, practicality, abundance",
    "King of Pentacles": "Abundance, success, ambition"
}

class Tarot_Card():

    def __init__(self, name, reversed=False):
        self.name = name
        self.reversed = reversed

    def __str__(self):
        if self.reversed:
            return f"Reversed {self.name}"
        else:
            return self.name


def shuffle_deck():
    tarot_deck = list(CARD_IMAGES.keys())  # Use only the names of the cards for the deck
    for i in range(len(tarot_deck) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        tarot_deck[i], tarot_deck[j] = tarot_deck[j], tarot_deck[i]
    return tarot_deck


def draw_card():
    tarot_deck = shuffle_deck()
    if tarot_deck:
        card_name = tarot_deck.pop()
        reversed_chance = secrets.randbelow(100)  # 50% chance of being reversed
        reversed_card = reversed_chance < 50
        return Tarot_Card(card_name, reversed=reversed_card)

def draw_one_card_command():
    tarot_card = draw_card()
    if tarot_card:
        card_name = f"Card: {tarot_card}"
        card_meaning = f"Meaning: {CARD_MEANINGS.get(tarot_card.name, 'Meaning not available')}"
        try:
            img = Image.open(CARD_IMAGES[tarot_card.name])
            if tarot_card.reversed:
                img = img.rotate(180)
            img = img.resize((100, 175))
            img = ImageTk.PhotoImage(img)
            card_label = ttk.Label(cards_frame.container, text=card_name + "\n" + card_meaning, image=img, compound="top")
            card_label.image = img
        except FileNotFoundError:
            card_label = ttk.Label(cards_frame.container, text=card_name + "\n" + card_meaning)

        ### insert the card into the text widget
        cards_frame.container.window_create("end", window=card_label, padx=5, pady=5)
        cards_frame.cards.append(card_label)

root = Tk()
root.title("PyTarot")
root.geometry("1024x768")

# Define custom styles
root.tk_setPalette(background="black", foreground="purple")
root.style = ttk.Style(root)
root.style.configure("TFrame", background="black")
root.style.configure("TLabel", background="black", foreground="purple")
root.style.configure("TButton", background="black", foreground="purple")

frm = ttk.Frame(root, padding=10)
frm.pack()  ### use pack() to pack the frame at the top side

draw_button = ttk.Button(frm, text="Draw a Card", command=draw_one_card_command)
draw_button.grid(column=0, row=0, padx=10, pady=10, sticky="ew")

title_label = ttk.Label(frm, text="~ ~ ~ PyTarot ~ ~ ~", font=("Helvetica", 16, "bold"))
title_label.grid(column=1, row=0, pady=10, sticky="ew")

quit_button = ttk.Button(frm, text="Quit", command=root.destroy)
quit_button.grid(column=2, row=0, padx=10, pady=10, sticky="ew")

cards_frame = Frame(root, bg="black")
cards_frame.pack(fill="both", expand=1)  ### used pack()

### use Text widget for showing the cards
cards_frame.container = Text(cards_frame, width=1, height=1, bd=0)
cards_frame.container.pack(side="left", fill="both", expand=1)

cards_frame.scrollbar = ttk.Scrollbar(cards_frame, orient="vertical", command=cards_frame.container.yview)
cards_frame.scrollbar.pack(side="right", fill="y")

cards_frame.cards = []

root.mainloop()
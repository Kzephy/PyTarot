import secrets
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Get the directory path where the Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory path for the images folder
images_dir = os.path.join(script_dir, "images")

# Define the paths to the images of the tarot cards
CARD_IMAGES = {
    "The Fool": os.path.join(images_dir, "The_Fool.jpg"),
    "The Magician": os.path.join(images_dir, "The_Magician.jpg"),
    "The High Priestess": os.path.join(images_dir, "The_High_Priestess.jpg"),
    "The Empress": os.path.join(images_dir, "The_Empress.jpg"),
    "The Emperor": os.path.join(images_dir, "The_Emperor.jpg"),
    "The Hierophant": os.path.join(images_dir, "The_Hierophant.jpg"),
    "The Lovers": os.path.join(images_dir, "The_Lovers.jpg"),
    "The Chariot": os.path.join(images_dir, "The_Chariot.jpg"),
    "Strength": os.path.join(images_dir, "Strength.jpg"),
    "The Hermit": os.path.join(images_dir, "The_Hermit.jpg"),
    "Wheel of Fortune": os.path.join(images_dir, "Wheel_of_Fortune.jpg"),
    "Justice": os.path.join(images_dir, "Justice.jpg"),
    "The Hanged Man": os.path.join(images_dir, "The_Hanged_Man.jpg"),
    "Death": os.path.join(images_dir, "Death.jpg"),
    "Temperance": os.path.join(images_dir, "Temperance.jpg"),
    "The Devil": os.path.join(images_dir, "The_Devil.jpg"),
    "The Tower": os.path.join(images_dir, "The_Tower.jpg"),
    "The Star": os.path.join(images_dir, "The_Star.jpg"),
    "The Moon": os.path.join(images_dir, "The_Moon.jpg"),
    "The Sun": os.path.join(images_dir, "The_Sun.jpg"),
    "Judgement": os.path.join(images_dir, "Judgement.jpg"),
    "The World": os.path.join(images_dir, "The_World.jpg"),
    "Ace of Cups": os.path.join(images_dir, "Ace_of_Cups.jpg"),
    "Two of Cups": os.path.join(images_dir, "Two_of_Cups.jpg"),
    "Three of Cups": os.path.join(images_dir, "Three_of_Cups.jpg"),
    "Four of Cups": os.path.join(images_dir, "Four_of_Cups.jpg"),
    "Five of Cups": os.path.join(images_dir, "Five_of_Cups.jpg"),
    "Six of Cups": os.path.join(images_dir, "Six_of_Cups.jpg"),
    "Seven of Cups": os.path.join(images_dir, "Seven_of_Cups.jpg"),
    "Eight of Cups": os.path.join(images_dir, "Eight_of_Cups.jpg"),
    "Nine of Cups": os.path.join(images_dir, "Nine_of_Cups.jpg"),
    "Ten of Cups": os.path.join(images_dir, "Ten_of_Cups.jpg"),
    "Page of Cups": os.path.join(images_dir, "Page_of_Cups.jpg"),
    "Knight of Cups": os.path.join(images_dir, "Knight_of_Cups.jpg"),
    "Queen of Cups": os.path.join(images_dir, "Queen_of_Cups.jpg"),
    "King of Cups": os.path.join(images_dir, "King_of_Cups.jpg"),
    "Ace of Swords": os.path.join(images_dir, "Ace_of_Swords.jpg"),
    "Two of Swords": os.path.join(images_dir, "Two_of_Swords.jpg"),
    "Three of Swords": os.path.join(images_dir, "Three_of_Swords.jpg"),
    "Four of Swords": os.path.join(images_dir, "Four_of_Swords.jpg"),
    "Five of Swords": os.path.join(images_dir, "Five_of_Swords.jpg"),
    "Six of Swords": os.path.join(images_dir, "Six_of_Swords.jpg"),
    "Seven of Swords": os.path.join(images_dir, "Seven_of_Swords.jpg"),
    "Eight of Swords": os.path.join(images_dir, "Eight_of_Swords.jpg"),
    "Nine of Swords": os.path.join(images_dir, "Nine_of_Swords.jpg"),
    "Ten of Swords": os.path.join(images_dir, "Ten_of_Swords.jpg"),
    "Page of Swords": os.path.join(images_dir, "Page_of_Swords.jpg"),
    "Knight of Swords": os.path.join(images_dir, "Knight_of_Swords.jpg"),
    "Queen of Swords": os.path.join(images_dir, "Queen_of_Swords.jpg"),
    "King of Swords": os.path.join(images_dir, "King_of_Swords.jpg"),
    "Ace of Wands": os.path.join(images_dir, "Ace_of_Wands.jpg"),
    "Two of Wands": os.path.join(images_dir, "Two_of_Wands.jpg"),
    "Three of Wands": os.path.join(images_dir, "Three_of_Wands.jpg"),
    "Four of Wands": os.path.join(images_dir, "Four_of_Wands.jpg"),
    "Five of Wands": os.path.join(images_dir, "Five_of_Wands.jpg"),
    "Six of Wands": os.path.join(images_dir, "Six_of_Wands.jpg"),
    "Seven of Wands": os.path.join(images_dir, "Seven_of_Wands.jpg"),
    "Eight of Wands": os.path.join(images_dir, "Eight_of_Wands.jpg"),
    "Nine of Wands": os.path.join(images_dir, "Nine_of_Wands.jpg"),
    "Ten of Wands": os.path.join(images_dir, "Ten_of_Wands.jpg"),
    "Page of Wands": os.path.join(images_dir, "Page_of_Wands.jpg"),
    "Knight of Wands": os.path.join(images_dir, "Knight_of_Wands.jpg"),
    "Queen of Wands": os.path.join(images_dir, "Queen_of_Wands.jpg"),
    "King of Wands": os.path.join(images_dir, "King_of_Wands.jpg"),
    "Ace of Pentacles": os.path.join(images_dir, "Ace_of_Pentacles.jpg"),
    "Two of Pentacles": os.path.join(images_dir, "Two_of_Pentacles.jpg"),
    "Three of Pentacles": os.path.join(images_dir, "Three_of_Pentacles.jpg"),
    "Four of Pentacles": os.path.join(images_dir, "Four_of_Pentacles.jpg"),
    "Five of Pentacles": os.path.join(images_dir, "Five_of_Pentacles.jpg"),
    "Six of Pentacles": os.path.join(images_dir, "Six_of_Pentacles.jpg"),
    "Seven of Pentacles": os.path.join(images_dir, "Seven_of_Pentacles.jpg"),
    "Eight of Pentacles": os.path.join(images_dir, "Eight_of_Pentacles.jpg"),
    "Nine of Pentacles": os.path.join(images_dir, "Nine_of_Pentacles.jpg"),
    "Ten of Pentacles": os.path.join(images_dir, "Ten_of_Pentacles.jpg"),
    "Page of Pentacles": os.path.join(images_dir, "Page_of_Pentacles.jpg"),
    "Knight of Pentacles": os.path.join(images_dir, "Knight_of_Pentacles.jpg"),
    "Queen of Pentacles": os.path.join(images_dir, "Queen_of_Pentacles.jpg"),
    "King of Pentacles": os.path.join(images_dir, "King_of_Pentacles.jpg")
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

class Card():

    def __init__(self, name, reversed=False):
        self.name = name
        self.reversed = reversed

    def __str__(self):
        if self.reversed:
            return f"Reversed {self.name}"
        else:
            return self.name


def shuffle_deck():
    deck = list(CARD_IMAGES.keys())  # Use only the names of the cards for the deck
    for i in range(len(deck) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck


def draw_card():
    deck = shuffle_deck()
    if deck:
        card_name = deck.pop()
        reversed_chance = secrets.randbelow(100)  # 50% chance of being reversed
        reversed_card = reversed_chance < 50
        return Card(card_name, reversed=reversed_card)

def draw_one_card_command():
    card = draw_card()
    if card:
        card_name = f"Card: {card}"
        card_meaning = f"Meaning: {CARD_MEANINGS.get(card.name, 'Meaning not available')}"
        try:
            img = Image.open(CARD_IMAGES[card.name])
            if card.reversed:
                img = img.rotate(180)
            img = img.resize((100, 175))
            img = ImageTk.PhotoImage(img)
            card_label = ttk.Label(cards_frame.interior, text=card_name + "\n" + card_meaning, image=img, compound="top")
            card_label.image = img
            
            # Calculate row and column
            row = len(cards_frame.cards) // 5
            column = len(cards_frame.cards) % 5
            
            card_label.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            cards_frame.cards.append(card_label)
        except FileNotFoundError:
            card_label = ttk.Label(cards_frame.interior, text=card_name + "\n" + card_meaning)
            card_label.grid(sticky="w", padx=5, pady=5)

def on_configure(event):
    cards_frame.canvas.configure(scrollregion=cards_frame.canvas.bbox("all"))

def on_title_configure(event):
    title_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root = Tk()
root.title("PyTarot")
root.geometry("800x600")

# Define custom styles
root.tk_setPalette(background="black", foreground="purple")
root.style = ttk.Style(root)
root.style.configure("TFrame", background="black")  # Set frame background color to black
root.style.configure("TLabel", background= "black", foreground="purple")  # Set label text color to purple
root.style.configure("TButton", background="black", foreground="purple")  # Set button text color to purple

frm = ttk.Frame(root, padding=10)
frm.grid(sticky="ew")

title_label = ttk.Label(frm, text="~ ~ ~ PyTarot ~ ~ ~", font=("Helvetica", 16, "bold"))
title_label.grid(column=0, row=0, columnspan=2, pady=10, sticky="ew")

draw_button = ttk.Button(frm, text="Draw a Card", command=draw_one_card_command)
draw_button.grid(column=0, row=1, padx=10, pady=10, sticky="ew")

quit_button = ttk.Button(frm, text="Quit", command=root.destroy)
quit_button.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

cards_frame = Frame(root, bg="black")
cards_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

cards_frame.grid_rowconfigure(0, weight=1)
cards_frame.grid_columnconfigure(0, weight=1)

cards_frame.canvas = Canvas(cards_frame, bg="black", highlightthickness=0)
cards_frame.canvas.grid(row=0, column=0, sticky="nsew")

cards_frame.scrollbar = ttk.Scrollbar(cards_frame, orient="vertical", command=cards_frame.canvas.yview)
cards_frame.scrollbar.grid(row=0, column=1, sticky="ns")
cards_frame.canvas.configure(yscrollcommand=cards_frame.scrollbar.set)

# Create cards_frame.interior as a child of cards_frame.canvas
cards_frame.interior = Frame(cards_frame.canvas, bg="black")
cards_frame.canvas.create_window((0, 0), window=cards_frame.interior, anchor="nw")

cards_frame.interior.bind("<Configure>", on_configure)

cards_frame.cards = []

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.bind("<Configure>", on_title_configure)

root.mainloop()
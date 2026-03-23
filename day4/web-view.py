import random
import webbrowser

websites = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.wikipedia.org"
]

chosen_site = random.choice(websites)
webbrowser.open(chosen_site)
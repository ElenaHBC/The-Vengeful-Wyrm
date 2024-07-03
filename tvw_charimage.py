"""
Module for fetching images for the characters through APIs
- create a list of 3 urls for each race: dwarf, elf, human wizzard
- each time a random image will be displayed after creating the character
- inroduce the module and link it to the game
- Class? so the user can describe their character and based on that the fitting image is fetched?
- add the name of the character as a title in the image/plot? added
- add description to the image?
"""

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import requests

# Function to display image from URL for character
def display_image(url, character_name, caption_text):
    try:
        # Fetch the image
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Open the image using PIL
        img = Image.open(BytesIO(response.content))

        # Display the image using matplotlib
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(img)
        ax.axis('off')  # Turn off axis numbers and ticks
        plt.title(f"{character_name}", pad = 30) # displays the name of the character as title
        fig.text(0.5, 0.1, f"{character_name}{caption_text}", ha = "center", va = "top", wrap = True,
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='none')) # formatting of the description text should be good for all dif images
        plt.subplots_adjust(top = 0.85, bottom = 0.2)
        plt.show() # should be at the end of all other functions
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch image: {e}")
    except IOError as e:
        print(f"Failed to open image: {e}")

# Example URL lists for characters
import random
dwarf_img_list = ["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f9e05a5d-03ce-4fb2-ba79-3b15306a0cdd/de5fzr2-4f1a02ab-d733-4186-9fba-bb810a622c88.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Y5ZTA1YTVkLTAzY2UtNGZiMi1iYTc5LTNiMTUzMDZhMGNkZFwvZGU1ZnpyMi00ZjFhMDJhYi1kNzMzLTQxODYtOWZiYS1iYjgxMGE2MjJjODguanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pYL1yabIDa1Cd7DOHV3-JXi5Z1yeBDm-LcxIo_qHZ20",
              "https://i0.wp.com/nerdarchy.com/wp-content/uploads/2017/06/dwarfminer.jpg?w=564&ssl=1", 
              "https://static.wikia.nocookie.net/forgottenrealms/images/b/b6/Dwarf-5e.png/revision/latest?cb=20180814005205"]
dwarf_img = random.choice(dwarf_img_list)


elf_img_list = ["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/16839a88-ba93-4b12-a311-eded58cf9f7e/dg3at3m-d17dcd60-61de-45a1-99ca-1a6c120830ea.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE2ODM5YTg4LWJhOTMtNGIxMi1hMzExLWVkZWQ1OGNmOWY3ZVwvZGczYXQzbS1kMTdkY2Q2MC02MWRlLTQ1YTEtOTljYS0xYTZjMTIwODMwZWEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.TcPUWcZr8Sge3t25DMksvyG2-AzNhUbJaqdfzYvuq0Q",
                "https://assets.playgroundai.com/091bb2df-428a-4f62-8062-a6533f714f6d.png",
                "https://assets.playgroundai.com/35cf8f50-ca26-400c-983a-4ea76b04a217.png"]

elf_img = random.choice(elf_img_list)


wizzard_img_list = ["https://images.nightcafe.studio/jobs/HVW6ec4BjYhrx4r5Z5Rx/HVW6ec4BjYhrx4r5Z5Rx--1--i6vxc.jpg?tr=w-1600,c-at_max",
               "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3362b80d-a497-446e-91b3-89fa22a794a8/dgz379s-24246f54-c1fc-4259-a91e-5ccf90b7af75.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzMzNjJiODBkLWE0OTctNDQ2ZS05MWIzLTg5ZmEyMmE3OTRhOFwvZGd6Mzc5cy0yNDI0NmY1NC1jMWZjLTQyNTktYTkxZS01Y2NmOTBiN2FmNzUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.N-YYmTwFJA7T8TZxcZpn8VJ4MPHYnYn3ZXO4Ab1wKb8",
               "https://www.wargamer.com/wp-content/sites/wargamer/2022/01/dnd-wizard-5e-580x334.jpg"]

wizzard_img = random.choice(wizzard_img_list)

# Function to display image from URL for wyrm
def display_wyrm(url, character_name):
    try:
        # Fetch the image
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Open the image using PIL
        img = Image.open(BytesIO(response.content))

        # Display the image using matplotlib
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(img)
        ax.axis('off')  # Turn off axis numbers and ticks
        plt.title("A wild angry wyrm appears!", pad = 30) # displays the name of the character as title
        fig.text(0.5, 0.1, f"{character_name}, how dare you enter my forest! You will pay with your life!", 
                 ha = "center", va = "top", wrap = True,
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='none')) # formatting of the description text should be good for all dif images
        plt.subplots_adjust(top = 0.85, bottom = 0.2)
        plt.show() # should be at the end of all other functions
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch image: {e}")
    except IOError as e:
        print(f"Failed to open image: {e}")

wyrm_img_list = ["https://static.wikia.nocookie.net/dragons/images/9/98/C35d2456e3197272474f01d1f0c70a5a.jpg/revision/latest?cb=20200107153740",
                 "https://awoiaf.westeros.org/images/thumb/a/a0/Firewyrm_by_Kevin_Catalan.jpg/1200px-Firewyrm_by_Kevin_Catalan.jpg",
                 "https://i.redd.it/ui0qntdao7qb1.png"]

wyrm_img = random.choice(wyrm_img_list)
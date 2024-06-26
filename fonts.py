"""
- Add colors, fonts and special characters to print statements to make the game visually better
"""
# first install termcolor trough command prompt: python -m pip install --upgrade termcolor
# first install simple_colors trough command prompt: python -m pip install simple-colors

from termcolor import colored
print(colored('Hello', 'green', attrs=['bold']))

"""
ext colors	Text highlights	Attributes
black	on_black	bold
red	on_red	dark
green	on_green	underline
yellow	on_yellow	blink
blue	on_blue	reverse
magenta	on_magenta	concealed
cyan	on_cyan	strike
white	on_white	
light_grey	on_light_grey	
dark_grey	on_dark_grey	
light_red	on_light_red	
light_green	on_light_green	
light_yellow	on_light_yellow	
light_blue	on_light_blue	
light_magenta	on_light_magenta	
light_cyan	on_light_cyan	
"""

from simple_colors import *
print(green('Hello', ['bold']))
print(green('hello', ['bold', 'underlined']))


"""
* Simple colors: black, red, green, yellow, blue, magenta, cyan
Included styles: bold, bright, dim, italic, underlined, blink, reverse : only bright, reverse and underlined work
"""

print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
print('--\N{SECTION SIGN}--')
print('--\N{PER MILLE SIGN}--')
print('--\N{BLACK STAR}--')
print('--\N{SNOWMAN}--')
print('--\N{KATAKANA LETTER TU}--')

# simple_colors
print(red("The Wyrm lands it's final blow and you are defeated!", ["reverse"]))
print(blue("The Wyrm lands it's final blow and you are defeated!"))
print(yellow("The Wyrm lands it's final blow and you are defeated!"))
print(magenta("The Wyrm lands it's final blow and you are defeated!"))
print(cyan("The Wyrm lands it's final blow and you are defeated!"))
print(green("The Wyrm lands it's final blow and you are defeated!", ["reverse"]))
print(black("The Wyrm lands it's final blow and you are defeated!", ["reverse"])) # with ot without reverse you cannot see on a black screen

# termcolor
print(colored("You attack first! Roll for an attack.", "green", attrs=['dark']))
print(colored("You attack first! Roll for an attack.", "light_blue"))

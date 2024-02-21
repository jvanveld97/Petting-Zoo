# import the python datetime module to help us create a timestamp

from slithering import Anaconda, MilkSnake, Python, RatSnake, Copperhead
from swimming import Bullfrog, Capybara, Catfish, Mallard, Salmon
from walking import Donkey, Hippo, Horse, Llama

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "Llama Chow")
jorge = Hippo("Jorge", "Hippo", "afternoon", "Watermelon")
sam = Donkey("Sam", "Jackass", "morning", "Carrots")
honey = Horse("Honey", "Horsey", "morning", "Hay")
cooper = Copperhead("Cooper", "Snake", "Rats")
ratty = RatSnake("Ratty", "Rat Snake", "Mice")
sal = Python("Sal", "Python", "Sunflower Seeds")
anna = Anaconda("Anna", "Anaconda", "Baby Cow")
milkshake = MilkSnake("Milkshake", "Milk Snake", "Popcorn")
billy = Mallard("Billy", "Mallard", "Bread")
bub = Bullfrog("Bub", "Bullfrog", "Flies")
sally = Catfish("Sally", "Catfish", "Kibble")
bob = Salmon("Bob", "Salmon", "Kibble")
cappy = Capybara("Cappy", "Capybara", "Pizza")

print(miss_fuzz.feed())
print(cappy.feed())

print(
    f"{jorge.name} the {jorge.species} is available to pet during the {jorge.shift} shift."
)

print(bub)

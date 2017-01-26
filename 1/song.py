# Riley Hal Taylor
# CSC 110, Spring 2017, Section 2J
# Alexander Farmer
# Homework 1

# This program will run through each verse, which will use a combination of
# new text and text encapsulated by the 'Repeated Lines' functions.

def main():
	verse1()
	verse2()
	verse3()
	verse4()
	verse5()
	verse6()
	verse7()

# Repeated Lines
# Each of these strings is used often enough to justify wrapping it in abs
# function.
def space():
	print("")

def coda():
	print("I don't know why she swallowed that fly,\nPerhaps she'll die.")

def spider_fly():
	print("She swallowed the spider to catch the fly,")

def bird_spider():
	print("She swallowed the bird to catch the spider,")

def cat_bird():
	print("She swallowed the cat to catch the bird,")

def dog_cat():
	print("She swallowed the dog to catch the cat,")

def custom():
	print("She swallowed the Rodent of Unusual Size to catch the dog,")

# Verses
# Each verse adds the text that exists soley in this verse and uses the functions
# necessary to generate the repeating sections of the verse.
def verse1():
	print("There was an old woman who swallowed a fly.")
	coda()
	space()

def verse2():
	print("There was an old woman who swallowed a spider,\nThat wriggled and iggled and jiggled inside her.")
	spider_fly()
	coda()
	space()

def verse3():
	print("There was an old woman who swallowed a bird,\nHow absurd to swallow a bird.")
	bird_spider()
	spider_fly()
	coda()
	space()

def verse4():
	print("There was an old woman who swallowed a cat,\nImagine that to swallow a cat.")
	cat_bird()
	bird_spider()
	spider_fly()
	coda()
	space()
	
def verse5():
	print("There was an old woman who swallowed a dog,\nWhat a hog to swallow a dog.")
	dog_cat()
	cat_bird()
	bird_spider()
	spider_fly()
	coda()
	space()

def verse6():
	print("There was an old woman who swallowed a Rodent Of Unusual Size,\nHer stomach she must despise to swallow a Rodent of Unusual Size.")
	custom()
	dog_cat()
	cat_bird()
	bird_spider()
	spider_fly()
	coda()
	space()

def verse7():
	print("There was an old woman who swallowed a horse,\nShe died of course.")

main()

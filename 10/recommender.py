# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Book Recommender
#
# Interacts with a review database and provides recommended books based
# on similarities between users

# HW9 Hours Spent: 4
# HW10 Hours Spent: 7

from review import *

FILE = 'ratings.txt'


def main():
    print("Welcome to the CSC110 Book Recommender. Type the word in the\n"
          "left column to do the action on the right.\n"
          "recommend : recommend books for a particular user\n"
          "best      : the book with the highest rating among all users\n"
          "add       : add a new book\n"
          "quit      : exit the program\n")
    recommendations = {}
    get_recommendations(recommendations)

    done = False
    while not done:
        selection = input("next task? ")
        if selection == "recommend":
            recommend(recommendations)
        elif selection == "best":
            best(recommendations)
        elif selection == "add":
            add(recommendations)
        elif selection == "quit":
            done = True
        else:
            print("please enter a valid response\n")


# --------------------------------------------------------------------
# get_recommendations fetches data from the provided file and adds it
#                     to the reviews database.
#
# PARAMETERS: db -- a dictionary. The reviews database
# --------------------------------------------------------------------
def get_recommendations(db):
    recs = open(FILE).readlines()
    for entry in range(0, len(recs), 4):
        user = recs[entry].strip()
        review = Review(recs[entry + 1].strip(),
                        recs[entry + 2].strip(),
                        recs[entry + 3].strip())
        add_recomendation(db, user, review)


# --------------------------------------------------------------------
# add_recomendation() adds a review to the database.
#
# PARAMETERS: db -- a dictionary. The reviews database
# --------------------------------------------------------------------
def add_recomendation(db, user, review):
    if user not in db:
        db[user] = set()
    db[user].add(review)


# --------------------------------------------------------------------
# get_best() finds the highest rated book in the database
#
# PARAMETERS: db -- a dictionary. The reviews database
# RETURNS: a tuple of the best rated title and it's rating
# --------------------------------------------------------------------
def get_best(db):
    ratings = {}
    for user in db:
        for rec in db[user]:
            if rec.get_title() not in ratings:
                ratings[rec.get_title()] = (rec.get_rating(), 1)
            else:
                new_rating = ratings[rec.get_title()][0] + rec.get_rating()
                new_count = ratings[rec.get_title()][1] + 1
                ratings[rec.get_title()] = (new_rating, new_count)
    highest_title = ''
    highest_avg_rating = 0
    for r in ratings:
        if ratings[r][0] / ratings[r][1] > highest_avg_rating:
            highest_title = r
            highest_avg_rating = ratings[r][0] / ratings[r][1]
    return highest_title, highest_avg_rating


# --------------------------------------------------------------------
# get_books_for_user() returns the bookset for a particular user
#
# PARAMETERS: db -- a dictionary. The reviews database
#             user -- a string. The user to find in the database
# RETURNS: a set of reviews
# --------------------------------------------------------------------
def get_books_for_user(db, user):
    return db[user]


# --------------------------------------------------------------------
# recommend() finds the user with the most similar reviews and
#             recommends their books for the inputed user
#
# PARAMETERS: db -- a dictionary. The reviews database
# --------------------------------------------------------------------
def recommend(db):
    user_recommend_for = input("user? ")
    similarities = {}
    # For each review the recommendee has, check reviews of other users
    if user_recommend_for in db:
        for review in db[user_recommend_for]:
            for user in db:
                for other_review in db[user]:
                    if review.get_title() == other_review.get_title():
                        # Add matches to the similarities list
                        dist = review.get_rating() * other_review.get_rating()
                        if user not in similarities:
                            similarities[user] = 0
                        similarities[user] += dist
    else:
        print("User not in database")
    similar_user = ''
    score = 0
    # Find the most similar user
    for user in similarities:
        if (similarities[user] > score) and (user != user_recommend_for):
            similar_user = user
            score = similarities[user]
    reviews = get_books_for_user(db, similar_user)
    for r in reviews:
        print(r)


# --------------------------------------------------------------------
# best() displays the highest rated book.
#
# PARAMETERS: db -- a dictionary. The reviews database
# --------------------------------------------------------------------
def best(db):
    book, avg = get_best(db)
    print("The highest rated book is:\n" + book,
          "\nwith an overall score of " + str(avg))


# --------------------------------------------------------------------
# add() adds a review to the database
#
# PARAMETERS: db -- a dictionary. The reviews database
# --------------------------------------------------------------------
def add(db):
    user = input("user? ")
    title = input("title? ")
    author = input("author? ")
    rating = input("rating? ")
    review = Review(title, author, rating)
    add_recomendation(db, user, review)


main()

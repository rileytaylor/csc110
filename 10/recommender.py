# HW9 Hours Spent: 4
# HW10 Hours Spent: 4

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


def get_recommendations(db):
    recs = open(FILE).readlines()
    for entry in range(0, len(recs), 4):
        user = recs[entry].strip()
        review = Review(recs[entry + 1].strip(),
                        recs[entry + 2].strip(),
                        recs[entry + 3].strip())
        add_recomendation(db, user, review)


def add_recomendation(db, user, review):
    if user not in db:
        db[user] = set()
    db[user].add(review)


def get_best(db):
    # return "Ender's Game", "5.0"
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


def recommend(db):
    user_recommend_for = input("user? ")
    if user_recommend_for in db:
        recommendee_books = db[user_recommend_for]
    else:
        print("Please try another user")


def best(db):
    best, avg = get_best(db)
    print("The highest rated book is:\n" + best,
          "\nwith an overall score of " + str(avg))


def add(db):
    user = input("user? ")
    title = input("title? ")
    author = input("author? ")
    rating = input("rating? ")
    review = Review(title, author, rating)
    add_recomendation(db, user, review)


main()

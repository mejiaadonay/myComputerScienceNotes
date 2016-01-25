def read_text():
    
# check profanity words
# Author:   Jose Escobar Mejia
# Date:     01/23/2016

    quotes = open("/Users/adonay/desktop/GitPortfolio/myComputerScienceCourseNotes/Python-Programming/Python-Programs/movies_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
    

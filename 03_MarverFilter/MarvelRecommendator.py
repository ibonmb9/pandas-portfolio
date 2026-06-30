import pandas as pd
marvel = pd.read_csv("./data/marvel_master.csv")

def recommendFilmOrSeries():
    print("Hi! Welcome to the Marvel Film/Series recommendator")
    formatChoice = int(input("Would you rather watch a film or a series? 1.Film ; 2.Series ; 3.don't care\n"))
    if (formatChoice == 1):
        formatFilterApplied = marvel[marvel.type == "movie"]
        print(formatFilterApplied.head())
    elif(formatChoice == 2):
        formatFilterApplied = marvel[marvel.type == "series"]
        print(formatFilterApplied.head())
    elif(formatChoice == 3):
        #It is not necessary to change anything, but we could remove the ones with NaN
        formatFilterApplied = marvel.loc[marvel.type.notnull()]
        print(formatFilterApplied.head())
    else:
        print(f"ERROR: {formatChoice} is not a valid choice. Try again.")

    response = int(input("By which filter would you like to filter? 1.Search title ; 2.Year\n"))
    if (response == 1):
        searchTitle(formatFilterApplied)
    elif(response == 2):
        filterYear(formatFilterApplied)
    else:
        print(f"ERROR: {response} is not a valid choice. Try again.")
        recommendFilmOrSeries()

def searchTitle(formatFilterApplied):
    title = str(input("Type the content you are looking for, please.\n"))
    solution = formatFilterApplied[formatFilterApplied.title.str.contains(title, case = False, na = False)] #It searches if the string appears in a title. with case=False ignores upper or lower cases and with na=False considerns that NaN does not contain it
    print(solution)

def filterYear(formatFilterApplied):
    lowLimitYear = int(input("Enter the year from which you would like to filter.\n"))
    highLimitYear = int(input("Enter the top year from which you would like to filter.\n"))

    solution = formatFilterApplied.loc[(formatFilterApplied.year >= lowLimitYear) & (formatFilterApplied.year <= highLimitYear)]
    print(solution)

recommendFilmOrSeries()
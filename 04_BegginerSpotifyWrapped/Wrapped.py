import pandas as pd

#STEP 1: Create the DataFrame itself
history2017 = pd.read_json("./MusicData/Streaming_History_Audio_2017.json")
history2018 = pd.read_json("./MusicData/Streaming_History_Audio_2018.json")
history2019 = pd.read_json("./MusicData/Streaming_History_Audio_2019.json")
history2020 = pd.read_json("./MusicData/Streaming_History_Audio_2020.json")
history2021 = pd.read_json("./MusicData/Streaming_History_Audio_2021.json")
history2022 = pd.read_json("./MusicData/Streaming_History_Audio_2022.json")
history2023 = pd.read_json("./MusicData/Streaming_History_Audio_2023.json")
history20240 = pd.read_json("./MusicData/Streaming_History_Audio_2024.json")
history20241 = pd.read_json("./MusicData/Streaming_History_Audio_2024_1.json")
history20250 = pd.read_json("./MusicData/Streaming_History_Audio_2025.json")
history20251 = pd.read_json("./MusicData/Streaming_History_Audio_2025_1.json")
history20260 = pd.read_json("./MusicData/Streaming_History_Audio_2026.json")
history20261 = pd.read_json("./MusicData/Streaming_History_Audio_2026_1.json")

songHistoryList = [history2017, history2018, history2019, history2020, history2021, history2022, history2023, history20240, history20241, history20250, history20251, history20260, history20261] #Create a list with all the DataFrames
singleSongHistoryJSON = pd.concat(songHistoryList, ignore_index = True) #Use concat() to create a single DataFrame with all of them. Since each of the DataFrame's index starts with 0, ignore_index is used to remake the index

# Así eliges tú el lugar exacto en el disco duro
singleSongHistoryJSON.to_csv("C:/Users/ibont/Desktop/IBON/CS/pandas-portfolio/04_BegginerSpotifyWrapped/MusicData/singleSongHistory.csv", index=False)
#print(singleSongHistoryJSON.head()) #Just to test if all went well

#STEP 2: Spotify Wrapped
def SpotifyWrappedArchive(singleSongHistory):
    print("HI! Welcome to your Spotify Wrapped Archive!") #Welcoming message
    statsRange = int(input("Would you like to see your music stats of a specific day or day-range?\n1. Specific Day ; 2.Day-Range\n")) #Ask user about range and analize answer
    if(statsRange == 1):
        SingleDayStats(singleSongHistory)
    elif(statsRange == 2):
        DayRangeStats(singleSongHistory)
    else:
        print("ERROR: Your input is not a choice. Please, try again.")
        SpotifyWrappedArchive(singleSongHistory)

def SingleDayStats(singleSongHistory):
    #It is not posible to do a do-while on Python. Therefore, it has to be an "infinit loop" with breaks
    while True:
        selectedDay = str(input("Please, enter the specific date in the next format: dd/mm/yyyy\nNOTE: If there is a single digit number, add zeros. Otherwise, the summary will be incorrect.\n"))
        dateParts = selectedDay.split("/") #Separate the date into day, month and year
        day = int(dateParts[0])
        month = int(dateParts[1])
        year = int(dateParts[2])
        if(ConfirmDateValidity(day, month, year)): #Check if the input is correct and throw Error if not
            break
        else:
            print("ERROR: date is not valid. Try again.")

    #When it reaches here, it means the date is checked and it is correct
    #Search the date in the DataFrame and prepare it stats
    searchDate = f"{dateParts[2]}-{dateParts[1]}-{dateParts[0]}"
    daySorting = singleSongHistory[singleSongHistory.ts.str.startswith(searchDate, na = False)]
    #In daySorting variable is all the info about the day selected. Now, we need to sort it a print it
    PrintResults(daySorting)

def DayRangeStats(singleSongHistory):
    while True:
        while True:
            selectedStartDay = str(input("Please, enter the starting date of the date-range in the next format: dd/mm/yyyy\nNOTE: If there is a single digit number, add zeros. Otherwise, the summary will be incorrect.\n"))
            startDateParts = selectedStartDay.split("/") #Separate the date into day, month and year
            dayStart = int(startDateParts[0])
            monthStart = int(startDateParts[1])
            yearStart = int(startDateParts[2])
            if(ConfirmDateValidity(dayStart, monthStart, yearStart)): #Check if the input is correct and throw Error if not
                break
            else:
                print("ERROR: starting date is not valid. Try again.")

        while True:
            selectedFinishDay = str(input("Please, enter the finishing date of the date-range in the next format: dd/mm/yyyy\nNOTE: If there is a single digit number, add zeros. Otherwise, the summary will be incorrect.\n"))
            finishDateParts = selectedFinishDay.split("/") #Separate the date into day, month and year
            dayFinish = int(finishDateParts[0])
            monthFinish = int(finishDateParts[1])
            yearFinish = int(finishDateParts[2])
            if(ConfirmDateValidity(dayFinish, monthFinish, yearFinish)): #Check if the input is correct and throw Error if not
                break
            else:
                print("ERROR: finishing date is not valid. Try again.")
        
        if(ConfirmRangeValidity(dayStart, monthStart, yearStart,dayFinish, monthFinish, yearFinish)):
            break
        else:
            print("The range is not acceptable. Try again.")

    #If it arrives here, the range is correct
    rangeDataFrame = CreateRangeDataFrame(startDateParts, finishDateParts, singleSongHistory)
    if(rangeDataFrame.empty):
        DayRangeStats(singleSongHistory)

    PrintResults(rangeDataFrame)

def ConfirmDateValidity(day, month, year):
    #This part of the code is not the most efficient option because it needs to be changed manually. Otherwise, it could cause errors.
    #START: Not efficient option
    if(year <= 2026):
        if(month in [1,3,5,7,8,10,12]):
            return (day <= 31)
        elif(month in [4,6,9,11]):
            return (day > 30)
        elif(month == 2):
            if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)): #Leap year
                return (day <= 29)
            else:
                return (day <= 28)
        else:
            return False
    else:
        return False
    #END: Not efficient option

def ConfirmRangeValidity(dayStart, monthStart, yearStart,dayFinish, monthFinish, yearFinish):
    result = False #First, let's suppose that the range is incorrect

    if(yearStart < yearFinish):
        result = True
    elif(yearStart == yearFinish):
        if(monthStart < monthFinish):
            result = True
        elif(monthStart == monthFinish):
            if(dayStart < dayFinish):
                result = True
            elif(dayStart == dayFinish):
                result = False
                print("Since both dates are the same, there is no range.")
    
    return result

def CreateRangeDataFrame(startDateParts, finishDateParts, singleSongHistory):
    #Method: Arrange the DataFrame in ascending order. Find start position and finish position. Sort the original DataFrame
    #We need to find the positions of the first appearance of the start date and the last aparition of the finish date
    #STEP 1: first appearance of start date
    searchStartDate = f"{startDateParts[2]}-{startDateParts[1]}-{startDateParts[0]}"
    startDateDataFrame = singleSongHistory[singleSongHistory.ts.str.startswith(searchStartDate, na = False)]
    if(startDateDataFrame.empty):
        print("There are not records on the starting date.")
        return pd.DataFrame
    else:
        #The index is not changed. Therefore, we have the position of the first appearance of the start date
        posFirstAppStartDate = startDateDataFrame.index[0]

    #STEP 2: last appearance of finish date
    searchFinishDate = f"{finishDateParts[2]}-{finishDateParts[1]}-{finishDateParts[0]}"
    finishDateDataFrame = singleSongHistory[singleSongHistory.ts.str.startswith(searchFinishDate, na=False)]
    if(finishDateDataFrame.empty):
        print("There are no records on the finishing date.")
        return pd.DataFrame
    else:
        posLastAppFinishDate = finishDateDataFrame.index[len(finishDateDataFrame)-1]
    
    rangeDataFrame = singleSongHistory.loc[posFirstAppStartDate : posLastAppFinishDate]
    return rangeDataFrame

def PrintResults(musicData):
    print("TIME LISTENING")
    SummaryTimeListened(musicData)
    print("---------------")

    print("ARTISTS")
    SummaryArtists(musicData)
    print("---------------")

    print("SONGS")
    SummarySongs(musicData)
    print("---------------")

    print("ALBUMS")
    SummaryAlbums(musicData)
    print()

    print("Thanks for using Spotify Wrapped Archive!")

def SummaryArtists(sortedByDateData):
    artistsFrequency = sortedByDateData.master_metadata_album_artist_name.value_counts() #This variable is a Series
    lenArtFreq = len(artistsFrequency)

    print(f"You've listened to {lenArtFreq} artists.")
    if(lenArtFreq < 5):
        print(f"Here it is your top {lenArtFreq}:")
        for i in range(0, lenArtFreq):
            print(f"Top {i+1}: {artistsFrequency.index[i]}")
    else:
        print("Here it is your top 5:")
        for i in range(0,5): #It does not use the first one (0)
            print(f"Top {i+1}: {artistsFrequency.index[i]}")

def SummarySongs(sortedByDateData):
    songsFrequency = sortedByDateData.master_metadata_track_name.value_counts()
    lenSongsFreq = len(songsFrequency)

    print(f"You've listened to {lenSongsFreq} songs.")
    if(lenSongsFreq < 5):
        print(f"Here is your top {lenSongsFreq}:")
        for i in range(0,lenSongsFreq):
            print(f"Top {i+1}: {songsFrequency.index[i]}. You've listened to it {songsFrequency.iloc[i]} times.")
    else:
        print("Here is your top 5:")
        for i in range(0,5):
            print(f"Top {i+1}: {songsFrequency.index[i]}. You've listened to it {songsFrequency.iloc[i]} times.")

def SummaryAlbums(sortedByDateData):
    albumsFrequency = sortedByDateData.master_metadata_album_album_name.value_counts()
    lenAlbFreq = len(albumsFrequency)
    print(f"You've listened to {lenAlbFreq} albums.")
    if(lenAlbFreq < 5):
        print(f"Here is your Top {lenAlbFreq}:")
        for i in range(0,lenAlbFreq):
            print(f"Top {i+1}: {albumsFrequency.index[i]}.")
    else:
        print("Here is your top 5:")
        for i in range(0,5):
            print(f"Top {i+1}: {albumsFrequency.index[i]}")

def SummaryTimeListened(sortedByDateData):
    totalMS = sortedByDateData.ms_played.sum()
    totalMin = totalMS // 60000
    print(f"You've listened {totalMin} minutes in total.")

SpotifyWrappedArchive(singleSongHistoryJSON)
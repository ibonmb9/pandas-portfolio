# pandas-portfolio
This repository will contain different contents and projects related with pandas on python
The objective of this repository is to document my progress on pandas

It will be all perfectly separated and organized in folders. The first one will about all the contents I have learned about pandas. The first course I made about pandas was Kaggle: Pandas tutorial (https://www.kaggle.com/learn/pandas).

02_KaggleCourseCode: 
In the process of the course, the code was made in the Kaggle web itself. However, I copied and pasted the code to have examples of differents exercises and methods available whenever. It has to be taken into account that due to the big size of the DataFrames, they will not be uploaded to the repository as it is specified in .gitignore. That is why, since the database used is available on Kaggle, that the link will be provided: https://www.kaggle.com/datasets/zynicide/wine-reviews

--------------------------------------------------------

03_MarvelFilter:
This is the very first project I have made using pandas. At this point, I was not really comfortable and familiar with pandas. That is why I have used Google Gemini to make this projects. I have asked different questions about why the code was not working and what I had todo to solve it. In retrospective, even though it only has been used for correction purposes and not to make the code itself, I believe I have abused the AI use and that is why, starting on the next project, I want to limit AI use. Otherwise, I will not learn since the best learning is when mistakes are made. As it happened with the course. The database used for this project was also from Kaggle. That is why I will provide the link: https://www.kaggle.com/datasets/vanshkumar007/mcu-and-marvel-media-complete-dataset

For this project, I have made a python file for tests. However, it is not finished. That is because the DataFrame I used is really extense and it takes plenty of time to create the expected result DataFrame. That process does not have much importance. In consequence, the test is unfinished. Even though it has many gaps, I decided to leave it there because it provides a sketch of how to make a testing Python file when pandas is used.

RESULTS
These are some of the outputs that will be shown on the terminal

<img src="https://github.com/user-attachments/assets/0891612b-c105-4b00-912d-aa7229860728" width="350" alt="image" />
<img src="https://github.com/user-attachments/assets/5ccb3049-2823-4b75-b92f-e69b27490fc1" width="350" alt="image" />

--------------------------------------------------------

04_BeginnerSpotifyWrapped: 
For this project I have used my personal data from Spotify. Therefore, due to privacy, the database will not be shared. Taking into account Spotify's data privacy, I have learned that it is posible to ask about my listening story. Spotify sent me my listening stats starting in 2017 and ending on 2026. They became in JSON format and a file or two per year. The first challenge was to make all the JSON files a single CSV DataFrame (to achieve this, Google Gemini provided me a guide (see it in 01_Concepts folder)). After that, the program itself began. First, it asks the user whether it wants to see stats of a specific date or a date-range. In both, the date is checked to see if it is valid. If so, it is possible to continue. Bear in mind that I have the code the easiest way possible since I am not very experienced yet in coding and, therefore, it is not the most efficient. My goal is to redo this project later on making it more efficient and giving the stats in visual way rathen than from the terminal. 

The data search method will be the next one: since one of the options is the specific day stats and the other day-range (various specific dates), the artists summary, song summary... will be made for a day and for the day-range, I will find the starting point and ending point and create a DataFrame with the data between the two limits.

RESULTS
1st option (Specific Date): This is an example of what will be shown on the terminal

<img src="https://github.com/user-attachments/assets/aa8f9f23-31bc-4cdd-ab5e-a9db482c76ea" width="350" alt="image" />

2nd option (Day-Range): This is an example of what will be shown on the terminal

<img src="https://github.com/user-attachments/assets/45de689d-38e6-45e0-954a-b61cc7341ce9" width="350" alt="image" />

--------------------------------------------------------

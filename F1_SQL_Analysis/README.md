# Project: F1_SQL_Analysis
  - Data Analysis (EDA) using Python and SQL

## About Formula 1:
Formula 1 (F1) is the highest level of international single-seater auto racing sanctioned by the Fédération Internationale de l'Automobile (FIA). The F1 World Championship consists of a series of races known as Grands Prix that take place on various circuits around the world. The cars are highly sophisticated and feature cutting-edge technology and engineering, with each team designing and building their own cars. The drivers compete for the Drivers' Championship, while the teams compete for the Constructors' Championship. The sport has a huge following and is considered to be one of the most prestigious and glamorous forms of motorsport in the world.

Each Grand Prix is a unique event, held on a different circuit, and involves a race where drivers compete against each other to finish first and score points towards the F1 World Championship.

Qualifying is a session held before the race, where drivers compete to set the fastest lap time they can on the track. The fastest time determines the driver's starting position on the grid for the race. The qualifying session consists of three parts: Q1, Q2, and Q3. In Q1, all drivers have 18 minutes to set their fastest time. The slowest drivers are then eliminated, and the remaining drivers go on to Q2. In Q2, drivers have 15 minutes to set their fastest time, with the slowest drivers again being eliminated. The remaining drivers go on to Q3, where they have 12 minutes to set their fastest time and determine their starting positions for the race.

Sprint races, also known as sprint qualifying, are a new format introduced in 2021. They are shorter races held on Saturdays, where drivers compete to set their starting positions for the Grand Prix. The format consists of a 100km race with no mandatory pit stops, and the finishing order of the sprint race determines the starting grid for the Grand Prix, with the winner starting from pole position. Sprint races are currently being trialed at three Grand Prix events in 2021.

## About the Project:
The aim of this project is to analyse a database consisting of all information on the Formula 1 races, drivers, constructors, qualifying, circuits, lap times, pit stops, championships from 1950 till the latest 2023 season to answer some questions concerning the predictability of the winners.

The questions for analysis were:
1. How accurately can the qualifying positions predict the race winners?
2. How accurately can the sprint positions predict the race winners?
3. Does the fastest lap of a GP indicates the winner?
4. Does pit stop strategy matters?

# Description:

The 'archive' paste has all the data in csv, it was later condensed in a database created with the code inside of the jupyter notebook file and then sued for the SQL analysis.

The 'SQL_F1_Analysis.ipynb' file contains the SQL code to answer the questions above imposed for the analysis as well as the code that created the database from the csv files.

The 'F1_1950_2023.db' is tha database utilized for the analysis.

The original data was obtained from <a href="https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/" target="_blank"> Kaggle </a>.

You may use https://inloop.github.io/sqlite-viewer/ and insert the database to visualize it as well as the SQL code with its results.

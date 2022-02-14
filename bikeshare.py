import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to take a closer look? Chicago, New York City or Washington? \nMake sure to type the city correctly otherwise it won't work.\n")
        if city not in ('New York City', 'Chicago', 'Washington'):
            print("Sorry, but we don't cover this city. Please try again.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or all?\nMake sure to type the month correctly otherwise it won't work.\n")
         if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
             print("Sorry, but we don't cover this month. Please try again.\n")
             continue
         else:
             break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day do you want to analyse? Type: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' if you do not have any preference.\nMake sure to type the day correctly otherwise it won't work.\n")
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'):
            print("Sorry, but we don't cover that. Please try again.\n")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day of the week:", most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("Most common start hour:", most_common_start_hour)

    #prints how long this function took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station:", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used end station:", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print("Most frequent used combination of start station and end station trip:", start_station, " & ", end_station)

    #prints how long this function took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel time:", df['Trip Duration'].mean())

    #prints how long this function took
    print("\nThis took %s seconds. " % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:\n", user_types)

    # TO DO: Display counts of gender
    try:
      gender = df['Gender'].value_counts()
      print("\nGender:\n", gender)
    except KeyError:
      print("\nGender:\nNo data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Year of birth'].min()
      print("\nEarliest Year:", earliest_year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      most_recent_year = df['Year of birth'].max()
      print("Most Recent Year:", most_recent_year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      most_common_year = df['Year of birth'].value_counts().idxmax()
      print("Most Common Year:", most_common_year)
    except KeyError:
      print("Most Common Year:\nNo data available for this month.")

    #prints how long this function took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        question = True
        while question:
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue: yes or no?").lower()
            if view_data == "no":
                question = False
                break
            else:
                continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city
    while True:
        city = input("Which city would you like to explore? (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please choose from: chicago, new york city, washington.")

    # Get user input for month
    while True:
        month = input("Which month would you like to explore? (all, january, february, march, april, may, june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please enter one of the following: all, january, february, march, april, may, june.")

    # Get user input for day of the week
    while True:
        day = input("Which day would you like to explore? (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day. Please enter a valid day of the week or 'all'.")

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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print("Most Popular Month:", popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most Popular Day:", popular_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most Popular Start Hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Popular Start Station:", popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Popular End Station:", popular_end_station)

    # Display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Most Frequent Combination of Start and End Station Trip:", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:", total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average Travel Time:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:\n", user_types)

    # Display counts of gender (only for NYC and Chicago)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Gender Counts:\n", gender_counts)
    else:
        print("Gender data not available for this city.")

    # Display earliest, most recent, and most common year of birth (only for NYC and Chicago)
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest Year of Birth: {earliest_year}")
        print(f"Most Recent Year of Birth: {most_recent_year}")
        print(f"Most Common Year of Birth: {most_common_year}")
    else:
        print("Birth Year data not available for this city.")

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

        # Ask user if they want to view raw data
        view_data = input('\nWould you like to view the raw data? Enter yes or no.\n')
        if view_data.lower() == 'yes':
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_data = input("\nWould you like to view 5 more rows of raw data? Enter yes or no.\n")
                if more_data.lower() != 'yes':
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
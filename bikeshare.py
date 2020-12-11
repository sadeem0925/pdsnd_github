import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #First im creaing a list for cities, months and days to ensure valid inputs from the user
    cities = ['chicago','new york city','washington']
    months = ['all','january','february','march','april','may','june']
    days = ['all','sunday','monday','tuesday','wednesday','thursday','friday']
    #taking input from user and storing the lower() of the string to the variables city, month and day
    #then creating a while loop that repeats until the user gives me a valid input
    city = (input('Enter a city from the following: Chicago, New York City, Washington\n')).lower()
    while city not in cities:
        print("Please enter a valid city")
        city = (input('Enter a city from the following: Chicago, New York City, Washington\n')).lower()
    print("You want to view the data for {0}".format(city.title()))
    month = (input('Enter a month from the following: January, February, March, April, May, June, All\n')).lower()
    while month not in months:
        print("Please enter a valid month")
        month = (input('Enter a month from the following: January, February, March, April, May, June, All\n')).lower()
    print("You want to view the data for {0}".format(month.title()))
    day = (input('Enter a day from the following: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All\n')).lower()
    while day not in days:
        print("Please enter a valid day")
        day = (input('Enter a day from the following: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All\n')).lower()
    print("You want to view the data for {0}".format(day.title()))

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
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is: {0}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("The most common day is: {0}".format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is: {0}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_st = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {0}".format(common_st))


    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most commonly used End Station is {0}".format(common_end))


    # TO DO: display most frequent combination of start station and end station trip

    common_combo = (df['Start Station'] + df['End Station']).mode()[0]
    print("The most commonly used combination of Start and End Stations is {0}".format(common_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration']).sum()
    print("The total travel time is {0}".format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = (df['Trip Duration']).mean()
    print("The average/mean travel time is {0}".format(avg_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    sub_counts = (df.loc[df['User Type'] == 'Subscriber']).count()[0]
    print("The number of users that are subscribed is {0}".format(sub_counts))

    cust_counts = (df.loc[df['User Type'] == 'Customer']).count()[0]
    print("The number of users that are customers is {0}".format(cust_counts))

    if city != 'washington':
        # TO DO: Display counts of gender
        female_count = (df.loc[df['Gender'] == 'Female']).count()[0]
        print("The number of users that are female is {0}".format(female_count))

        male_count = (df.loc[df['Gender'] == 'Male']).count()[0]
        print("The number of users that are male is {0}".format(male_count))


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = int((df['Birth Year']).min())
        print("The earliest birth year is {0}".format(earliest_year))

        most_recent_year = int((df['Birth Year']).max())
        print("The most recent birth year is {0}".format(most_recent_year))

        most_common_year = int((df['Birth Year']).mode())
        print("The most common birth year is {0}".format(most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    response = input("Would you like to view 5 rows of raw data? (yes/no)")
    x = 0
    while(response == 'yes'):
        rows = df.iloc[x:x+5]
        print(rows)
        x+=5
        response = input("Continue? (yes/no)")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        #i changed the parameters of this user_stats function so that if the city is washington,
        #the function will not count gender and birthyear, since that information is unavailable
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv("adult.data.csv", header=0)

    
    # 1. How many of each race are represented in this dataset?
    # This returns a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    
    # 2. What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    
    # 3. What is the percentage of people who have a Bachelor's degree?
    total_count = df.shape[0]
    bachelors_count = df[df["education"] == "Bachelors"].shape[0]
    percentage_bachelors = round(100 * bachelors_count / total_count, 1)
    
    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    # 5. What percentage of people without advanced education make more than 50K?
    # Define advanced education
    advanced_degrees = ["Bachelors", "Masters", "Doctorate"]
    higher_education = df[df["education"].isin(advanced_degrees)]
    lower_education = df[~df["education"].isin(advanced_degrees)]
    
    # Percentage with salary >50K for those with advanced education
    higher_education_rich = round(100 * higher_education[higher_education["salary"] == ">50K"].shape[0] / higher_education.shape[0], 1)
    # Percentage with salary >50K for those without advanced education
    lower_education_rich = round(100 * lower_education[lower_education["salary"] == ">50K"].shape[0] / lower_education.shape[0], 1)
    
    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()
    
    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(100 * min_workers[min_workers["salary"] == ">50K"].shape[0] / min_workers.shape[0], 1)
    
    # 8. What country has the highest percentage of people that earn >50K?
    # First, compute the total and rich counts for each country
    country_counts = df["native-country"].value_counts()
    rich_country_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()
    # Compute the percentage of rich people per country
    rich_country_percentage = (rich_country_counts / country_counts) * 100
    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = round(rich_country_percentage.max(), 1)
    
    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()
    
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

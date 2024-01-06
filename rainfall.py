"""
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 

The program should first ask for the number of years. 
The outer loop will iterate once for each year.
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
"""

MONTHS = 12


def main():
    years = int(input("Please input number of years of rainfall to enter:\n"))

    rainfall_history=[]

    for year in range(years):     
        
        rainfall_history.append([])
        for month in range(MONTHS):
            inches = float(input(f"Enter inches of rainfall for year {year}, month {month}: "))
            rainfall_history[year].append(inches) 

    total_months = years*MONTHS
    total_inches = sum(map(sum,rainfall_history))
    average_rainfall = total_inches/total_months

    print(f"Over {total_months} months there were {total_inches} inches of rain, with an average of {average_rainfall} inches of rain per month.")



if __name__ == "__main__":
    main()




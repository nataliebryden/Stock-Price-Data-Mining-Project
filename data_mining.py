"""
DT249 Programming  & Algorithms Assignment 1: Data Mining Project
This is a file that takes a CSV with Google 2019 stock price data and outputs the best and worst 6 months and years.
"""
import requests


def get_csv(url):
    """
    Downloads the CSV file containing daily stock data from the url provided and extracts the Date,
    Adjusted Close Price and Volume. The CSV file should be formatted with the following rows of data:
    Date,Open,High,Low,Close,Adj Close,Volume

    :param url: A string, the URL where the csv file is located.

    :return: A list of lists with the Date, Adj Close Price and Volume for each day.
    e.g. [['2004-08-19', 50.220219, 44659000.0], ... , ['2004-08-20', 54.209209, 22834300.0]]
    """
    try:
        csv_data = requests.get(url)
        csv = csv_data.text
        csv.strip()
        rows = csv.split('\n')
        # Delete first row to remove headers
        del rows[0]
        data_list = []
        for row in rows:
            if row:
                columns = row.split(',')
                # Delete the following columns: Open,High,Low,Close
                del columns[1:5]
                columns[1] = float(columns[1])
                columns[2] = float(columns[2])
                data_list.append(columns)
        return data_list

    except Exception as e:
        print(f"Error when trying to read {url}.\n Cannot return anything\n{e}")
        return None


def get_avg(all_stock_data):
    """
    Calculates the average of the data.

    :param all_stock_data: The list of lists with the Date, Adj Close Price and Volume for each day.
    e.g. [['2004-08-19', 50.220219, 44659000.0], ... , ['2004-08-20', 54.209209, 22834300.0]]

    :return: The average of the data.
    """
    try:
        sum_close_vol = 0.0
        sum_vol = 0.0
        for item in all_stock_data:
            adj_close = item[1]
            volume = item[2]
            sum_close_vol += adj_close * volume
            sum_vol += item[2]
        return sum_close_vol / sum_vol

    except Exception as e:
        print(e)
        exit()


def get_yearly_avg(all_stock_data):
    """
    Returns the yearly average of the inputted data.

    :param all_stock_data: The list of lists with the Date, Adj Close Price and Volume for each day.
    e.g. [['2004-08-19', 50.220219, 44659000.0], ... , ['2004-08-20', 54.209209, 22834300.0]]

    :return: A List of tuples with the year and average.
    """
    try:
        yearly_stock_data = {}
        for data in all_stock_data:
            year = data[0][0:4]
            if year not in yearly_stock_data:
                yearly_stock_data[year] = []
            yearly_stock_data[year].append(data)
        yearly_avg_list = []
        for year, stock_data in yearly_stock_data.items():
            yearly_avg_list.append((year, get_avg(stock_data)))
        return yearly_avg_list

    except Exception as e:
        print(e)
        exit()


def get_monthly_avg(all_stock_data):
    """
    Returns the monthly average of the inputted data.

    :param all_stock_data: The list of lists with the Date, Adj Close Price and Volume for each day.
    e.g. [['2004-08-19', 50.220219, 44659000.0], ... , ['2004-08-20', 54.209209, 22834300.0]]

    :return: A list of tuples with the month and average.
    """
    try:
        monthly_data = {}
        for data in all_stock_data:
            month = data[0][0:7]
            if month not in monthly_data:
                monthly_data[month] = []
            monthly_data[month].append(data)
        monthly_avg_list = []
        for month, stock_data in monthly_data.items():
            monthly_avg_list.append((month, get_avg(stock_data)))
        return monthly_avg_list

    except Exception as e:
        print(e)
        exit()


def pretty_print(list_of_averages):
    """
    Prints the results in a formatted fashion.

    :param list_of_averages:  A list of tuples with the sorted date and associated average value

    :return: The date and its average value in a formatted presentation.
    """
    try:
        for date, average in list_of_averages:
            print('{:11s}{:0.2f}'.format(date, average))

    except Exception as e:
        print(e)
        exit()



def sort_func(x):
    """Returns the first item in a list for sorting."""
    try:
        return x[1]

    except Exception as e:
        print(e)
        exit()


def main():
    try:
        stock_data = get_csv('http://193.1.33.31:88/pa1/GOOGL.csv')
        best_months = sorted(get_monthly_avg(stock_data), key=sort_func, reverse=True)
        worst_months = sorted(get_monthly_avg(stock_data), key=sort_func)
        best_years = sorted(get_yearly_avg(stock_data), key=sort_func, reverse=True)
        worst_years = sorted(get_yearly_avg(stock_data), key=sort_func)

        select_data = input("To make your selection, press:  \n"
                            "1: The Best and Worst Six Months \n"
                            "2: The Best and Worst Six Years \n"
                            "3: The Best and Worst Six Months and The Best and Worst Six Years \n")

        if select_data == '1':
            print('Please find the Best and Worst Six Months below.')
            print()
            print('The Best Six Months are:')
            pretty_print(best_months[0:6])
            print()
            print('The Worst Six Months are:')
            pretty_print(worst_months[0:6])
        elif select_data == '2':
            print('Please find the Best and Worst Six Years below.')
            print()
            print('The Best Six Years are:')
            pretty_print(best_years[0:6])
            print()
            print('The Worst Six Years are:')
            pretty_print(worst_years[0:6])
        elif select_data == '3':
            print('Please find the Best and Worst Six Months and The Best and Worst Six Years below.')
            print()
            print('The Best and Worst Six Months are:')
            print()
            print('The Best Six Months are:')
            pretty_print(best_months[0:6])
            print()
            print('The Worst Six Months are:')
            pretty_print(worst_months[0:6])
            print()
            print('The Best and Worst Six Years are:')
            print()
            print('The Best Six Years are:')
            pretty_print(best_years[0:6])
            print()
            print('The Worst Six Years are:')
            pretty_print(worst_years[0:6])

    except Exception as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()

# Project : Railway Reservation Analyzer (PS No. 82)
# Language: Python 3
# Concepts: Pandas, CSV, Matplotlib, Grouping

import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename):
    """Read the CSV file, skip rows with invalid fare, return clean data."""
    # Step 1: read the file (handle missing file)
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        print("Error: File '" + filename + "' not found.")
        return None

    # Step 2: convert Fare to number; wrong values like 'abc' become NaN
    data["Fare"] = pd.to_numeric(data["Fare"], errors="coerce")

    # Step 3: print a warning for every row with invalid fare
    for i in range(len(data)):
        if pd.isna(data.loc[i, "Fare"]):
            print("Warning: Row with PNR " + str(data.loc[i, "PNR"])
                  + " skipped - invalid fare.")

    # Step 4: keep only valid rows
    data = data.dropna(subset=["Fare"])
    print("Valid records analysed:", len(data))
    return data


def bookings_per_train(data):
    """Count all bookings of each train and draw a bar chart."""
    counts = data.groupby("Train").size()
    counts = counts.sort_values(ascending=False, kind="stable")

    for train, number in counts.items():
        print(train, ":", number)
    print("Total bookings:", counts.sum())

    plt.bar(counts.index, counts.values, color="skyblue")
    plt.title("Bookings per Train")
    plt.xlabel("Train")
    plt.ylabel("Number of Bookings")
    plt.show()


def revenue_per_train(data):
    """Add the fare of Confirmed tickets only for each train."""
    confirmed = data[data["Status"] == "Confirmed"]
    revenue = confirmed.groupby("Train")["Fare"].sum()
    revenue = revenue.sort_values(ascending=False)

    for train, amount in revenue.items():
        print(train, ": Rs.", int(amount))
    print("Total confirmed revenue: Rs.", int(revenue.sum()))

    plt.bar(revenue.index, revenue.values, color="lightgreen")
    plt.title("Revenue per Train (Confirmed tickets only)")
    plt.xlabel("Train")
    plt.ylabel("Revenue (Rs.)")
    plt.show()


def tickets_by_status(data):
    """Count Confirmed, Waiting and Cancelled tickets."""
    status = data.groupby("Status").size()
    for name in ["Confirmed", "Waiting", "Cancelled"]:
        print(name, ":", status.get(name, 0))


def main():
    print("===== Railway Reservation Analyzer =====")
    filename = input("Enter file name (e.g. bookings.csv): ")
    data = load_data(filename)
    if data is None:          # file not found -> stop safely
        return

    while True:
        print("\n1. Bookings per train")
        print("2. Revenue per train (Confirmed only)")
        print("3. Tickets by status")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            bookings_per_train(data)
        elif choice == "2":
            revenue_per_train(data)
        elif choice == "3":
            tickets_by_status(data)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


main()

import sys
from csv import DictReader
from typing import Dict, List


def main() -> None:
    """Entrypoint of program run as module."""
    args: Dict[str, str] = read_args()
    if args["operation"] == "list":
        result: List[float] = list(args["file_path"], args["column"])
        print(result)
    elif args["operation"] == "min":
        result: float = min(args["file_path"], args["column"])
        print(result)
    elif args["operation"] == "max":
        result: float = max(args["file_path"], args["column"])
        print(result)
    elif args["operation"] == "avg":
        result: float = avg(args["file_path"], args["column"])
        print(result)
    
    dates_list: List[str] = []
    file_handle = open("projects/pj01/2019-09-1-to-30.csv", "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        for element in row:
            if element == "DATE" and row["REPORT_TYPE"] == "SOD  ":
                date_string: str = ""
                i: int = 0
                while i < 10:
                    date_string = date_string + row[element][i]
                    i += 1
                dates_list.append(date_string)
    file_handle.close()
    chart_data(list("projects/pj01/2019-09-1-to-30.csv", "DailyAverageWindSpeed"), "DailyAverageWindSpeed", dates_list)


def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments and return them in a dictrionary."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    file_handle = open(sys.argv[1], "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    fail_test: bool = True
    for the_row in csv_reader:
        for the_column in the_row:
            if the_column == sys.argv[2]:
                fail_test = False
    if fail_test:
        print(f"Invalid column: {sys.argv[2]}")
        exit()
    if sys.argv[3] != "list" and sys.argv[3] != "min" and sys.argv[3] != "max" and sys.argv[3] != "avg":
        print(f"Invalid operation: {sys.argv[3]}")
        exit()
    file_handle.close()
    return {
        "file_path": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3]
    }


def list(file_path: str, column: str) -> List[float]:
    """Generates a list of floats for the values in a column."""
    results_list: List[float] = []
    file_handle = open(file_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        for element in row:
            if element == column and row["REPORT_TYPE"] == "SOD  ":
                try:
                    results_list.append(float(row[element]))
                except ValueError:
                    ...
    file_handle.close()
    return results_list


def min(file_path: str, column: str) -> float:
    """Finds the minimum value in a column."""
    values: List[float] = list(file_path, column)
    minimum: float = values[0]
    for num in values:
        if num < minimum:
            minimum = num
    return minimum


def max(file_path: str, column: str) -> float:
    """Finds the maximum value in a column."""
    values: List[float] = list(file_path, column)
    max: float = values[0]
    for num in values:
        if num > max:
            max = num
    return max


def avg(file_path: str, column: str) -> float:
    """Finds the average value of a column."""
    values: List[float] = list(file_path, column)
    sum: float = 0
    for num in values:
        sum += num
    average: float = sum / len(values)
    return average


def chart_data(data: List[float], column: str, dates: List[float]) -> None:
    """Plots data."""
    import matplotlib.pyplot as plt

    plt.title(f"Plot of {column} against Time")
    plt.xlabel("Date")
    plt.xticks(rotation=60)
    plt.ylabel(column)
    plt.plot(dates, data)
    plt.show()


if __name__ == "__main__":
    main()

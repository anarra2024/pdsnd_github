import csv

def read_csv(file_path):
    """
    This method reads data from a CSV file.
    
    Argumentss:
        file_path (str): Path to the CSV file.
        
    Returns:
        list: List of dictionaries where each dictionary represents a row in the CSV file.
    """
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    """
    Process the data read from the CSV file.
    
    Args:
        data (list): List of dictionaries representing the CSV data.
    """
    # Example processing: print the data
    for row in data:
        print(row)

if __name__ == "__main__":
    # Path to the CSV file - sample_data.csv
    csv_file_path = "sample_data.csv"
    
    # Read data from CSV file
    data = read_csv(csv_file_path)
    
    # Process the data
    process_data(data)
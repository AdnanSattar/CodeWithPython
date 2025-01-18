import csv

def filter_csv(input_file, output_file, column_name, condition):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            
            # Filter rows based on the condition
            filtered_rows = [row for row in reader if condition(row[column_name])]
            
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
        
        print(f"Filtered data saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the CSV Data Filter! 📊🔍")
    input_file = input("Enter the path to your input CSV file: ").strip()
    output_file = input("Enter the path to save the filtered data: ").strip()
    column_name = input("Enter the column name to filter by: ").strip()
    condition_str = input("Enter the condition (e.g., lambda x: x == 'specific_value'): ").strip()
    
    # Convert the condition string to a lambda function
    condition = eval(condition_str)
    
    filter_csv(input_file, output_file, column_name, condition)

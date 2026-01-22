import pandas as pd
import logging

# Configure Logging
logging.basicConfig(filename='data_validation.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def read_csv(file_path):
    """Function to read CSV safely. """
    try:
        df = pd.read_csv(file_path)
        return df

    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return pd.DataFrame() # Return an empty DataFrame in case of error

def validate_records(df):
    """Function to validate records."""
    valid_records = []
    for index, row in df.iterrows():
        age = row['age']
        if pd.isnull(age) or not isinstance(age, (int, float)) or not (0 <= age <= 120):
            logging.warning(f"Invalid age found at index {index}: {age}")
            continue
        valid_records.append(row)
    return pd.DataFrame(valid_records)

def summarize_date(df):
    """Function to produce a summary."""
    summary = {
        'total_valid_users': len(df),
        'users_per_country': df['country'].value_counts().to_dict(),
        'average_age': df['age'].mean() if not df.empty else 0
    }
    return summary

def output_results(summary, output_path):
    """Function to output the results."""
    try:
        with open(output_path, 'w') as file:
            file.write(f"Total Valid Users: {summary['total_valid_users']}\n")
            file.write(f"Users Per Country: {summary['users_per_country']}\n")
            file.write(f"Average Age: {summary['average_age']}\n")
        logging.info("Results output successfully.")
    except Exception as e:
        logging.error(f"Error writing to output file: {e}")

if __name__ == "__main__":
    df = read_csv('users.csv')
    valid_data = validate_records(df)
    summary = summarize_date(valid_data)
    output_results(summary, 'summary_output.txt')
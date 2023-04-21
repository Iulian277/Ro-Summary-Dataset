import os
import argparse
import pandas as pd
import traceback

ENCODING = 'utf-8'
CSV_COLUMNS = [
    'Document',
    'Summary',
    'Title',
    'Keywords',
    'Url',
    'Author',
]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, required=True, help='input directory')
    return parser.parse_args() 

def check_only_csvs(input_dir):
    exts = list(set([os.path.splitext(f)[1] for f in os.listdir(input_dir)]))
    if not all([ext == '.csv' for ext in exts]):
        print(f'[X]: Input directory `{input_dir}` should contain only `.csv` files.\n' \
                f'Found extensions: `{exts}`.')
        return False
    return True

def check_header(input_dir):
    files = os.listdir(input_dir)
    for file in files:
        file_path = os.path.join(input_dir, file)
        # Check if the CSV has a header row
        try:
            pd.read_csv(file_path, delimiter=',', encoding=ENCODING, header=0)
        except Exception as e:
            print(traceback.format_exc())
            print(f'[X]: Could not read file `{file_path}` because of error `{e}`.')
            return False
    return True
    
def check_empty_csv(input_dir):
    files = os.listdir(input_dir)
    for file in files:
        file_path = os.path.join(input_dir, file)
        # Sanity check for empty CSVs (no header, no rows)
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(traceback.format_exc())
            print(f'[X]: Could not read file `{file_path}` because of error `{e}`.')
            return False
        
        if len(df) == 0:
            print(f'[X]: The CSV file `{file_path}` has no rows.')
            return False

    return True

def check_comma_separated(input_dir):
    files = os.listdir(input_dir)
    for file in files:
        file_path = os.path.join(input_dir, file)
        # Check if the CSV is comma separated
        try:
            pd.read_csv(file_path, delimiter=',')
        except Exception as e:
            print(traceback.format_exc())
            print(f'[X]: Could not read file `{file_path}` because of error `{e}`.')
            return False
    return True

def check_columns(input_dir):
    files = os.listdir(input_dir)
    # Open each file and check if it has the correct columns
    for file in files:
        file_path = os.path.join(input_dir, file)
        # Check if the CSV has the correct columns
        # Also check the order of the columns
        df = pd.read_csv(file_path)
        columns = df.columns
        if not set([col for col in columns]) == set(CSV_COLUMNS):
            if len(set(columns)) > len(set(CSV_COLUMNS)):
                diff = set(columns) - set(CSV_COLUMNS)
            else:
                diff = set(CSV_COLUMNS) - set(columns)
            print(f'[X]: File `{file_path}` does not have the correct header.\n' \
                    f'\tFound header: `{list(columns)}`\n'\
                    f'\tExpected header: `{CSV_COLUMNS}`\n'\
                    f'\tDiff: `{list(diff)}`.')
            return False

        if not columns.to_list() == CSV_COLUMNS:
            print(f'[X]: File `{file_path}` does not have the correct order of header\'s columns.\n' \
                    f'\tFound columns: `{list(columns)}`\n'\
                    f'\tExpected columns: `{CSV_COLUMNS}`.')
            return False
    return True

def check_encoding(input_dir):
    files = os.listdir(input_dir)
    for file in files:
        file_path = os.path.join(input_dir, file)
        # Check if the CSV has the correct encoding
        try:
            pd.read_csv(file_path, delimiter=',', encoding=ENCODING)
        except Exception as e:
            print(traceback.format_exc())
            print(f'[X]: Could not read file `{file_path}` because of error `{e}`.')
            return False
    return True

def check_extra_columns(input_dir):
    files = os.listdir(input_dir)
    # Open each file and check if it has the correct columns
    for file in files:
        file_path = os.path.join(input_dir, file)
        # Iterate over the rows and check if there are extra columns
        try:
            pd.read_csv(file_path, delimiter=',', encoding=ENCODING, index_col=False)
        except Exception as e:
            print(traceback.format_exc())
            print(f'[X]: Could not read file `{file_path}` because of error `{e}`.')
            return False

    return True

def check_parse_csvs(input_dir):
    files = os.listdir(input_dir)
    for file in files:
        file_path = os.path.join(input_dir, file)
        try:
            df = pd.read_csv(file_path, delimiter=',', encoding=ENCODING, index_col=False)
            print(20*'-----')
            print(f'[W]: Successfully parsed the file `{file_path}` with `{len(df)}` rows.')
            print(df)
            df.to_csv(file, index=False)
            print(20*'-----')
        except Exception as e:
            print(traceback.format_exc())
            print(f'[X]: Could not parse the file `{file_path}` because of error `{e}`.')
            continue

def main():
    args = parse_args()
    input_dir = args.input_dir
    
    if not check_only_csvs(input_dir):
        return
    if not check_header(input_dir):
        return
    if not check_empty_csv(input_dir):
        return
    if not check_comma_separated(input_dir):
        return
    if not check_columns(input_dir):
        return
    if not check_encoding(input_dir):
        return
    if not check_extra_columns(input_dir):
        return
    
    check_parse_csvs(input_dir)

if __name__ == '__main__':
    main()

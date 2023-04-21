# Romanian Summarization Dataset

## CSV File Format
The CSV files must have the following header (6 columns):
`Document,Summary,Title,Keywords,Url,Author`

Example of a valid CSV file:
```csv
Document,Summary,Title,Keywords,Url,Author
Doc1Text,Sum1Text,Title1,Keywords1Text,Url1,Author1
Doc2Text,Sum2Text,Title2,Keywords2Text,Url2,Author2
...
```

The CSV files must have the following format:
- The first row must be the header
- The header must be exactly as above
- Each row must have the same number of columns (6)
- Comma-separated values
- UTF-8 encoding

> **Warning**
> When adapting you files to this required format, please keep all the rows, even if some values are missing.

> For example, if you don't have the author of a document, please keep the column and leave it empty. In this way, we do not lose any information and maybe for a certain downstream task, we do not need the author, but we need the document and the summary.

## Checker Usage
```sh
$ python3 checker.py --input-dir=<input_directory>
```

## Checker Output
The checker will warn you if the CSV files are not valid.

If the CSV files are valid, the checker will try to parse the CSV files and will output the status for each file.

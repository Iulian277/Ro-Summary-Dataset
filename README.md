# Romanian Summarization Dataset

## CSV File Format
The CSV files must have the following header (7 columns):
`Document,Summary,Title,Keywords,Url,Author,Topic`

Example of a valid CSV file:
```csv
Document,Summary,Title,Keywords,Url,Author,Topic
Doc1Text,Sum1Text,Title1,Keywords1Text,Url1,Author1,Topic1
Doc2Text,Sum2Text,Title2,Keywords2Text,Url2,Author2,Topic2
...
```

The CSV files must have the following format:
- The first row must be the header
- The header must be exactly as above
- Each row must have the same number of columns (6)
- Comma-separated values
- UTF-8 encoding

> **Warning**
**When adapting you files to this required format, please keep all the rows, even if some values are missing. For example, if you don't have the author of a document, please keep the column and leave it empty. In this way, we do not lose any information and maybe for a certain downstream task, we do not need the author, but we need the document and the summary.**

## Checker Usage
```sh
$ python3 checker.py --input-dir=<input_directory>
```

## Checker Output
The checker will warn you if the CSV files are not valid.

If the CSV files are valid, the checker will try to parse the CSV files and will output the status for each file.


## How to add a dataset
- Create a new `branch` called `dataset_name`
- Create a new `directory` called `dataset_name` in the root of the repository
- Add the CSV files in the `dataset_name` directory
- Ensure that the CSV files are valid (by running the `checker.py` script)
- Create a `Pull Request` from branch `dataset_name` to `main`
- `Wait` for a review from one of the maintainers.
- If the PR is approved, it will be merged into `main` and the dataset will be available for everyone.

### Example
If you want to add a new dataset extracted from `ProTV`, you will have to:
- Create a new `branch` called `protv`
- Create a new `directory` called `protv` in the root of the repository
- Add the CSV files in the `protv` directory.

    - The tree structure will look like this:
    ```
    .
    ├── protv
    |   └── *.csv
    ``` 
- Ensure that the CSV files are valid (by running the `checker.py` script)
- Create a `Pull Request` from branch `protv` to `main`
- `Wait` for a review from one of the maintainers.
- If the PR is approved, it will be merged into `main` and the dataset will be available for everyone.

## Git LFS

Some of the CSV files are too large to be stored in the repository. So, we use [Git LFS](https://git-lfs.github.com/) to store them. Make sure you have Git LFS installed on your machine.

Ensure that you `track` all the `.csv` files with Git LFS:
```sh
$ git lfs track "*.csv"
```

After that, you can easily add the files to the repository:
```sh
$ git checkout -b <dataset_name>
$ git add <dirname>/*.csv
$ git commit -m "Add dataset <dataset_name>"
$ git push origin <dataset_name>
```



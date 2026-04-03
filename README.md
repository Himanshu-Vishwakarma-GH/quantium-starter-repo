# Quantium Starter Repo

This repository shows the full workflow used to answer Soul Foods’s question:
Were Pink Morsel sales higher before or after the price increase on 15 January 2021?

The project starts with raw CSV files, formats and combines the data, builds an analysis dataset, turns that into a Dash visualiser, and then adds automated testing and CI so the app can be verified repeatedly.

A companion notebook, [main.ipynb](main.ipynb), walks through the raw data preparation workflow interactively. The Python script in [main.py](main.py) contains the final Dash app used for the visualiser.

## What the project does

The app visualises Pink Morsel sales over time and lets the user filter by region. The main view contains:

- A clear header explaining the business question.
- A line chart showing total sales by date.
- A region picker with `north`, `east`, `south`, `west`, and `all`.
- Styling to make the dashboard easier to read and more polished.

## Step-by-step flow

### 1. Start with the raw CSV data

The repository includes three source files in the `data/` folder:

- `data/daily_sales_data_0.csv`
- `data/daily_sales_data_1.csv`
- `data/daily_sales_data_2.csv`

Each file contains sales rows with the columns:

- `product`
- `price`
- `quantity`
- `date`
- `region`

At this stage, the `price` column is still stored as text with a dollar sign.

### 2. Format and combine the data

The data preparation step reads each CSV, keeps only rows for `pink morsel`, converts price into a numeric value, computes sales, and keeps the fields needed for analysis.

The logic is:

- Load each file from `data/*.csv`.
- Filter the rows to `pink morsel`.
- Remove the `$` sign from `price` and convert it to a number.
- Create a new `sales` field using `quantity * price`.
- Keep only `date`, `sales`, and `region`.
- Combine all of the cleaned frames into one dataset.
- Convert `date` into a proper datetime column.

This produces the formatted sales file:

- `Pink Morsel Sales.csv`

### 3. Analyze the sales data

Once the data is formatted, the analysis groups total sales by date.

This step is important because the visualiser needs a single sales total for each day, not one row per transaction line.

The result is a daily sales table ordered by date.

### 4. Build the chart

The dashboard uses Plotly Express to create a line chart.

The chart:

- plots `date` on the x-axis
- plots `sales` on the y-axis
- includes axis labels
- uses markers so the data points are easy to read

The chart title is designed to make the story obvious: whether sales changed around the Pink Morsel price increase.

### 5. Add the Dash interface

The Dash app uses a simple layout with three main UI pieces:

- A header that frames the business question.
- A region filter using radio buttons.
- The line chart below the filter.

The visual styling is intentionally more polished than a default app. It uses spacing, a soft background gradient, card-like panels, and rounded controls to make the dashboard easier to scan.

### 6. Make the chart interactive

The radio picker lets the user switch between:

- north
- east
- south
- west
- all

When the selection changes, a Dash callback rebuilds the figure using only the selected region’s data. Choosing `all` shows the full company-wide view.

## Main files

### [main.ipynb](main.ipynb)

The notebook version of the workflow. It shows the step-by-step data loading, filtering, sales calculation, and CSV formatting process that produces `Pink Morsel Sales.csv`.

### [main.py](main.py)

Contains the Dash app, the chart-building logic, the region callback, and the page styling.

### [Pink Morsel Sales.csv](Pink%20Morsel%20Sales.csv)

The cleaned and combined dataset created from the raw CSV inputs.

### [test_main.py](test_main.py)

Contains the Dash UI tests that check the app renders the expected elements.

### [run_tests.sh](run_tests.sh)

A bash wrapper that activates the virtual environment and runs the test suite.

### [.github/workflows/tests.yml](.github/workflows/tests.yml)

GitHub Actions workflow that runs the test suite automatically on push and pull request.

## How to run the app

From the project root:

```bash
python main.py
```

The app will start a local Dash server and open the dashboard in your browser.

## How to run the tests

You can run the tests directly with pytest:

```bash
python -m pytest -q
```

Or use the bash helper:

```bash
bash run_tests.sh
```

## Continuous integration

The repository includes a GitHub Actions workflow that:

- creates a virtual environment
- installs the dependencies needed by the app and tests
- runs the bash test script

This makes it easy to verify the project automatically whenever code changes are pushed.

## Project summary

In order, the project does the following:

1. Reads the raw daily sales CSV files.
2. Cleans the data and computes a `sales` field.
3. Combines the cleaned files into one formatted dataset.
4. Aggregates sales by date for analysis.
5. Creates a line chart to visualise the trend.
6. Adds a Dash interface with a title, chart, and region picker.
7. Styles the app for a better user experience.
8. Adds automated UI tests.
9. Adds a bash script for CI-friendly test execution.
10. Adds a GitHub Actions workflow so the tests run automatically.

That gives Soul Foods a working dashboard, a region-aware sales view, and a repeatable testing pipeline.

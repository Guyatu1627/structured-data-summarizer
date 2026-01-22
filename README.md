# Structured Data Summarizer



## Overview

This project reads a CSV of user data, validates it, and produces a summary, mirroring real data engineering tasks.



## Dataset

A CSV file named `users.csv` containing columns: user\_id, age, country, signup\_date, with simulated messy data.



## Running the Project

1. Ensure Python and the required libraries are installed.

2. Create your virtual environment and install dependencies.

3. Run the script with `python summarizer.py`.

4. Check `summary\_output.txt` for results and `data\_validation.log` for any issues.



## Assumptions

\- Ages must be valid numbers between 0 and 120.

\- Rows with missing or invalid data are logged and skipped.


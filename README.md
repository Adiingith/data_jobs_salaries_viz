
# Data Jobs Salary Visualization

This project is an interactive data visualization built with D3.js, designed to display the average salaries of data-related jobs across countries from 2020 to 2024. It also includes detailed job descriptions for each position.

## Project Structure

```
.
├── Data_jobs_salaries.csv                  # Raw job and salary data
├── Data_jobs_salaries_describe.csv        # CSV with job descriptions
├── job_descriptions.py                    # Script to generate job_descriptions.json
├── salary_by_year_country_avg.json        # Nested data: year → country → [{job, salary}]
├── job_descriptions.json                  # Detailed descriptions for each job title
├── csvtojson.py                           # Script to generate salary_by_year_country_avg.json
├── Data_jobs_salaries.html                # Main D3 visualization page
```

## How to Run the Visualization

You can run the visualization using one of the following local server methods:

### On Windows

#### Option 1: Python HTTP Server

```cmd
cd "D:\your\project\path"
python -m http.server 8000
```

Then open in your browser:
```
http://localhost:8000/Data_jobs_salaries.html
```

#### Option 2: Live Server (VS Code Plugin)

1. Open the project folder in Visual Studio Code
2. Right-click `Data_jobs_salaries.html`
3. Choose "Open with Live Server"

#### Option 3: npx live-server

If you have Node.js installed:

```cmd
cd "D:\your\project\path"
npx live-server
```

This will open the visualization automatically in your browser.

---

### On macOS

macOS comes with Python pre-installed. You can simply start a local server with:

```bash
cd /path/to/your/project
python3 -m http.server
```

Then visit in your browser:
```
http://localhost:8000/Data_jobs_salaries.html
```

---

## Data Preprocessing Scripts

- `job_descriptions.py`: Extracts and cleans job title descriptions from `Data_jobs_salaries_describe.csv` and saves them as `job_descriptions.json`.
- `csvtojson.py`: Groups salary data by year and country, calculates the average salary for each job title, and saves it to `salary_by_year_country_avg.json`.

Run with:

```bash
python job_descriptions.py
python csvtojson.py
```

---

## Browser Support

Use the latest version of Chrome, Edge, or Firefox for best experience.

## Tech Stack

- Visualization: D3.js v7
- Data Format: CSV + JSON
- Scripts: Python

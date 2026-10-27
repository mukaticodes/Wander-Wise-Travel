# WanderWise — Smart Travel Itinerary Planner

**Final-year student project | Python | Streamlit | ReportLab**

WanderWise is a responsive web application that creates a day-by-day travel itinerary for selected Indian destinations, estimates trip costs in INR, gives practical travel tips, and exports a printable PDF guide.

> **Project scope:** This is a rule-based planning application. It does not make bookings, use live pricing, or call an external AI service. Cost estimates are illustrative and should not be treated as quotes.

## 1. Features

- 10 Indian destinations with destination-specific highlights and food suggestions
- Custom trip start date and duration (1–14 days)
- Solo, couple, family, and friends travel profiles
- Relaxed, balanced, and activity-packed itinerary styles
- Budget, moderate, and comfort budget profiles
- Interest-aware itinerary text
- Itemized INR budget estimate
- PDF export with trip details, budget table, and day-wise plan
- Modular codebase and unit tests
- No API key or database required

## 2. Technology stack

| Component | Technology | Purpose |
|---|---|---|
| Front end | Streamlit | Interactive browser UI |
| Application logic | Python | Itinerary and budget generation |
| PDF generation | ReportLab | Downloadable travel guide |
| Testing | `unittest` | Core logic verification |
| Configuration | TOML | Streamlit theme settings |

## 3. Project structure

```text
WanderWise_Final_Year_Project/
├── app.py                    # Streamlit entry point and UI
├── wanderwise/
│   ├── __init__.py
│   ├── data.py               # Destinations and preference options
│   ├── planner.py            # Itinerary and budget logic
│   ├── pdf_export.py         # PDF report generation
│   └── utils.py              # Shared formatting helpers
├── tests/
│   └── test_planner.py       # Unit tests for core functionality
├── .streamlit/
│   └── config.toml           # App theme and server configuration
├── .gitignore
├── requirements.txt
└── README.md
```

## 4. Requirements

- Python 3.10 or newer
- VS Code or another Python editor
- Internet access for initial dependency installation

## 5. Run on Windows

Open the extracted project folder in VS Code, then open **Terminal → New Terminal**.

### Create a virtual environment

```powershell
py -m venv .venv
```

### Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt and run:

```bat
.venv\Scripts\activate.bat
```

### Install packages

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Start the application

```powershell
python -m streamlit run app.py
```

Open the local address printed in the terminal, usually `http://localhost:8501`.

## 6. Run on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 7. Run the tests

From the project root, with the virtual environment activated:

```bash
python -m unittest discover -s tests -v
```

The tests cover itinerary length and structure, invalid duration handling, budget totals, trip output fields, and currency formatting.

## 8. How the application works

1. The user selects destination, date, duration, party, pace, budget style, and interests.
2. The planner loads destination highlights and local food suggestions from `wanderwise/data.py`.
3. `wanderwise/planner.py` builds morning, afternoon, and evening activities for each day.
4. The budget estimator calculates lodging, food, activities, local transport, and intercity transport estimates.
5. Streamlit displays the plan and budget.
6. `wanderwise/pdf_export.py` generates the PDF when the user downloads the guide.

## 9. Budget model

The budget is estimated from configurable per-day cost assumptions and travel-party multipliers. It is intentionally simple and transparent for a student demo. It does not include every possible cost, and actual costs can vary substantially.

## 10. Deployment (optional)

### Streamlit Community Cloud

1. Create a GitHub repository and upload the project files.
2. Open Streamlit Community Cloud and create a new app.
3. Select the repository and branch.
4. Set the main file path to `app.py`.
5. Deploy and test the public URL.

Do not commit secrets, credentials, or private configuration files. This project does not require secrets by default.

## 11. Suggested final-year submission checklist

- [ ] Run the app locally and test every destination.
- [ ] Run the unit tests and capture the passing output.
- [ ] Capture screenshots of the itinerary, budget, and PDF export.
- [ ] Add your name, roll number, department, institution, and academic year to your report/cover page if required.
- [ ] Explain that the itinerary is rule-based and the budget is estimated rather than live.
- [ ] Follow your institution's rules for attribution and project disclosure.

## 12. Limitations and future enhancements

- Current recommendations use curated static data rather than live attraction or weather APIs.
- Travel estimates are illustrative and do not use live ticket or hotel prices.
- The app does not store accounts, saved trips, or bookings.

Possible extensions include a database for saved itineraries, map integration, verified weather data, hotel/transport API integration, user accounts, and a recommendation model. Any external API integration should include secure key management and clear handling of unavailable data.

# WanderWise — Project Report Outline

Use this as a starting point for your own academic report. Adapt it to your institution's required format and describe only work you have actually completed.

## Abstract
WanderWise is a web-based travel itinerary planning application developed with Python and Streamlit. It generates a day-wise itinerary from destination and preference inputs, estimates trip expenses in Indian rupees, and provides a downloadable PDF travel guide. The prototype uses rule-based logic and curated static destination data, avoiding external API dependencies.

## Problem statement
Planning a multi-day trip involves organizing activities, considering personal preferences, and estimating expenses. A simple tool that combines these tasks can help users create an initial travel plan more quickly.

## Objectives
1. Build a user-friendly interface for travel preferences.
2. Generate a structured itinerary for each day.
3. Estimate expenses by category.
4. Export a printable itinerary and budget.
5. Separate application logic from UI code and verify core behavior with unit tests.

## Scope
The prototype supports ten curated Indian destinations and trips from one to fourteen days. It is a planning aid, not a booking platform or source of live travel prices.

## Methodology
The user submits travel preferences through Streamlit. The planner selects destination highlights and food suggestions, builds morning/afternoon/evening activities, adjusts text based on selected interests, and estimates costs using budget-style and party-size multipliers. The PDF module formats the resulting trip object for download.

## System modules
- **UI module (`app.py`):** collects inputs and displays itinerary, budget, and tips.
- **Destination data (`wanderwise/data.py`):** stores destination highlights and preference options.
- **Planner (`wanderwise/planner.py`):** validates inputs and generates itineraries and cost estimates.
- **PDF module (`wanderwise/pdf_export.py`):** creates the downloadable PDF.
- **Utilities (`wanderwise/utils.py`):** common currency formatting.
- **Tests (`tests/test_planner.py`):** checks core planner behavior.

## Testing
Run `python -m unittest discover -s tests -v`. Record the actual output and any fixes made before submitting. Do not report tests as passed unless you ran them successfully.

## Limitations
The prototype has no user authentication, persistent database, live API integration, or booking functionality. Prices and itineraries are illustrative and require independent verification.

## Future scope
Potential enhancements include persistent saved trips, maps, live weather, verified attraction information, booking-provider links, and more detailed cost models.

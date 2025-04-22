# 🎬 ETL Pipeline for TMDB Data

This project is an ETL (Extract, Transform, Load) pipeline that collects movie data from [The Movie Database (TMDB)](https://www.themoviedb.org/), processes it, and saves it into various storage formats including CSV, PostgreSQL, and Google Sheets.

## 📌 Features

- ✅ Extract movie data from TMDB API  
- 🔄 Transform raw data into clean, structured format  
- 💾 Load data into:
  - CSV file
  - PostgreSQL database
  - Google Sheets (via API)

## 🛠️ Tech Stack

- Python 🐍
- Requests / Pandas / Psycopg2 / gspread
- PostgreSQL
- Google Sheets API

## 🚀 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/blasterdark300/ETL-Pipeline-TMDB.git
   cd ETL-Pipeline-TMDB

2.Create and activate virtual environment

python -m venv venv
venv\Scripts\activate  # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Configure Google Sheets API

Create a service account in Google Cloud Console

Enable the Sheets API

Download the credentials JSON file as google-sheets-api.json

Share the target Google Sheet with your service account email

Edit your configuration (API keys, DB credentials) in .env or directly in the script.

5. 📁 Output
output/movies.csv

PostgreSQL table tmdb_movies

Google Sheet: TMDB ETL Output

👨‍💻 Author
Created with 💡 by blasterdark300

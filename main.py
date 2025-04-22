import subprocess
from utils.extract import get_movies
from utils.transform import transform_movies
from utils.load import load_to_csv, load_to_sheets

def run_etl(pages=500, spreadsheet_id=None):
    """
    pages: jumlah halaman yang ingin diambil dari TMDb (20 film per halaman).
    spreadsheet_id: ID Google Sheets jika ingin mengunggah data ke Google Sheets.
    """
    all_movies = []
    for p in range(1, pages + 1):
        print(f"Fetching page {p}...")
        all_movies.extend(get_movies(page=p))  # Mengambil data film dari halaman yang berbeda

    # Transformasi data film menjadi DataFrame
    df = transform_movies(all_movies)
    
    # Simpan data ke CSV
    load_to_csv(df, filename='film.csv')

    # Jika ada spreadsheet_id, upload ke Google Sheets
    if spreadsheet_id:
        load_to_sheets(df, spreadsheet_id)

if __name__ == '__main__':
    # ID Google Sheets milikmu
    SPREADSHEET_ID = "1ylE2Y-ptscZffM6XsOQbkeuRrZghITBp67ZGXv8dnHI"
    
    # Jalankan ETL dan upload ke Google Sheets
    run_etl(pages=500, spreadsheet_id=SPREADSHEET_ID)

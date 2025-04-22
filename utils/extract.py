import requests

# Masukkan API key TMDB Anda di sini
tmdb_api_key = 'faa3dad377f9a4e068777a25eb9cb59f'

def get_movies(page=1):
    """
    Ambil daftar film populer dari TMDB (per halaman).
    Returns list of movie dicts.
    """
    url = (
        f'https://api.themoviedb.org/3/movie/popular'
        f'?api_key={tmdb_api_key}&page={page}'
    )
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json().get('results', [])
    raise Exception(f"Failed to fetch data: {resp.status_code}")
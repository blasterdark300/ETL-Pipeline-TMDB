import pandas as pd

def transform_movies(movies):
    """
    Transform list of movie dicts into a cleaned pandas DataFrame.
    - Strip whitespace from titles
    - Round vote_average to 1 decimal
    - Convert genre_ids list to comma-separated string
    - Filter out entries with zero or missing rating
    - Select & rename relevant columns
    """
    df = pd.DataFrame(movies)

    # 1. Bersihkan title (hapus whitespace)
    df['title'] = df['title'].str.strip()

    # 2. Bulatkan vote_average ke 1 decimal, skip None
    df['vote_average'] = df['vote_average'].apply(
        lambda x: round(x, 1) if isinstance(x, (int, float)) else None
    )

    # 3. Ubah genre_ids (list of ints) ke string “1,2,3”
    df['genres'] = df['genre_ids'].apply(
        lambda ids: ",".join(str(i) for i in ids) if isinstance(ids, list) else ''
    )

    # 4. Filter rating <= 0 atau None
    df = df[df['vote_average'].notna() & (df['vote_average'] > 0)]

    # 5. Pilih kolom yang tersedia dan rename
    df = df[['title', 'release_date', 'genres', 'vote_average']]
    df.columns = ['title', 'release_date', 'genres', 'rating']

    # 6. Konversi release_date ke datetime dan drop invalid
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['release_date'])

    return df

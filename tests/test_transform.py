import pandas as pd
from utils.transform import transform_movies

def test_transform_movies():
    sample = [
        {'title': ' MovieX ', 'genre_ids': [1,2], 'vote_average': 7.25, 'release_date': '2025-01-01', 'runtime': 100},
        {'title': 'BadMovie', 'genre_ids': [], 'vote_average': 0.0, 'release_date': '2025-01-02', 'runtime': 90}
    ]
    
    # Mengubah data sample menjadi DataFrame yang sudah dibersihkan
    df = transform_movies(sample)
    
    # Memastikan judul telah di-strip dari spasi
    assert df.iloc[0]['title'] == 'MovieX'
    
    # Memastikan rating telah dibulatkan ke satu angka desimal (round)
    assert df.iloc[0]['rating'] == 7.2  # Update dengan 7.2 sesuai pembulatan
    
    # Memastikan 'BadMovie' telah difilter karena ratingnya 0
    assert 'BadMovie' not in df['title'].tolist()
    
    # Memastikan genre telah diformat dengan benar (komma-seperated)
    assert df.iloc[0]['genres'] == '1,2'

import pytest
from unittest.mock import patch
from utils.extract import get_movies

# Menguji jika API berhasil merespons data film
@patch('utils.extract.requests.get')
def test_get_movies_success(mock_get):
    # Menetapkan status code sebagai 200 (OK)
    mock_get.return_value.status_code = 200
    # Menetapkan nilai json untuk response yang dipalsukan
    mock_get.return_value.json.return_value = {'results': [{'title': 'A', 'genre_ids': [], 'vote_average': 5.0, 'release_date': '2025-01-01', 'runtime': 120}]}  
    # Memanggil fungsi get_movies dan memverifikasi hasilnya
    movies = get_movies(page=1)
    assert isinstance(movies, list)  # Memastikan hasilnya berupa list
    assert len(movies) > 0  # Memastikan ada data film
    assert movies[0]['title'] == 'A'  # Memastikan judul film pertama sesuai

# Menguji jika API merespons dengan kesalahan
@patch('utils.extract.requests.get')
def test_get_movies_failure(mock_get):
    # Menetapkan status code sebagai 404 (Not Found)
    mock_get.return_value.status_code = 404
    # Menggunakan pytest.raises untuk memastikan bahwa Exception dilempar
    with pytest.raises(Exception):
        get_movies(page=1)  # Memanggil fungsi yang seharusnya melempar error

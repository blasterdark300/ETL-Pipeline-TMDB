import pandas as pd
import pytest
from unittest.mock import patch
from utils.load import load_to_csv

# Uji untuk memverifikasi apakah fungsi load_to_csv memanggil pd.DataFrame.to_csv dengan benar
@patch.object(pd.DataFrame, 'to_csv')
def test_load_to_csv(mock_to_csv):
    # Membuat DataFrame contoh
    df = pd.DataFrame([{'a': 1, 'b': 2}])
    
    # Memanggil fungsi load_to_csv dengan DataFrame dan nama file 'film.csv'
    load_to_csv(df, filename='film.csv')
    
    # Memastikan bahwa to_csv dipanggil sekali dengan argumen yang tepat, 'film.csv' dan index=False
    mock_to_csv.assert_called_once_with('film.csv', index=False)

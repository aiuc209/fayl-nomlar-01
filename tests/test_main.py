import pytest
from datetime import datetime
from your_module import get_file_creation_date

def test_get_file_creation_date():
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    expected_dates = ["01.01.2022", "02.02.2022", "03.03.2022"]
    for file_name, expected_date in zip(file_names, expected_dates):
        date = get_file_creation_date(file_name)
        assert date == expected_date

def test_get_file_creation_date_invalid_file():
    file_name = "non_existent_file.txt"
    date = get_file_creation_date(file_name)
    assert date is None

def test_get_file_creation_date_empty_file_name():
    file_name = ""
    date = get_file_creation_date(file_name)
    assert date is None

def test_get_file_creation_date_invalid_date_format():
    file_name = "file_with_invalid_date.txt"
    date = get_file_creation_date(file_name)
    assert date is None

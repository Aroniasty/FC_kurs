from unittest.mock import patch

from Lesson_12_Python.pobieranie_danych_z_zewnatrz import pobieranie_danych_z_zewnatrz


def test_pobierania_danych_z_zewnatrz():
    with patch("Lesson_12_Python.pobieranie_danych_z_zewnatrz.py.pobieranie_danych_z_zewnatrz") as mock_data:
        mock_data.return_value = "dane z wewnatrz"
        assert pobieranie_danych_z_zewnatrz() == "dane z wewnatrz"
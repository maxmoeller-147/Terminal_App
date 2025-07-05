import pytest
import json
from unittest.mock import mock_open, patch
from utilities import show_complete_decklist

mock_decklist = {
    "Blade Flurry (red)": 3,
    "Draw Swords (red)": 3,
    "Gorganian Tome": 1
}

def test_show_complete_decklist(capsys):
    fake_json = json.dumps(mock_decklist)

    with patch("builtins.open", mock_open(read_data=fake_json)):
        show_complete_decklist()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')

    expected_lines = [
        "3x Blade Flurry (red)",
        "3x Draw Swords (red)",
        "1x Gorganian Tome"
    ]

    for expected in expected_lines:
        assert expected in output_lines

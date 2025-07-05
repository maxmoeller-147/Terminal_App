import pytest
import json
import random
from unittest.mock import patch, mock_open
from utilities import draw_hand_from_decklist 

def test_draw_hand_from_decklist(capsys):

    mock_deck = {
        "Blade Flurry (red)": 3,
        "Draw Swords (red)": 3,
        "Gorganian Tome": 1,
        "Hit and Run (blue)": 3,
        "Spoils of War (red)": 3
    }

    fake_json = json.dumps(mock_deck)

   
    fixed_hand = ["Draw Swords (red)", "Gorganian Tome", "Spoils of War (red)", "Hit and Run (blue)"]

    with patch("builtins.open", mock_open(read_data=fake_json)), \
         patch("random.sample", return_value=fixed_hand):

        draw_hand_from_decklist()


    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")

    assert output == fixed_hand

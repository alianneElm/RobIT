from unittest.mock import patch
from main import main

def test_main_flow(capsys):
    user_inputs = [
        "5",    # grid width
        "5",    # grid height
        "2",    # RobIT x
        "3",    # RobIT y
        "N",    # RobIT direction
        "FFRFF",  # movement commands
        "exit"  # exit command
    ]
    with patch("builtins.input", side_effect=user_inputs):
        main()

    captured = capsys.readouterr()

    print("=== OUTPUT START ===")
    print(captured.out)
    print("=== OUTPUT END ===")

    assert "📍 Final report:" in captured.out

    final_state = "4 4 E"
    lines = captured.out.strip().splitlines()
    assert any(final_state in line for line in lines), (
        f"Expected final state '{final_state}' not found in output:\n{captured.out}"
    )

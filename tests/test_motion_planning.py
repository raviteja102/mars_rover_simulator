import subprocess

def test_motion_planning_file_input():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_input.txt"], capture_output=True, text=True)
        assert "Read commands from a file" in result.stdout
def test_motion_planning_test_input():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_input.txt"], capture_output=True, text=True)
        assert "Robot placed at (1, 1) facing WEST" in result.stdout
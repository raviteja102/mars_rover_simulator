import subprocess

def test_motion_planning_file_input():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_input.txt"], capture_output=True, text=True)
        assert "1,1,WEST" in result.stdout
def test_motion_planning_test_input():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_input_two.txt"], capture_output=True, text=True)
        assert "Rover not yet placed" in result.stdout
def test_motion_planning_valid_commands():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_valid_commands.txt"],capture_output=True, text=True)
        assert "1,1,EAST" in result.stdout
def test_motion_planning_invalid_commands():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_invalid_commands.txt"],capture_output=True, text=True)
        assert "Rover not yet placed" in result.stdout
def test_motion_planning_invalid_file():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_invalid_file.txt"],capture_output=True, text=True)
        assert "No such file or directory" in result.stderr
def test_motion_planning_empty_file():
        result = subprocess.run( ["python3", "src/motion_planning.py", "--file", "tests/test_empty_file.txt"],capture_output=True, text=True)
        # Check that the return code is 0 (indicating success)
        assert result.returncode == 0
        assert result.stdout.strip() == ""  # No output expected
        assert result.stderr.strip() == ""  # No errors expected


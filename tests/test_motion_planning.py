import subprocess

def test_motion_planning_file_input():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_input.txt"], capture_output=True, text=True)
        assert "1,1,WEST" in result.stdout
def test_motion_planning_test_input():
        result = subprocess.run(["python3", "src/motion_planning.py", "--file", "tests/test_input_two.txt"], capture_output=True, text=True)
        assert "Rover not yet placed" in result.stdout
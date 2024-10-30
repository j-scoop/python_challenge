import unittest
import subprocess
import sys


class TestScriptsRun(unittest.TestCase):

    def run_script(self, script_name):
        command = ["poetry", "run", "python", "-m", script_name]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(
            result.returncode, 0, msg=f"Script {script_name} failed: {result.stderr}"
        )

    def test_levels(self):
        """
        Tests that each level script runs successfully
        """
        scripts = [
            "levels.level_0",
            "levels.level_1",
            "levels.level_2",
            "levels.level_3",
            "levels.level_4",
            "levels.level_5",
            "levels.level_6",
            "levels.level_7",
            "levels.level_8",
            "levels.level_9",
            "levels.level_10",
            "levels.level_11",
            "levels.level_12",
            "levels.level_13",
            "levels.level_14",
            "levels.level_15",
            "levels.level_16",
        ]

        for script in scripts:
            print(f"Testing {script}... ", end="")
            sys.stdout.flush()
            with self.subTest(script=script):
                self.run_script(script)
            print("OK")
            sys.stdout.flush()


if __name__ == "__main__":
    unittest.main()

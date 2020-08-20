import fnmatch, os
from pathlib import Path

dir = Path(os.getcwd()) / "LeetCode" / "Solved"

easy = len(os.listdir( Path(dir / "Easy") ))
med = len(os.listdir( Path(dir / "Medium") ))
hard = len(os.listdir( Path(dir / "Hard") ))

total = easy + med + hard

print("Easy: ", easy)
print("Medium: ", med)
print("Hard: ", hard)
print("Total: ", total)
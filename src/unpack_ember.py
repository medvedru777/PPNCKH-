import tarfile
from pathlib import Path

input_path = Path("data/raw/ember_dataset_2018_2.tar.bz2")
output_path = Path("data/processed/ember")

output_path.mkdir(parents=True, exist_ok=True)

with tarfile.open(input_path, "r:bz2") as tar:
    tar.extractall(output_path)

print("DONE extracting:", output_path)
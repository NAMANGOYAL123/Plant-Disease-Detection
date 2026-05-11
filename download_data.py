"""
Data Collection Script for PlantVillage Dataset
Downloads and organizes the dataset from Kaggle.
"""

import os
import zipfile
import shutil
from pathlib import Path


def download_plantvillage_dataset():
    """
    Download and extract the PlantVillage dataset from Kaggle.
    """
    print("=" * 60)
    print("DOWNLOADING PLANTVILLAGE DATASET FROM KAGGLE")
    print("=" * 60)

    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nDownloading dataset into: {data_dir}")

    os.system(
        "kaggle datasets download "
        "-d abdallahalidev/plantvillage-dataset "
        f"-p {data_dir}"
    )

    zip_files = list(data_dir.glob("*.zip"))
    if not zip_files:
        print("Error: No ZIP file found. Download may have failed.")
        return False

    zip_file = zip_files[0]
    print(f"\nExtracting dataset: {zip_file.name}")

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(data_dir)

    zip_file.unlink()

    print("\nDataset extracted successfully.")
    print(f"Dataset location: {data_dir.resolve()}")

    print("\nDataset structure:")
    display_dataset_structure(data_dir)

    return True


def display_dataset_structure(data_dir: Path):
    """
    Display class-wise image counts in the dataset.
    """
    subfolders = [f for f in data_dir.iterdir() if f.is_dir()]
    if not subfolders:
        print("No dataset folders found.")
        return

    for folder in subfolders:
        print(f"\nFolder: {folder.name}")
        class_dirs = [d for d in folder.iterdir() if d.is_dir()]
        print(f"Number of classes: {len(class_dirs)}")

        total_images = 0
        for class_dir in class_dirs:
            images = list(class_dir.glob("*.jpg")) + list(class_dir.glob("*.png"))
            total_images += len(images)
            print(f"  {class_dir.name}: {len(images)} images")

        print(f"Total images: {total_images}")


def verify_dataset():
    """
    Check whether the dataset already exists.
    """
    data_dir = Path("data/raw")
    return data_dir.exists() and any(data_dir.iterdir())


if __name__ == "__main__":
    print("\nPLANT DISEASE DETECTION - DATA COLLECTION")
    print("=" * 60)

    if verify_dataset():
        response = input(
            "Dataset already exists. Re-download? (yes/no): "
        ).strip().lower()

        if response not in {"yes", "y"}:
            display_dataset_structure(Path("data/raw"))
            exit(0)

        shutil.rmtree("data/raw")
        Path("data/raw").mkdir(parents=True, exist_ok=True)

    if download_plantvillage_dataset():
        print("\nData collection completed successfully.")
        print("Next steps:")
        print("1. Explore data in notebooks/")
        print("2. Start model training")
    else:
        print("\nData collection failed.")
        print("Please verify Kaggle configuration and internet access.")

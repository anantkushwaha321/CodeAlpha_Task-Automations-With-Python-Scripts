"""
Python Automation Script: Move all .jpg files from a folder to a new folder.
Key Concepts Used: os, shutil, file handling
"""

import os
import shutil


def move_jpg_files(source_dir: str, destination_dir: str):
    """
    Scans source_dir for all .jpg files and moves them to destination_dir.
    Creates destination_dir if it doesn't already exist.
    """
    # Normalize paths
    source_dir = os.path.abspath(source_dir)
    destination_dir = os.path.abspath(destination_dir)

    print("=" * 60)
    print(" Move all .jpg files to a destination folder")
    print("=" * 60)
    print(f"Source Folder     : {source_dir}")
    print(f"Destination Folder: {destination_dir}\n")

    # Verify source directory exists
    if not os.path.exists(source_dir):
        print(f"[ERROR] Source folder does not exist: {source_dir}")
        return

    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # List all items in the source directory
    items = os.listdir(source_dir)
    jpg_files = []

    # Find matching .jpg files (case-insensitive)
    for item in items:
        source_item_path = os.path.join(source_dir, item)
        # Check if it's a file and ends with .jpg or .jpeg
        if os.path.isfile(source_item_path) and item.lower().endswith((".jpg", ".jpeg")):
            jpg_files.append(item)

    if not jpg_files:
        print("[INFO] No .jpg files found in the source directory.")
        return

    print(f"[FOUND] {len(jpg_files)} .jpg file(s) to move.\n")

    moved_count = 0
    for filename in jpg_files:
        src_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(destination_dir, filename)

        # If a file with the same name already exists in destination, handle conflict
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(destination_dir, f"{base}_{counter}{ext}")):
                counter += 1
            dest_path = os.path.join(destination_dir, f"{base}_{counter}{ext}")

        try:
            shutil.move(src_path, dest_path)
            print(f"  -> Moved: '{filename}' -> '{os.path.basename(dest_path)}'")
            moved_count += 1
        except Exception as e:
            print(f"  [!] Failed to move '{filename}': {e}")

    print("\n" + "-" * 60)
    print(f"[SUCCESS] Successfully moved {moved_count} of {len(jpg_files)} file(s).")
    print("-" * 60)


def create_sample_files(source_dir: str):
    """Helper function to create sample dummy files for testing."""
    os.makedirs(source_dir, exist_ok=True)
    sample_files = [
        "nature_photo.jpg",
        "vacation_pic.JPG",
        "avatar.jpeg",
        "document.txt",
        "data_report.pdf",
        "landscape.jpg",
    ]
    created = 0
    for fname in sample_files:
        file_path = os.path.join(source_dir, fname)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Sample dummy content for {fname}\n")
            created += 1
    if created > 0:
        print(f"[SETUP] Created {created} sample test files in '{source_dir}' for demonstration.\n")


if __name__ == "__main__":
    SOURCE_FOLDER = "source_folder"
    DEST_FOLDER = "destination_folder"

    # Automatically set up sample files if source folder has none
    create_sample_files(SOURCE_FOLDER)

    # Run the automation
    move_jpg_files(SOURCE_FOLDER, DEST_FOLDER)

"""
Main Automation Hub - Python Automation Scripts
Allows running any of the three automation scripts or all of them together.
"""

import sys
import subprocess


def show_menu():
    print("\n" + "=" * 65)
    print("         PYTHON TASK AUTOMATION HUB")
    print("=" * 65)
    print(" 1. Move all .jpg files from a folder to a new folder (os, shutil)")
    print(" 2. Extract email addresses from a .txt file (re, file handling)")
    print(" 3. Scrape webpage title and save it (requests, re, file handling)")
    print(" 4. Run all automations sequentially")
    print(" 5. Exit")
    print("=" * 65)


def run_script(script_name: str):
    print(f"\n[RUNNING] python {script_name} ...\n")
    subprocess.run([sys.executable, script_name])


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            run_script("move_jpg_files.py")
        elif choice == "2":
            run_script("extract_emails.py")
        elif choice == "3":
            run_script("scrape_webpage_title.py")
        elif choice == "4":
            print("\n>>> Running: Move .jpg files <<<")
            run_script("move_jpg_files.py")
            print("\n>>> Running: Extract email addresses <<<")
            run_script("extract_emails.py")
            print("\n>>> Running: Scrape webpage title <<<")
            run_script("scrape_webpage_title.py")
            print("\n[ALL COMPLETED SUCCESSFULLY]")
        elif choice == "5":
            print("Exiting Automation Hub. Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ("1", "jpg", "move"):
            run_script("move_jpg_files.py")
        elif arg in ("2", "email", "extract"):
            run_script("extract_emails.py")
        elif arg in ("3", "web", "scrape"):
            run_script("scrape_webpage_title.py")
        elif arg in ("4", "all"):
            run_script("move_jpg_files.py")
            run_script("extract_emails.py")
            run_script("scrape_webpage_title.py")
        else:
            print(f"Unknown argument: {arg}. Usage: python main.py [1|2|3|all]")
    else:
        main()

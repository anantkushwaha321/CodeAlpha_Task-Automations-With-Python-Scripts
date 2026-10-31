"""
Python Automation Script: Extract all email addresses from a .txt file and save them to another file.
Key Concepts Used: re (regular expressions), file handling
"""

import os
import re


def extract_emails(input_file_path: str, output_file_path: str):
    """
    Reads text from input_file_path, uses regular expressions to find all
    valid email addresses, deduplicates them, and writes them to output_file_path.
    """
    print("=" * 60)
    print(" Extract email addresses from text file")
    print("=" * 60)
    print(f"Input File : {os.path.abspath(input_file_path)}")
    print(f"Output File: {os.path.abspath(output_file_path)}\n")

    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"[ERROR] Input file '{input_file_path}' does not exist.")
        return

    # Regular expression pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Step 1: Read the input file using Python file handling
    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"[ERROR] Failed to read input file: {e}")
        return

    # Step 2: Extract all matching email addresses using re.findall
    found_emails = re.findall(email_pattern, content)

    if not found_emails:
        print("[INFO] No email addresses were found in the text file.")
        return

    print(f"[FOUND] Found {len(found_emails)} email address occurrence(s).")

    # Deduplicate while preserving order (case-insensitive deduplication)
    unique_emails = []
    seen = set()
    for email in found_emails:
        lowered = email.lower()
        if lowered not in seen:
            seen.add(lowered)
            unique_emails.append(email)

    print(f"[UNIQUE] {len(unique_emails)} unique email address(es):\n")
    for idx, email in enumerate(unique_emails, 1):
        print(f"  {idx}. {email}")

    # Step 3: Write extracted emails to the output file using file handling
    try:
        # Ensure target directory exists if specified in path
        output_dir = os.path.dirname(output_file_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write("# Extracted Email Addresses\n")
            file.write(f"# Total Unique Emails: {len(unique_emails)}\n")
            file.write("-" * 40 + "\n")
            for email in unique_emails:
                file.write(f"{email}\n")

        print("\n" + "-" * 60)
        print(f"[SUCCESS] Saved {len(unique_emails)} email(s) to '{output_file_path}'.")
        print("-" * 60)

    except Exception as e:
        print(f"[ERROR] Failed to write output file: {e}")


def create_sample_text_file(filepath: str):
    """Creates a sample text file with contacts if it doesn't already exist."""
    if not os.path.exists(filepath):
        sample_text = (
            "Team Contact Directory & Meeting Notes\n"
            "======================================\n"
            "Hello team,\n\n"
            "For project support, reach out to Alice Smith at alice.smith@example.com or support@company.org.\n"
            "You can also contact John (engineering lead) at john_doe123@techcorp.io.\n"
            "For urgent queries, email marketing team: info@marketing-hub.net or alice.smith@example.com (duplicate).\n\n"
            "Other points of contact:\n"
            "- Billing inquiry: billing+finance@startup.co\n"
            "- Feedback: feedback.user@domain.edu\n"
            "- Personal note: please do not email invalid-email@ or @nodomain.com\n\n"
            "Best regards,\n"
            "HR Office (hr.department@globalcorp.com)\n"
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(sample_text)
        print(f"[SETUP] Created sample text file '{filepath}' for demonstration.\n")


if __name__ == "__main__":
    INPUT_FILE = "sample_contacts.txt"
    OUTPUT_FILE = "extracted_emails.txt"

    # Create dummy input file if not present
    create_sample_text_file(INPUT_FILE)

    # Run the email extraction
    extract_emails(INPUT_FILE, OUTPUT_FILE)

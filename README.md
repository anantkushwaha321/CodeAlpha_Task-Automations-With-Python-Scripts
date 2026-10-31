# Task Automation with Python Scripts

This project contains Python scripts designed to automate small, repetitive real-life tasks.

---

## 🎯 Automations Included
1. **Move all `.jpg` files from a folder to a new folder** (`move_jpg_files.py`)
2. **Extract all email addresses from a `.txt` file and save them to another file** (`extract_emails.py`)
3. **Scrape the title of a fixed webpage and save it** (`scrape_webpage_title.py`)

All scripts are fully functional, commented, and can be run independently or via `main.py`.

---

## 🛠️ Key Concepts & Libraries Used

| Script | Description | Key Concepts / Modules |
| :--- | :--- | :--- |
| **`move_jpg_files.py`** | Scans a folder for `.jpg`/`.jpeg` files and moves them to a destination directory. | `os`, `shutil`, directory traversal, path handling |
| **`extract_emails.py`** | Reads text from a file, extracts valid email addresses via regex, and writes them to an output file. | `re` (regular expressions), file handling (`open`, read, write) |
| **`scrape_webpage_title.py`** | Fetches the HTML of a webpage over HTTP, parses the `<title>` tag, and saves it. | `requests`, `re`, HTTP headers, file handling |

---

## 🚀 How to Run the Scripts

### Option A: Central Menu Runner
Run the interactive console menu:
```bash
python main.py
```
Or pass an argument directly:
```bash
python main.py 1    # Runs .jpg mover
python main.py 2    # Runs Email extractor
python main.py 3    # Runs Webpage title scraper
python main.py all  # Runs all sequentially
```

---

### Option B: Run Scripts Individually

#### 1. Move `.jpg` Files
```bash
python move_jpg_files.py
```
- Automatically sets up a `source_folder` with sample images (`.jpg`, `.jpeg`) and other files (`.txt`, `.pdf`) if not present.
- Detects all `.jpg`/`.jpeg` files case-insensitively.
- Safely moves the files into `destination_folder` using `shutil.move()`, handling name collisions gracefully.

#### 2. Extract Email Addresses
```bash
python extract_emails.py
```
- Automatically generates `sample_contacts.txt` with sample text and emails if absent.
- Uses regex pattern `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` to extract all valid emails.
- Deduplicates emails while preserving occurrence order.
- Writes the results cleanly to `extracted_emails.txt`.

#### 3. Scrape Webpage Title
```bash
python scrape_webpage_title.py
```
- Sends an HTTP GET request to `https://example.com` using the `requests` library.
- Extracts the text between `<title>...</title>` using regular expressions (`re`).
- Cleans whitespace and decodes HTML entities.
- Writes the title, target URL, and timestamp to `webpage_title.txt`.

---

## 📁 File Structure
```
c:\Task Automations\
├── main.py                     # Central menu runner
├── move_jpg_files.py           # Script to move .jpg files
├── extract_emails.py           # Script to extract emails from text
├── scrape_webpage_title.py     # Script to scrape webpage title
├── source_folder/              # Source directory for image moving
├── destination_folder/         # Destination directory for images
├── sample_contacts.txt         # Input text file with sample emails
├── extracted_emails.txt        # Output file containing extracted emails
├── webpage_title.txt           # Output file containing scraped webpage title
└── README.md                   # Documentation
```

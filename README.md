# School & NCC Records Manager

A small collection of Python command-line scripts for managing school administration records and NCC (National Cadet Corps) cadet enrollment. All data is stored in plain CSV files for easy viewing and portability.

## Contents

| File | Purpose |
| --- | --- |
| `hello.py` | Multi-purpose school management menu (Admission, TC, Marks, Suggestions, Library) |
| `main.py` | NCC cadet enrollment form that appends records to `enrollment 2023-24.csv` |
| `enrollment 2023-24.csv` | Sample / live data file produced by `main.py` |
| `pyproject.toml` | Poetry project configuration and dependencies |

## Features

### `hello.py` — School Management System
Run the script and pick one of the menu options:

1. **Admission** — Collect candidate details (name, DOB, parents, blood group, class, caste, etc.) and assign a random 5-digit admission number. Saved to `helio3.O.csv`.
2. **TC (Transfer Certificate)** — Record a TC request with name, admission number, and reason. Saved to `tc.csv`.
3. **Marks** — Enter marks for English, Hindi, Maths, Social Science and Science for one or more students. Calculates average and grade. Saved to `marks.csv`.
4. **Suggestion** — Capture a suggestion from a parent. Saved to `suggestion.csv`.
5. **Library Management** — Display, add, issue, and return books stored in `library.csv`.

### `main.py` — NCC Cadet Enrollment
A long enrollment form for NCC cadets that captures group, battalion, regimental number, full names of cadet and parents, contact details, academic stream, marks, bank details, and more. Records are appended to `enrollment 2023-24.csv` so existing data is preserved across sessions.

## Requirements

- Python `>=3.10, <3.11`
- Standard library only for the core scripts (`csv`, `random`)
- Optional dev dependencies are listed in `pyproject.toml` (managed via Poetry)

## Running

From the project root:

```bash
# School management menu
python hello.py

# NCC cadet enrollment
python main.py
```

Each script is interactive — answer the prompts in the terminal. CSV files are written to the project root.

## Data Files

All output is in CSV format and can be opened in Excel, Google Sheets, or any text editor:

- `helio3.O.csv` — admissions
- `tc.csv` — transfer certificates
- `marks.csv` — student marks and grades
- `suggestion.csv` — parent suggestions
- `library.csv` — library inventory
- `enrollment 2023-24.csv` — NCC cadet enrollment

## Notes & Known Limitations

- Inputs are not validated heavily — entering the wrong type (e.g. text where a number is expected) will raise an error.
- `hello.py` opens output files in write mode (`'w'`), so re-running an option will overwrite previous data for that section. `main.py` uses append mode (`'a'`) and preserves history.
- The scripts use `eval()` for some numeric inputs; only enter trusted values.
- Mobile-number length checks print a warning but do not stop execution.

## License

No license specified. Add one if you plan to share or distribute this project.

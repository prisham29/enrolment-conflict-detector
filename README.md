# Enrolment Conflict Detector

A Python automation tool that scans student booking data and 
automatically flags scheduling conflicts, missing assignments, 
and incomplete records — then saves a timestamped report.

## The problem it solves

Manual student enrolment processes create recurring errors:
- Tutors double-booked at the same time slot
- Students assigned no tutor
- Missing contact information

This tool automates the detection of all three — built from 
real inefficiencies observed during IT coordination work at 
a tutoring centre.

## How to run it

**Print results to terminal:**
```bash
python3 detector.py
```

**Generate a saved report file:**
```bash
python3 generate_report.py
```

Reports are saved to the `/reports` folder with a timestamp.

## Example output
```
============================================================
  ENROLMENT CONFLICT DETECTOR — REPORT
============================================================

  Summary:
    Double booking: 2 issue(s)
    Missing tutor: 2 issue(s)
    Missing contact: 1 issue(s)

  Full details:

  [1] [HIGH] Double booking
      Booking(s): B001 and B002
      Detail:     Mr. Patel is booked twice at Mon 9am

  [2] [HIGH] Double booking
      Booking(s): B003 and B008
      Detail:     Ms. Taylor is booked twice at Mon 11am

  [3] [HIGH] Missing tutor
      Booking(s): B004
      Detail:     Liam Park has no tutor assigned

  [4] [HIGH] Missing tutor
      Booking(s): B010
      Detail:     Daniel Tran has no tutor assigned

  [5] [MEDIUM] Missing contact
      Booking(s): B006
      Detail:     Tom Nguyen has no contact email

============================================================
```

## Project structure
```
enrolment-conflict-detector/
├── data.csv              ← sample input data
├── detector.py           ← core detection logic
├── generate_report.py    ← automation + report saving
├── reports/              ← auto-generated reports land here
└── README.md             ← documentation
```

## Built with

- Python 3
- csv module (built-in)
- datetime module (built-in)
- No external dependencies required

## Background

Built from real process inefficiencies identified during IT 
coordination work at a tutoring centre. The tool demonstrates 
how a business problem — manual booking errors causing 
operational disruptions — can be solved through automation 
and structured data validation.

## Author

Prisha Muneshwar  
github.com/prisham29  
linkedin.com/in/prishamuneshwar
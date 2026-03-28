"""
Enrolment Conflict Detector
----------------------------
Reads student booking data and flags:
  1. Double-booked tutors
  2. Missing tutor assignments  
  3. Missing contact emails

Built by: Prisha Muneshwar
GitHub:   github.com/prisham29
"""

import csv
from datetime import datetime


# ── LOAD DATA ─────────────────────────────────────────────
# Opens your CSV and returns every row as a dictionary.
# A dictionary maps column names to values — like a row in Excel.
# Example: {"booking_id": "B001", "student_name": "Sarah Chen", ...}

def load_bookings(filename):
    bookings = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bookings.append(row)
    return bookings


# ── CHECK 1: DOUBLE BOOKINGS ───────────────────────────────
# Logic: if the same tutor appears at the same time twice — conflict.
# We use a dictionary to track every (tutor, time) pair we've seen.
# First time we see it: store it.
# Second time we see it: flag it as a conflict.

def find_double_bookings(bookings):
    seen = {}
    conflicts = []

    for row in bookings:
        tutor = row["tutor_name"].strip()
        time  = row["session_time"].strip()
        bid   = row["booking_id"].strip()

        if not tutor:
            continue

        key = (tutor, time)

        if key in seen:
            conflicts.append({
                "type":     "Double booking",
                "bookings": f"{seen[key]} and {bid}",
                "detail":   f"{tutor} is booked twice at {time}",
                "severity": "HIGH"
            })
        else:
            seen[key] = bid

    return conflicts


# ── CHECK 2: MISSING TUTORS ────────────────────────────────
# Logic: if tutor_name is empty — flag it.
# .strip() removes accidental spaces so "  " counts as empty too.

def find_missing_tutors(bookings):
    issues = []
    for row in bookings:
        if not row["tutor_name"].strip():
            issues.append({
                "type":     "Missing tutor",
                "bookings": row["booking_id"],
                "detail":   f"{row['student_name']} has no tutor assigned",
                "severity": "HIGH"
            })
    return issues


# ── CHECK 3: MISSING CONTACTS ──────────────────────────────
# Logic: if contact_email is empty — flag it.

def find_missing_contacts(bookings):
    issues = []
    for row in bookings:
        if not row["contact_email"].strip():
            issues.append({
                "type":     "Missing contact",
                "bookings": row["booking_id"],
                "detail":   f"{row['student_name']} has no contact email",
                "severity": "MEDIUM"
            })
    return issues


# ── SUMMARY STATS ──────────────────────────────────────────
# Counts how many of each issue type we found.
# This goes into the report header so it's easy to scan.

def get_summary(all_issues):
    summary = {"Double booking": 0, "Missing tutor": 0, "Missing contact": 0}
    for issue in all_issues:
        if issue["type"] in summary:
            summary[issue["type"]] += 1
    return summary


# ── PRINT TO TERMINAL ──────────────────────────────────────

def print_report(all_issues):
    print("\n" + "=" * 60)
    print("  ENROLMENT CONFLICT DETECTOR — REPORT")
    print("=" * 60)

    if not all_issues:
        print("  No issues found. All bookings look clean.")
    else:
        summary = get_summary(all_issues)
        print(f"\n  Summary:")
        for issue_type, count in summary.items():
            if count > 0:
                print(f"    {issue_type}: {count} issue(s)")

        print(f"\n  Full details:\n")
        for i, issue in enumerate(all_issues, 1):
            print(f"  [{i}] [{issue['severity']}] {issue['type']}")
            print(f"      Booking(s): {issue['bookings']}")
            print(f"      Detail:     {issue['detail']}")
            print()

    print("=" * 60 + "\n")


# ── MAIN ───────────────────────────────────────────────────
# This only runs when you execute this file directly.
# It ties everything together.

if __name__ == "__main__":
    FILE = "data.csv"

    print(f"\nLoading bookings from '{FILE}'...")
    bookings = load_bookings(FILE)
    print(f"  {len(bookings)} bookings loaded.")

    all_issues = (
        find_double_bookings(bookings) +
        find_missing_tutors(bookings) +
        find_missing_contacts(bookings)
    )

    print_report(all_issues)
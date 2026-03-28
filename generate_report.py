"""
Report Generator
-----------------
Runs the conflict detector and saves a timestamped
report to a /reports folder automatically.
"""

import os
from datetime import datetime
from detector import load_bookings, find_double_bookings, find_missing_tutors, find_missing_contacts, get_summary


def save_report(all_issues, bookings):

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Timestamp so every report has a unique name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/report_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("  ENROLMENT CONFLICT DETECTOR — AUTOMATED REPORT\n")
        f.write(f"  Generated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}\n")
        f.write(f"  Total bookings scanned: {len(bookings)}\n")
        f.write("=" * 60 + "\n\n")

        if not all_issues:
            f.write("  No issues found. All bookings look clean.\n")
        else:
            summary = get_summary(all_issues)

            f.write("  SUMMARY\n")
            f.write("  -------\n")
            for issue_type, count in summary.items():
                f.write(f"  {issue_type}: {count} issue(s)\n")

            f.write(f"\n  Total issues found: {len(all_issues)}\n")
            f.write("\n" + "-" * 60 + "\n\n")

            f.write("  FULL DETAILS\n")
            f.write("  ------------\n\n")

            for i, issue in enumerate(all_issues, 1):
                f.write(f"  [{i}] [{issue['severity']}] {issue['type']}\n")
                f.write(f"       Booking(s): {issue['bookings']}\n")
                f.write(f"       Detail:     {issue['detail']}\n\n")

        f.write("=" * 60 + "\n")
        f.write("  END OF REPORT\n")
        f.write("=" * 60 + "\n")

    print(f"\n  Report saved to: {filename}")
    return filename


if __name__ == "__main__":
    FILE = "data.csv"

    print(f"\nRunning conflict detection on '{FILE}'...")
    bookings = load_bookings(FILE)
    print(f"  {len(bookings)} bookings loaded.")

    all_issues = (
        find_double_bookings(bookings) +
        find_missing_tutors(bookings) +
        find_missing_contacts(bookings)
    )

    print(f"  {len(all_issues)} issue(s) found.")
    save_report(all_issues, bookings)
    print("\nDone. Check the /reports folder.\n")
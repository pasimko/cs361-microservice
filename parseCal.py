import icalendar
import csv
import urllib.request
import sys

id = "user_kxZN5GQfp8YaixypXoAe8MYU44NVaDJ7XV8b5dCA" # Anthony calendar
if len(sys.argv) > 1:
    id = sys.argv[1]
output = id + ".csv"

url = "https://canvas.oregonstate.edu/feeds/calendars/" + id + ".ics"
gcal = None

try:
    with urllib.request.urlopen(url) as f:
        print("Fetching " + url)
        gcal = icalendar.Calendar.from_ical(f.read())

except urllib.error.URLError as e:
    print(f"Error fetching {url}: {e}")
    sys.exit(1)
except icalendar.exceptions.CalendarException as e:
    print(f"Error parsing calendar data: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

with open(output, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for component in gcal.walk():
        if component.name == "VEVENT":
            summary = component.get('SUMMARY') # Format: Final Project Proposal [INTRO TO COMPUTER GRAPHICS (CS_450_X001_F2023)]
            dtstart = component.get('DTSTART') # Format: vDDDTypes(2023-12-11, Parameters({'VALUE': 'DATE'}))
            print(summary) 
            print(dtstart.dt) 
            dtstart = dtstart.dt # Format: 2023-12-11

            # Write the data to the CSV file
            csv_writer.writerow([summary, dtstart])

import csv
from django.utils import timezone
from traffic_app.models import TrafficData  # replace with your app name
from datetime import datetime

# Path to your CSV file
CSV_FILE_PATH = "traffic_data.csv"  # update with your actual file name

def run():
    with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Parse date_time from CSV (adjust format to your CSV)
                date_time = datetime.strptime(row['date_time'], "%Y-%m-%d %H:%M:%S")

                TrafficData.objects.get_or_create(
                    date_time=date_time,
                    location=row['location'],
                    vehicle_count=int(row['vehicle_count']),
                    average_speed=float(row['average_speed']),
                    congestion_level=row.get('congestion_level', None)
                )
            except Exception as e:
                print(f"Error importing row {row}: {e}")

    print("✅ CSV import completed.")

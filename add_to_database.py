from supabase import create_client, Client
import os
from dotenv import load_dotenv


# Supabase setup
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Student data
data = {
    "100000": {
        "name": "Shalom Harlow",
        "major": "Computer Sc",
        "starting_year": 2025,
        "total_attendance": 0,
        "year": 2,
        "last_attendance_time": "1999-12-11 00:54:34"
    },
    "100001": {
        "name": "Pamela Anderson",
        "major": "Computer Sc",
        "starting_year": 2025,
        "total_attendance": 0,
        "year": 2,
        "last_attendance_time": "1999-12-11 00:54:34"
    },
    "100002": {
        "name": "Yasmeen Ghauri",
        "major": "Computer Sc",
        "starting_year": 2025,
        "total_attendance": 0,
        "year": 2,
        "last_attendance_time": "1999-12-11 00:54:34"
    }
}

records = [{**student_data, "student_id": student_id} for student_id, student_data in data.items()]
response = supabase.table("students").upsert(records, on_conflict="student_id").execute()
if response.data:
    print(f"Successfully inserted or updated {len(response.data)} students.")
else:
    print("No new data inserted or updated, or the operation failed.")


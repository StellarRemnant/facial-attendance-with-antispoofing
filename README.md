# Smart Attendance System with Facial Recognition and Anti-Spoofing

A real-time attendance system that registers attendance via facial recognition with integrated anti-spoofing measures. The system updates attendance records in the database live, ensuring accurate and secure verification of identity.

## Features

- Real-time attendance registration using facial recognition.
- Anti-spoofing
- Attendance records include timestamps for accurate tracking.
- Integration with Supabase for database and storage.
- Supports management of student data and facial encoding generation.

---

## Installation and Setup

1. **Clone the repository and install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Set up Supabase:**

- Sign up at [Supabase](https://supabase.com) and create a new project.
- Create two tables in your Supabase database: `students` and `encodings`. (Schemas are provided in the `table_schemas` directory.)
- Create an `images` directory in Supabase Storage.

3. **Prepare your local environment**

- Place student images (216x216 pixels) inside the local `images` directory under the project root.
- Fill student information in `add_to_database.py`.

4. **Configure environment variables**

- Copy your Supabase project URL and API key to the `.env` file, replacing the placeholders for `SUPABASE_URL` and `SUPABASE_KEY`.

5. **Populate the database**

```bash
python add_to_database.py
```
```bash
python encodings_generator.py
```

6. **Run the attendance system:**

```bash
python main.py
```
---

## Project Structure

- `tables_schemas/` - SQL schemas for `students` and `encodings` tables.
- `images/` - Local folder for student face images (216x216 pixels).
- `a_s/` — Contains the integrated anti-spoofing model code (Silent Face Anti-Spoofing).
- `Resources/` — Holds background assets for the webcam view and UI mode images that reflect the current system state.
- `add_to_database.py` - Script to add student info to Supabase.
- `encodings_generator.py` - Script to generate facial encodings and upload.
- `main.py` - Main application script.
- `without_antispoofing.py` - Script to run the attendance system without the anti-spoofing module (for testing or baseline comparison).

---

## Known Limitations

- False negatives and positives can occur due to processing delays.

---

## Acknowledgements

This project is based on an open-source attendance system originally built with Firebase and facial recognition:

- [Original Attendance System](https://github.com/amithhd/Face_Recognition_With_Real_Time.git)  

Modifications and enhancements made in this project:
- Switched backend from **Firebase** to **Supabase**.
- Integrated anti-spoofing using the [Silent Face Anti-Spoofing model](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing.git).

---



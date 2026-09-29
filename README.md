# Event Management System - Introduction to Problem Solving and Programming Project

## 📌Overview
This is a Python based desktop application with a simple graphical interface (GUI) for planning and keeping track of events, designed to help users record upcoming meetings, birthdays, workshops and other events without relying on paper diaries or online calendar accounts. The user fills in a small form in a window and clicks buttons to add or delete events, and all events are saved to a local JSON file, so they remain available across sessions without needing an internet connection.

## 📌Features
* Event Scheduling: Record events with a name, date, category, and an optional venue using a simple form.
* Category Selection: Choose a category like Meeting, Birthday, Workshop, Seminar, etc. from a dropdown, or type its number or name in any case (e.g. "meeting" or "MEETING").
* Sorted Table: Events are shown in a table automatically arranged by date so the nearest event is always at the top.
* Past Events Highlight: Events whose date has already passed are shown in grey.
* Persistent Storage: Automatically saves all events to a local JSON file so data isn't lost when the program closes.
* Input Validation: Rejects a blank name, a wrongly formatted date, a past date and an invalid category, with a clear error pop-up.
* Delete Events: Remove cancelled or incorrect events by selecting a row and clicking "Delete Selected" (with a Yes/No confirmation).
* Event Counter: Displays the total number of events and how many are still upcoming.
* Simple GUI: One window with a form, four buttons (Add Event, Delete Selected, Clear Form, Exit) and an event table. Pressing Enter also adds an event.
* Object-Oriented Design: The code is organised into three small classes, each with one job.

## 📌Code Design (Classes)
| Class | What it does |
|---|---|
| `Event` | Stores the details of one event (name, date, category, venue) and turns it into a dictionary for saving or a line of text for display. |
| `EventManager` | Keeps the list of events and handles loading, saving, adding, deleting and counting upcoming events. |
| `EventApp` | Shows the menu, reads the user's input, validates it and prints the results. |

Keeping the data (`Event`, `EventManager`) separate from the menu (`EventApp`) means each part can be understood and changed on its own.

## 📌Technologies/Tools Used
* Programming Language: Python 3.7
* Interface: Graphical User Interface (Tkinter)
* Data Format: JSON (local file storage)
* Standard Library: tkinter, os, datetime, json

## 📌Steps to Install & Run the Project
### 1. *Requirement:*
Make sure that Python is installed on your system. You can check this by running:
```bash
python --version
```
### 2. *Clone/Download the Repository:*
Download the project files to your local machine.
### 3. *Install Dependencies:*
This project only uses Python's standard library, so no extra installation is required.
### 4. *▶️ Run the Application:*
Go to your project directory and run the script:
```bash
python Event_Manager.py
```

## 📌Instructions for Testing
Conduct the following tests to ensure that the application works as anticipated.

### 1. *Standard Entry Test:*
* Run the program. The Event Manager window opens.
* Enter "Tech Fest" as the name and "2026-12-15" as the date.
* Choose "Workshop" from the category dropdown (or type 3 or "workshop"), and enter "Main Auditorium" as the venue.
* Click "Add Event" (or press Enter).
* Expected Output: An "Event added!" pop-up appears, the event is listed in the table and the counter shows "Total Events: 1 | Upcoming: 1".

### 2. *Input Validation Test:*
* Leave the name blank, or type a date like "15/12/2026", or enter a past date, then click "Add Event".
* Expected Output: An error pop-up such as "Please Enter An Event Name", "Please Enter The Date As YYYY-MM-DD" or "Event Date Cannot Be In The Past".
* Type "xyz" in the category box and click "Add Event".
* Expected Output: "Please Choose A Valid Category".
* Click "Delete Selected" without selecting any row.
* Expected Output: "Please Select An Event To Delete".

### 3. *Sorting Test:*
* Add an event for a later date, then one for an earlier date.
* Expected Output: The earlier event is shown above the later one in the table.

### 4. *Persistence Test:*
* Add a few events and click "Exit".
* Run the program again.
* Expected Output: The previously added events are already shown in the table, loaded automatically from events.json.

### 5. *Delete Event Test:*
* Click on an event in the table, then click "Delete Selected" and choose "Yes".
* Expected Output: "Event deleted!" pop-up and the event is removed from the table.

## 📌Sample Output
```
===== Event Manager =====
1. Add Event
2. View Events
3. Delete Event
4. Exit
Enter your choice: 2

Scheduled Events:
  1. 2026-10-05 | Team Meet | Meeting |
  2. 2026-12-15 | Tech Fest | Workshop | Main Auditorium
Total Events: 2   |   Upcoming: 2
```

## 📌Project Structure
```
event manager
├── Event_Manager.py
├── events.json   (created automatically on first run)
├── README.md
├── statement.md
└── Report.pdf
```
## 📌Screenshots
1. Adding an event 
<img width="461" height="438" alt="image" src="https://github.com/user-attachments/assets/bc60af57-4959-4d6c-9c78-eef264614aa1" />

2. Viewing the event list, sorted by date
<img width="575" height="232" alt="image" src="https://github.com/user-attachments/assets/2638b119-d5e7-490d-8ac7-9e026f967174" />

3. Error messages for a blank name, a wrong date format, a past date and a wrong menu choice
<img width="462" height="208" alt="image" src="https://github.com/user-attachments/assets/023340dd-71f8-4988-b798-5bf294e352b4" />

4. Deleting an event
<img width="573" height="276" alt="image" src="https://github.com/user-attachments/assets/2b0a8cf7-a300-462e-b156-d0c2b9e38962" />


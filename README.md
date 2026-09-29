# Event Management System - Introduction to Problem Solving and Programming Project

## 📌Overview
This is a Python based command line application for planning and keeping track of events, designed to help users record upcoming meetings, birthdays, workshops and other events without relying on paper diaries or online calendar accounts. The user works through a simple numbered menu in the terminal, and all events are saved to a local JSON file, so they remain available across sessions without needing an internet connection.

## 📌Features
* Event Scheduling: Record events with a name, date, category, and an optional venue.
* Category Selection: Choose a category like Meeting, Birthday, Workshop, Seminar, etc. by its number or by typing its name in any case (e.g. "meeting" or "MEETING").
* Sorted List: Events are automatically arranged by date so the nearest event is always at the top.
* Persistent Storage: Automatically saves all events to a local JSON file so data isn't lost when the program closes.
* Input Validation: Rejects a blank name, a wrongly formatted date, a past date, and invalid menu choices.
* Delete Events: Remove cancelled or incorrect events by their number in the list.
* Event Counter: Displays the total number of events and how many are still upcoming.
* Simple Menu: A numbered menu (Add, View, Delete, Exit) that runs in any terminal.
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
* Interface: Command line (terminal)
* Data Format: JSON (local file storage)
* Standard Library: os, datetime, json

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
* Run the program and choose 1 (Add Event).
* Enter "Tech Fest" as the name and "2026-12-15" as the date.
* Choose the category by typing 3, or "workshop" in lowercase, and enter "Main Auditorium" as the venue.
* Choose 2 (View Events).
* Expected Output: The event is listed and the counter shows "Total Events: 1 | Upcoming: 1".

### 2. *Input Validation Test:*
* Choose 1 and leave the name blank, or type a date like "15/12/2026", or enter a past date.
* Expected Output: An error message such as "Please enter an event name", "Please enter the date as YYYY-MM-DD" or "Event date cannot be in the past".
* At the main menu, type 9.
* Expected Output: "Please enter a number from 1 to 4".

### 3. *Sorting Test:*
* Add an event for a later date, then one for an earlier date, and choose 2.
* Expected Output: The earlier event is shown above the later one.

### 4. *Persistence Test:*
* Add a few events and choose 4 (Exit).
* Run the program again and choose 2.
* Expected Output: The previously added events are still listed, loaded automatically from events.json.

### 5. *Delete Event Test:*
* Choose 3 (Delete Event) and enter the number of an event.
* Expected Output: "Event deleted!" and the event no longer appears when you choose 2.

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
![alt text](image.png)
 
2. Viewing the event list, sorted by date

 
3. Error messages for a blank name, a wrong date format, a past date and a wrong menu choice

 
4. Deleting an event


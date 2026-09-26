# Symptom and Medication Journal

## 📌**Overview**

The Symptom & Medication Journal helps users track their health by recording medications taken or symptoms experienced.
It allows users to log occurrences (e.g., taking a medication or feeling a specific symptom) and view a live summary of their health events.
It is a desktop application with a simple Tkinter GUI, beginner-friendly and easy to use.

## 📌**Features**
* **Add Item:** Register a new medication or symptom (Name + Category, chosen from a dropdown).
* **Log Event:** Select an item from the list and log an occurrence for it (increments the event count and records the time).
* **Live Journal View:** A single list shows every tracked item along with its total occurrence count and the time it was last logged — this doubles as the summary.
* **Delete Item:** Remove an item you no longer want to track.
* **Simple Interface:** Clean, form-based window — no typing menu numbers required.

## 📌**Technology**
* **Language:** Python 3.7
* **GUI Framework:** Tkinter
* **Data Structure:** List of Dictionaries (kept in memory while the app is running)

## 📌**Testing Instructions**

### Test Case 1: Add a health item (medication or symptom)

Enter Name: Fever.
Select Category: Symptom.
Click "Add Item".
Expected Result: Popup confirms "'Fever' added to your journal!" and it appears in the journal list.

### Test Case 2: Log an occurrence

Select "Fever" in the journal list.
Click "Log Event".
Expected Result: Popup confirms "Logged event for Fever!" and the list updates to show Total: 1 and the current time.

### Test Case 3: Invalid Input (Non-Functional Testing)

Leave the Name field blank and click "Add Item".
Expected Result: A warning pop-up appears ("Please enter a name") instead of the app crashing.

### Test Case 4: Log Event with Nothing Selected

Click "Log Event" without selecting anything in the journal list.
Expected Result: A warning pop-up appears ("Please select an item to log").

## 📌**How to Run**
1. Ensure you have Python installed.
2. Open your terminal or command prompt.
3. Run the command:
   ```bash
   python Symptom_Medication_Journal.py
   ```

## 📌**Project Structure**
```
Symptom & Medication Journal/
  ├── Symptom_Medication_Journal.py
  ├── README.md
  ├── statement.md
  ├── Report.pdf
  └── /recordings
```

## 📌**Screenshots**
### 1. Adding a new item

<img width="510" height="400" alt="Add Item screenshot" src="screenshots/add_item.png" />

### 2. Logging an event for a selected item

<img width="510" height="400" alt="Log Event screenshot" src="screenshots/log_event.png" />

### 3. Viewing the journal summary with counts and last-logged times

<img width="510" height="400" alt="Journal View screenshot" src="screenshots/journal_view.png" />



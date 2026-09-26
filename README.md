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

<img width="682" height="845" alt="Screenshot 2026-09-26 232005" src="https://github.com/user-attachments/assets/c41bf161-c434-4600-b895-55e3b0a5f702" />

### 2. Logging an event for a selected item

<img width="1042" height="840" alt="Screenshot 2026-09-26 232036" src="https://github.com/user-attachments/assets/fc4dac89-59a0-4084-8dea-c0b59173598a" />

### 3. Viewing the journal summary with counts and last-logged times

<img width="681" height="823" alt="Screenshot 2026-09-26 232135" src="https://github.com/user-attachments/assets/5e383a74-9a7f-4cca-8684-72a1cf638f68" />

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
data = []

class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Symptom & Medication Journal")
        self.root.geometry("500x550")

        self.create_widgets()
        self.refresh_list()

    def create_widgets(self):

        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=10)

        tk.Label(add_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(add_frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_var = tk.StringVar(value="Medication")
        category_menu = ttk.Combobox(
            add_frame, textvariable=self.category_var,
            values=["Medication", "Symptom"], width=22, state="readonly"
        )
        category_menu.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(add_frame, text="Add Item", bg="light blue", command=self.add_item).grid(
            row=2, column=0, columnspan=2, pady=10
        )

        tk.Label(self.root, text="Your Journal:", font=("Times New Roman", 12, "bold")).pack(pady=(10, 0))

        self.journal_list = tk.Listbox(self.root, width=60, height=15, exportselection=False)
        self.journal_list.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Log Event", bg="light green", command=self.log_occurrence).grid(
            row=0, column=0, padx=10
        )
        tk.Button(button_frame, text="Delete Selected", bg="light coral", command=self.delete_item).grid(
            row=0, column=1, padx=10
        )

    def add_item(self):
        name = self.name_entry.get().strip().title()
        category = self.category_var.get()

        if not name:
            messagebox.showwarning("Missing Info", "Please enter a name")
            return

        data.append({"name": name, "category": category, "count": 0, "last_logged": "Never"})

        self.name_entry.delete(0, tk.END)
        self.refresh_list()
        messagebox.showinfo("Item Added", f"'{name}' added to your journal!")

    def log_occurrence(self):
        selection = self.journal_list.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to log")
            return

        item = data[selection[0]]
        item["count"] += 1
        item["last_logged"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        self.refresh_list()
        messagebox.showinfo("Logged", f"Logged event for {item['name']}!")

    def delete_item(self):
        selection = self.journal_list.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to delete")
            return

        del data[selection[0]]
        self.refresh_list()


    def refresh_list(self):
        self.journal_list.delete(0, tk.END)
        for item in data:
            line = (
                f"{item['name']} ({item['category']})  -  "
                f"Total: {item['count']}  -  Last: {item['last_logged']}"
            )
            self.journal_list.insert(tk.END, line)


if __name__ == "__main__":
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()

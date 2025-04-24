import tkinter as tk
from tkinter import messagebox
from flightstrip import FlightStrip
import json
import os

DATA_FILE = "data.json"

class FlightStripApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Electronic Flight Strip System")

        # Container for strips
        self.strip_frame = tk.Frame(self.root)
        self.strip_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add Strip Button
        self.add_button = tk.Button(self.root, text="➕ Add Flight Plan", command=self.open_add_form)
        self.add_button.pack(pady=5)

        self.strips = []
        self.load_strips()

    def open_add_form(self):
        form = tk.Toplevel(self.root)
        form.title("Add Flight Plan")

        labels = ["Callsign", "Aircraft Type", "Departure", "Destination", "Altitude", "Route", "ETD"]
        entries = []

        for idx, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=idx, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(form, width=30)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            entries.append(entry)

        def submit():
            data = [e.get() for e in entries]
            if any(not field.strip() for field in data):
                messagebox.showerror("Error", "All fields are required.")
                return

            new_strip = FlightStrip(*data)
            self.strips.append(new_strip)
            self.render_strip(new_strip)
            self.save_strips()
            form.destroy()

        tk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def render_strip(self, strip):
        card = tk.Frame(self.strip_frame, bd=2, relief=tk.RIDGE, padx=10, pady=5)
        card.pack(pady=5, fill=tk.X)

        for key, value in strip.to_dict().items():
            line = f"{key}: {value}"
            tk.Label(card, text=line, anchor="w").pack(anchor="w")

    def save_strips(self):
        data = [strip.to_dict() for strip in self.strips]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_strips(self):
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return  # file is empty; nothing to load
                data = json.loads(content)
                for item in data:
                    strip = FlightStrip(**item)
                    self.strips.append(strip)
                    self.render_strip(strip)
        except json.JSONDecodeError:
            messagebox.showwarning("Warning", "data.json is corrupted. Starting fresh.")



if __name__ == "__main__":
    root = tk.Tk()
    app = FlightStripApp(root)
    root.mainloop()

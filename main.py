from tkinter import *

# List of registered clubs in the system
registered_clubs = ["Software", "Music", "Chess", "Art","dance","Language"]

def check_club():
    # Get the text entered in Entry and remove leading/trailing spaces
    entered_club = entry_club.get().strip()
    
    # Empty input check
    if not entered_club:
        label_result.config(text="Please enter a club name!", fg="orange")
        return

    # Case-insensitive search control
    is_found = False
    for club in registered_clubs:
        if entered_club.lower() == club.lower():
            is_found = True
            break

    # Item 7: Club check and message display
    if is_found:
        label_result.config(text="Registration available.", fg="green")
    else:
        label_result.config(text="Club not found", fg="red")

    # Item 8: Clear Entry field after operation
    entry_club.delete(0, END)

# Create main window
window = Tk()
window.title("School Club Registration Check System")

# Items 1, 2, and 3: Size constraints
window.geometry("400x250")  # Initial size
window.minsize(300, 200)   # Minimum size
window.maxsize(500, 300)   # Maximum size

# Centering column for grid layout
window.columnconfigure(0, weight=1)

# Item 4: "Enter Club Name" text at top
label_title = Label(window, text="Enter Club Name", font=("Arial", 12, "bold"))
label_title.grid(row=0, column=0, pady=(20, 5), padx=10)

# Item 5: Entry field
entry_club = Entry(window, font=("Arial", 11), width=25)
entry_club.grid(row=1, column=0, pady=5, padx=10)

# Item 6: "Check" button
button_check = Button(window, text="Check", font=("Arial", 10, "bold"), command=check_club)
button_check.grid(row=2, column=0, pady=10, padx=10)

# Item 7: Label area where result will be shown
label_result = Label(window, text="", font=("Arial", 11, "bold"))
label_result.grid(row=3, column=0, pady=10, padx=10)

# Start application
window.mainloop()

import tkinter as tk
from tkinter import filedialog

############################## event handlers #######################################

#Event handler for the 'SQL script file' button
def get_script_file():
  filename = filedialog.askopenfilename(title = "Select a SQL script file")
  sql_script_textbox.delete(0, tk.END)
  sql_script_textbox.insert(0, filename)

#Event handler for the 'Database file' button
def get_db_file():
  filename = filedialog.askopenfilename(title = "Select a SQLite or Ms-Access database file")
  db_textbox.delete(0, tk.END)
  db_textbox.insert(0, filename)

#Event handler for the 'Close' button
def close_it():
  exit(0)

#Event handler for the 'Run' button
def run_it():
  pass #remove this statement
  #Clear the listbox
  sql_display_listbox.delete(0, tk.END) 
  
  #Connect to DB
  #  code goes here (note: connection codes for SQLite and Ms-Access are different)
  import pyodbc #requires pyodbc package
db_file_path = "Z:\Assignment1-BIS371.accdb"
connect_string = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + db_file_path
try:
  #Make the connection using the connect_string
  connection = pyodbc.connect(connect_string)
  print("connected...")
except Exception as err:
  print("Error connecting...\n", err)
  exit(1) #Since we are not connected, we exit with non-zero exit status

#Close the connection
connection.close()
  #Read SQL script into a single string
  #  code goes here

  #Split the string into a list of SQL commands
  #  code goes here
  
  #Write each SQL statement to the listbox, but in such a way that they look the 
  #  same as in the script itself; i.e., broken out over multiple lines.
  #
  #  Send each SQL statement to the database for execution.
  #  Note: 
  #   Each SQL statement must print to the textbox BEFORE it is sent to the database.
  #   Each statement must be processed completely (printed and sent to the database),
  #     before the next statement is processed.
  #  code goes here (same code for both SQLite and Ms-Access)

  #Close the cursor
  #  code goes here (same code for both SQLite and Ms-Access)
cursor.close()
  #Commit the transactions
  #  code goes here (same code for both SQLite and Ms-Access)

  #Close the database connection
  #  code goes here (same code for both SQLite and Ms-Access)
connection.close()
################################# main #########################################

#Create the root window
window = tk.Tk()
window.title("SQL interpreter for Ms-Access and SQLite")

#Four frames:
header_frame = tk.Frame(master = window)
sql_script_frame = tk.Frame(master = window)
db_frame = tk.Frame(master = window)
sql_display_frame = tk.Frame(master = window)
run_close_frame = tk.Frame(master = window)

header_frame.pack(side = tk.TOP, fill = tk.BOTH)
sql_script_frame.pack(side = tk.TOP, fill = tk.BOTH)
db_frame.pack(side = tk.TOP, fill = tk.BOTH)
sql_display_frame.pack(side = tk.TOP, fill = tk.BOTH)
run_close_frame.pack(side = tk.TOP)

#Text to fill the header
label_text = "!!Note!!\n" \
"When you specify a *.accdb database file, the app assumes Ms-Access.\n" + \
"  (assumes 32-bit Python(3), 32-bit Ms-Access, pyodbc, Ms-Access driver)\n" + \
"For all other file extensions the app assumes SQLite(3)."

header_label = tk.Label(master = header_frame, text = label_text, justify = tk.LEFT)
header_label.pack(side = tk.LEFT)

#Two buttons for picking the files
sql_script_button = tk.Button(master = sql_script_frame, text = "SQL script file", command = get_script_file)
db_button = tk.Button(master = db_frame, text = "Database file", command = get_db_file)

#Two text boxes for the file paths
sql_script_textbox = tk.Entry(master = sql_script_frame, width = 100)
db_textbox = tk.Entry(master = db_frame, width = 100)

sql_script_button.pack(side = tk.LEFT)
db_button.pack(side = tk.LEFT)
sql_script_textbox.pack(side = tk.LEFT)
db_textbox.pack(side = tk.LEFT)

#Listbox for displaying things
sql_display_listbox = tk.Listbox(master = sql_display_frame, width = 113, height = 25)
sql_display_listbox.pack(side = tk.LEFT, fill = tk.Y)

#Scrollbar for the listbox
scrollbar = tk.Scrollbar(master = sql_display_frame)
scrollbar.pack(side = tk.LEFT, fill = tk.Y)

#Associate the scrollbar with the listbox
sql_display_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = sql_display_listbox.yview) 

#Two buttons, each with its own event_handler
run_button = tk.Button(text = "Run", master = run_close_frame, command = run_it)
close_button = tk.Button(text = "Close", master = run_close_frame, command = close_it)

run_button.pack(side = tk.LEFT)
close_button.pack(side = tk.LEFT)

window.mainloop()

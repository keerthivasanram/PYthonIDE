from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import subprocess

root = Tk()
root.title("Python IDLE")
root.geometry("1280x720+150+80")
root.configure(bg="#1E1E1E")
root.resizable(False, False)
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path
    status_bar.config(text=f"Current File: {file_path}")

def open_file():
    path = askopenfilename(filetypes=[('Python File', '*.py')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            code_input.delete('1.0', END)
            code_input.insert('1.0', code)
            set_file_path(path)

def save():
    global file_path
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python File', '*.py')])
        if path:
            with open(path, 'w') as file:
                code = code_input.get('1.0', END)
                file.write(code)
                set_file_path(path)
    else:
        with open(file_path, 'w') as file:
            code = code_input.get('1.0', END)
            file.write(code)

def run():
    if file_path == '':
        messagebox.showerror("Python IDLE", "Save your code first")
        return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.config(state=NORMAL)
    code_output.delete('1.0', END)
    code_output.insert('end', error.decode('utf-8'))
    code_output.insert('end', output.decode('utf-8'))
    code_output.config(state=DISABLED)

def debug():
    # Implement debug functionality here
    messagebox.showinfo("Debug", "Debug feature is not implemented yet.")

# Menubar
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

run_menu = Menu(menubar, tearoff=0)
run_menu.add_command(label="Run", command=run)
run_menu.add_command(label="Debug", command=debug)
menubar.add_cascade(label="Run", menu=run_menu)

root.config(menu=menubar)

# Layout for Code and Output
main_frame = Frame(root, bg="#1E1E1E")
main_frame.pack(fill=BOTH, expand=True)

# Code Input Area (60%)
code_input = ScrolledText(main_frame, font="Consolas 18", undo=True, wrap=None, bg="#1E1E1E", fg="white", insertbackground="white")
code_input.grid(row=0, column=0, sticky=NSEW)

# Output Area (40%)
code_output = Text(main_frame, font="Consolas 15", bg="#1E1E1E", fg="lightgreen", state=DISABLED, insertbackground="white")
code_output.grid(row=0, column=1, sticky=NSEW)

# Configure Grid Weights
main_frame.grid_columnconfigure(0, weight=6)  # 60%
main_frame.grid_columnconfigure(1, weight=4)  # 40%
main_frame.grid_rowconfigure(0, weight=1)

# Status Bar
status_bar = Label(root, text="Welcome to Python IDLE", bg="#323846", fg="white", anchor='w')
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()

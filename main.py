import tkinter as tk
import pandas as pd
from tkinter import filedialog
import dataframe_functions

BO_df = pd.DataFrame()
EWM_df = pd.DataFrame()
OHB_df = pd.DataFrame()

root = tk.Tk()
root.geometry("800x200")
texbox_width = 75

# Create frame
my_frame = tk.Frame(root)

def file_open_BO(pathbox):
   global BO_df
   filename = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Backorder Report")
   if filename:
        try:
            filename = r"{}".format(filename)
            BO_df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File Couldn't Be Opened...try again!")
        except FileNotFoundError:
            my_label.config(text="File Couldn't Be Found...try again!")
        print(BO_df.head())
        pathbox.config(state='normal')
        pathbox.insert(1.0, filename)
        pathbox.config(state='disabled')

def file_open_EWM(pathbox):
   global EWM_df
   filename = filedialog.askopenfilename(initialdir="C:/gui/", title="Open EWM report")
   if filename:
        try:
            filename = r"{}".format(filename)
            EWM_df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File Couldn't Be Opened...try again!")
        except FileNotFoundError:
            my_label.config(text="File Couldn't Be Found...try again!")
        print(EWM_df.head())
        pathbox.config(state='normal')
        pathbox.insert(1.0, filename)
        pathbox.config(state='disabled')

def file_open_OHB(pathbox):
   global OHB_df
   filename = filedialog.askopenfilename(initialdir="C:/gui/", title="Open OHB (MB52)")
   if filename:
        try:
            filename = r"{}".format(filename)
            OHB_df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File Couldn't Be Opened...try again!")
        except FileNotFoundError:
            my_label.config(text="File Couldn't Be Found...try again!")
        print(OHB_df.head())
        pathbox.config(state='normal')
        pathbox.insert(1.0, filename)
        pathbox.config(state='disabled')

# Add a menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Add menu dropdown
#S

bo_button = tk.Button(root, text="BACKORDER REPORT",  command=lambda:file_open_BO(bo_path_box))
bo_path_box = tk.Text(root, height=1, width=texbox_width, state='disabled')

ewm_button = tk.Button(root, text="EWM REPORT",  command=lambda:file_open_EWM(ewm_path_box))
ewm_path_box = tk.Text(root, height=1, width=texbox_width, state='disabled')

ohb_button = tk.Button(root, text="OHB REPORT",  command=lambda:file_open_OHB(ohb_path_box))
ohb_path_box = tk.Text(root, height=1, width=texbox_width, state='disabled')

go_button = tk.Button(root, text="GO!!", command=lambda:process_initiator())
go_path_box = tk.Text(root, height=1, width=texbox_width, state='disabled')

my_label = tk.Label(root, text='')
my_label.grid(row=5, column=0)

bo_button.grid(row=0, column=0)
bo_path_box.grid(row=0, column=1)
ewm_button.grid(row=1, column=0)
ewm_path_box.grid(row=1, column=1)
ohb_button.grid(row=2, column=0)
ohb_path_box.grid(row=2, column=1)

go_button.grid(row=5, column=0)
go_path_box.grid(row=5, column=1)

def process_initiator():
    global BO_df, EWM_df, OHB_df
    dataframe_functions.process_files(BO_df,EWM_df,OHB_df)

root.mainloop()
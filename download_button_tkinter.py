import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def main():
    root = tk.Tk()
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Image Button Demo')

    # exit button
    def download_clicked():
        showinfo(title='Information', message='Download button clicked!')

    download_button = ttk.Button(
        text='Download',
        command=download_clicked
    )
    download_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop()


if __name__ == '__main__':
    main()

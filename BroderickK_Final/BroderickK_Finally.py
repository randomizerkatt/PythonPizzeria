from tkinter import *
import tkinter.font as tkFont
import BackRoomView

if __name__ == '__main__':
    root = Tk()
    root.geometry("1100x800")
    back_room = BackRoomView.create_frame(root)
    back_room.pack(fill='both', expand=True)

    root.mainloop()
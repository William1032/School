from tkinter import *
import random


class Converter():
    """
    #convert temperatures c to f or f to c
    """

    def __init__(self):
        
        """
        temperature conversion gui
        """
        #window
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        #heading
        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        #instructions
        instructions = ("Please enter a temperature below and press one of the buttons to convert it between Celcius and Fahrenheit")
        self.temp_instructions = Label(self.temp_frame, text=instructions, wraplength=250, width=40, justify="left")
        self.temp_instructions.grid(row=1)

        #entry field
        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        #errors
        error = "Please enter a valid number"
        self.temp_error = Label(self.temp_frame, text=error, fg="#9C0000")
        self.temp_error.grid(row=3)

        #conversion, help, and history
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        #button list (text/bg color/command/row/column)
        button_details_list = [
            ["To Celsius", "#990099", "", 0, 0],
            ["To Fahrenheit", "#009900", "", 0, 1],
            ["Info / Help", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        #hold the buttons
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], fg="#FFFFFF", font=("Arial", "12", "bold"),
                                       width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
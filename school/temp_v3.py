from tkinter import *
import all_constants as c
import conv_round as cr


class Converter():
    """
    #convert temperatures c to f or f to c
    """

    def __init__(self):
        

        #calc list
        self.all_calculations_list = []
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
        self.answer_error = Label(self.temp_frame, text=error, fg="#9C0000", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        #conversion, help, and history
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        #button list (text/bg color/command/row/column)
        button_details_list = [
            ["To Celsius", "#990099", lambda:self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#009900", lambda:self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Info / Help", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", lambda:self.history(self.all_calculations_list), 1, 1]
        ]

        #hold the buttons
        self.button_ref_list = []

        #create buttons
        for item in button_details_list:
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], fg="#FFFFFF", font=("Arial", "12", "bold"),
                                       width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    
        
    def check_temp(self,min_temp):

        #get input
        to_convert = self.temp_entry.get()

        #reset label and entry box in case of error
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number greater than/equal to {min_temp}"

        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                self.convert(min_temp, to_convert)
            else:
                self.answer_error.config(text=error, fg="#9C0000", font=("Arial", "13", "bold"))
        except ValueError:
            self.answer_error.config(text="Temperature Invalid", fg="#9C0000", font=("Arial", "14", "bold"))
        

        #convert
    def convert(self, min_temp, to_convert):
        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert} °C is {answer} °F"
        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert} °F is {answer} °C"

        self.to_history_button.config(state=NORMAL)
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer)
    
    def history(self, list):
        history_statement = str(list).strip("[]").replace("'", "")
        self.answer_error.config(text=history_statement, wraplength=250)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
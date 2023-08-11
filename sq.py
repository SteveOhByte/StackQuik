import tkinter as tk
from tkinter import ttk
import argparse
import platform

class StackQuikApp(tk.Tk):
    def __init__(self, initial_value=None):
        super().__init__()
        self.title("StackQuik")
        self.geometry("300x150")

        # Centering the window on the screen
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry("+{}+{}".format(position_right, position_down))

        # Setting the icon
        system_name = platform.system()
        if system_name == "Windows":
            try:
                self.iconbitmap("icon.ico")
            except:
                print("Windows icon file not found!")
        elif system_name == "Darwin":  # macOS
            try:
                self.iconbitmap("icon.icns")
            except:
                print("macOS icon file not found!")
        elif system_name == "Linux":
            try:
                self.iconbitmap("icon.png")
            except:
                print("Linux icon file not found!")

        # Updated widget definitions to use ttk
        self.label_prompt = ttk.Label(self, text="Enter number of blocks:")
        self.label_prompt.pack(pady=5)

        self.entry_blocks = ttk.Entry(self)
        self.entry_blocks.pack(pady=5)

        self.button_calculate = ttk.Button(
            self, text="Calculate", command=self.calculate_and_display
        )
        self.button_calculate.pack(pady=5)

        self.label_result = ttk.Label(self, text="")
        self.label_result.pack(pady=5)

        if initial_value is not None:
            self.entry_blocks.insert(0, str(initial_value))
            self.calculate_and_display()

    def calculate_blocks(self, num_blocks):
        stack_size = 64
        full_stacks = num_blocks // stack_size
        remainder = num_blocks % stack_size
        return full_stacks, remainder

    def calculate_and_display(self):
        try:
            num_blocks = int(self.entry_blocks.get())
            full_stacks, remainder = self.calculate_blocks(num_blocks)
            self.label_result.config(
                text=f"{full_stacks} full stacks with {remainder} leftover."
            )
        except ValueError:
            self.label_result.config(text="Invalid input!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Minecraft stacks.")

    # Define a positional argument instead of a flag
    parser.add_argument(
        "number", type=str, nargs="?", default=None, help="Number of blocks."
    )

    args = parser.parse_args()

    # Strip the hyphen from the number and convert to int
    number = (
        int(args.number[1:]) if args.number and args.number.startswith("-") else None
    )

    app = StackQuikApp(number)
    app.mainloop()

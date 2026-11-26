import tkinter as tk

from core.calculator import calculate


BACKGROUND = "#1c1c1c"
DISPLAY_BACKGROUND = "#1c1c1c"
NUMBER_BACKGROUND = "#505050"
UTILITY_BACKGROUND = "#a5a5a5"
OPERATOR_BACKGROUND = "#ff9f0a"


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA Calculator")
        self.root.configure(bg=BACKGROUND)
        self.root.resizable(False, False)

        self.expression = tk.StringVar()
        self.result = tk.StringVar(value="0")
        self.postfix = tk.StringVar()

        self._create_display()
        self._create_buttons()
        self.root.bind("<Key>", self._handle_key)

    def _create_display(self):
        display = tk.Frame(self.root, bg=DISPLAY_BACKGROUND, padx=16, pady=14)
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        tk.Label(
            display,
            textvariable=self.expression,
            anchor="e",
            bg=DISPLAY_BACKGROUND,
            fg="#bdbdbd",
            font=("Segoe UI", 18),
            width=22,
        ).pack(fill="x")
        self.result_display = tk.Label(
            display,
            textvariable=self.result,
            anchor="e",
            bg=DISPLAY_BACKGROUND,
            fg="white",
            font=("Segoe UI", 34),
            width=14,
        )
        self.result_display.pack(fill="x", pady=(4, 8))
        tk.Label(
            display,
            textvariable=self.postfix,
            anchor="e",
            bg=DISPLAY_BACKGROUND,
            fg="#9b9b9b",
            font=("Segoe UI", 10),
            width=34,
        ).pack(fill="x")

    def _create_buttons(self):
        buttons = [
            [("C", "clear"), ("⌫", "backspace"), ("(", "("), (")", ")")],
            [("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/")],
            [("4", "4"), ("5", "5"), ("6", "6"), ("×", "*")],
            [("1", "1"), ("2", "2"), ("3", "3"), ("−", "-")],
            [(".", "."), ("0", "0"), ("=", "equals"), ("+", "+")],
        ]

        for row_index, row in enumerate(buttons, start=1):
            for column_index, (label, action) in enumerate(row):
                if action in ("clear", "backspace"):
                    color = UTILITY_BACKGROUND
                    text_color = "#1c1c1c"
                elif action in ("+", "-", "*", "/", "equals"):
                    color = OPERATOR_BACKGROUND
                    text_color = "white"
                else:
                    color = NUMBER_BACKGROUND
                    text_color = "white"

                button = tk.Button(
                    self.root,
                    text=label,
                    command=lambda value=action: self._press(value),
                    bg=color,
                    fg=text_color,
                    activebackground=color,
                    activeforeground=text_color,
                    font=("Segoe UI", 19),
                    relief="flat",
                    width=5,
                    height=2,
                    takefocus=False,
                )
                button.grid(
                    row=row_index,
                    column=column_index,
                    padx=4,
                    pady=4,
                    sticky="nsew",
                )

    def _press(self, action):
        if action != "equals":
            self.result_display.configure(font=("Segoe UI", 34))

        if action == "clear":
            self.expression.set("")
            self.result.set("0")
            self.postfix.set("")
        elif action == "backspace":
            self.expression.set(self.expression.get()[:-1])
            self.result.set("")
            self.postfix.set("")
        elif action == "equals":
            self._calculate()
        else:
            self.expression.set(self.expression.get() + action)
            self.result.set("")
            self.postfix.set("")

    def _calculate(self):
        try:
            result, postfix = calculate(
                self.expression.get(),
                show_postfix=True,
            )
        except ValueError as error:
            self.result_display.configure(font=("Segoe UI", 12))
            self.result.set(f"Error: {error}")
            self.postfix.set("")
            return

        self.result_display.configure(font=("Segoe UI", 34))
        self.result.set(f"{result:.10g}")
        self.postfix.set("Postfix: " + " ".join(str(token) for token in postfix))

    def _handle_key(self, event):
        if event.keysym in ("Return", "KP_Enter"):
            self._press("equals")
        elif event.keysym == "BackSpace":
            self._press("backspace")
        elif event.keysym == "Escape":
            self._press("clear")
        elif event.char and event.char in "0123456789.+-*/()":
            self._press(event.char)
        else:
            return

        return "break"


def run():
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()

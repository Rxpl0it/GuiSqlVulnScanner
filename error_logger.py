class ErrorLogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def log(self, message):
        # Append the message to the text widget
        self.text_widget.insert('end', message + '\n')
        # Automatically scroll to the end of the text widget
        self.text_widget.see('end')

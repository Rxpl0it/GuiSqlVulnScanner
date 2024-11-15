import tkinter as tk
from tkinter import ttk, scrolledtext
from scanner import start_scan
from graph import Graph
from counter import Counter
from error_logger import ErrorLogger

class SQLVulnScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Vulnerability Scanner")

        # URL Input
        self.url_label = ttk.Label(root, text="Enter URLs (one per line):")
        self.url_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")

        self.url_input = scrolledtext.ScrolledText(root, width=50, height=10)
        self.url_input.grid(row=1, column=0, padx=10, pady=5)

        # Start Button
        self.start_button = ttk.Button(root, text="Start Scan", command=self.start_scan)
        self.start_button.grid(row=2, column=0, padx=10, pady=5)

        # Live Counter
        self.counter_label = ttk.Label(root, text="Vulnerabilities Found:")
        self.counter_label.grid(row=3, column=0, padx=10, pady=5, sticky="W")

        self.counter_value = ttk.Label(root, text="0")
        self.counter_value.grid(row=3, column=0, padx=150, pady=5, sticky="W")

        # Graph Area
        self.graph_frame = ttk.Frame(root, width=400, height=200)
        self.graph_frame.grid(row=4, column=0, padx=10, pady=5)
        self.graph = Graph(self.graph_frame)

        # Error Log
        self.error_log_label = ttk.Label(root, text="MySQL Error Log:")
        self.error_log_label.grid(row=5, column=0, padx=10, pady=5, sticky="W")

        self.error_log = scrolledtext.ScrolledText(root, width=50, height=10)
        self.error_log.grid(row=6, column=0, padx=10, pady=5)

        # Initialize Counter and Error Logger
        self.counter = Counter(self.counter_value)
        self.error_logger = ErrorLogger(self.error_log)

    def start_scan(self):
        urls = self.url_input.get("1.0", tk.END).strip().split("\n")
        start_scan(urls, self.counter, self.graph, self.error_logger)

if __name__ == "__main__":
    root = tk.Tk()
    app = SQLVulnScannerGUI(root)
    root.mainloop()

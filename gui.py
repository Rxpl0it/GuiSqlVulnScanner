import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.font import Font
from scanner import start_scan
from graph import Graph
from counter import Counter
from error_logger import ErrorLogger

class SQLVulnScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Vulnerability Scanner")

        # Set font and style
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 10))
        self.style.configure('TButton', font=('Helvetica', 10))
        
        # Sidebar
        self.sidebar = ttk.Frame(root, width=200, height=400, relief='sunken')
        self.sidebar.grid(row=0, column=0, rowspan=7, sticky="NS")
        
        self.url_label = ttk.Label(self.sidebar, text="Enter URLs:")
        self.url_label.pack(padx=10, pady=5, anchor="w")

        self.url_input = scrolledtext.ScrolledText(self.sidebar, width=25, height=10)
        self.url_input.pack(padx=10, pady=5)

        self.start_button = ttk.Button(self.sidebar, text="Start Scan", command=self.start_scan)
        self.start_button.pack(padx=10, pady=5)

        # Main Panel
        self.main_panel = ttk.Frame(root, width=600, height=400)
        self.main_panel.grid(row=0, column=1, rowspan=6, sticky="NSEW")

        self.counter_label = ttk.Label(self.main_panel, text="Vulnerabilities Found:")
        self.counter_label.pack(padx=10, pady=5, anchor="w")

        self.counter_value = ttk.Label(self.main_panel, text="0")
        self.counter_value.pack(padx=10, pady=5, anchor="w")

        self.graph_frame = ttk.Frame(self.main_panel, width=400, height=200)
        self.graph_frame.pack(padx=10, pady=5)
        self.graph = Graph(self.graph_frame)

        self.error_log_label = ttk.Label(self.main_panel, text="MySQL Error Log:")
        self.error_log_label.pack(padx=10, pady=5, anchor="w")

        self.error_log = scrolledtext.ScrolledText(self.main_panel, width=70, height=10)
        self.error_log.pack(padx=10, pady=5)

        # Status Bar
        self.status_bar = ttk.Label(root, text="Ready", relief='sunken', anchor='w')
        self.status_bar.grid(row=7, column=0, columnspan=2, sticky="EW")

        # Initialize Counter and Error Logger
        self.counter = Counter(self.counter_value)
        self.error_logger = ErrorLogger(self.error_log)

    def start_scan(self):
        urls = self.url_input.get("1.0", tk.END).strip().split("\n")
        self.status_bar.config(text="Scanning...")
        start_scan(urls, self.counter, self.graph, self.error_logger)
        self.status_bar.config(text="Scan Complete")

if __name__ == "__main__":
    root = tk.Tk()
    app = SQLVulnScannerGUI(root)
    root.mainloop()

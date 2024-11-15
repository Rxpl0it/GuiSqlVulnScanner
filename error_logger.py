import logging
from logging.handlers import QueueHandler, QueueListener
import queue

class ErrorLogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.log_queue = queue.Queue()
        self.logger = logging.getLogger('ErrorLogger')
        self.logger.setLevel(logging.DEBUG)
        
        # Create a handler that writes log messages to the queue
        queue_handler = QueueHandler(self.log_queue)
        self.logger.addHandler(queue_handler)
        
        # Create a listener that processes log messages from the queue
        listener = QueueListener(self.log_queue, self._log_to_widget)
        listener.start()

        # Set the format for log messages
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        queue_handler.setFormatter(formatter)

    def _log_to_widget(self, record):
        message = self.logger.handlers[0].format(record)
        self.text_widget.insert('end', message + '\n')
        self.text_widget.see('end')

    def log(self, message):
        self.logger.error(message)

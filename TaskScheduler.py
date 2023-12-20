from datetime import datetime, timedelta
from time import sleep
from typing import Any, Callable, List

DATE_FORMAT = "%m/%d/%Y %I:%M:%S %p"

class Task:
    def __init__(self, target, *args) -> None:
        self.target = target
        self.args = args

    @staticmethod
    def parse_time(date) -> datetime:
        if isinstance(date, str):
            return datetime.strptime(date, DATE_FORMAT)
        elif isinstance(date, datetime):
            return date
        else:
            raise ValueError("Invalid date format")

    def run(self):
        self.target(*self.args)
    
    def daily(self, start_date: str | datetime, recur_every: int = 1):
        """
        Run a daily task starting from a specified date.

        Args:
            start_date (str | datetime): The starting date for the daily task.
                It can be a string in a recognizable format or a datetime object.
            recur_every (int): Number of days between each iteration. Default is 1.
        """
        while True:
            now = datetime.now()

            # Convert start_date to datetime object if it's a string
            start_date = self.parse_time(start_date)

            if now > start_date:
                # Execute the daily task
                self.run()

                # Calculate the next date to run the task
                next_date = now + timedelta(days=recur_every)
                next_date_in_sec = next_date.timestamp()

                # Sleep until the next iteration
                sleep(next_date_in_sec)
            else:
                # Calculate the time duration until the start_date
                sleep_duration = (start_date - now).total_seconds()
                # Sleep for that duration
                sleep(sleep_duration)



class TaskScheduler:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def create(self, target: Callable, *args: Any) -> Task:
        """
        Create a new task and add it to the scheduler.

        Args:
            target (Callable): The function or method to be executed by the task.
            *args (Any): Arguments to be passed to the target function.

        Returns:
            Task: The created task.
        """
        task = Task(target, *args)
        self.tasks.append(task)
        return task

    def run_all_tasks(self) -> None:
        """
        Run all tasks in the scheduler.
        """
        for task in self.tasks:
            task.run()
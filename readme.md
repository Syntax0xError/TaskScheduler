# Task Scheduler

A simple Python task scheduler that supports daily tasks with additional performance benefits due to the use of thread sleeping.

## Usage

### Task Class

#### `Task(target, *args)`

- `target`: The function or method to be executed by the task.
- `*args`: Arguments to be passed to the target function.

#### `parse_time(date) -> datetime`

Parses the input date and returns a datetime object.

#### `run()`

Executes the task by calling the target function with the provided arguments.

#### `daily(start_date: str | datetime, recur_every: int = 1)`

Run a daily task starting from a specified date.

- `start_date` (str | datetime): The starting date for the daily task. It can be a string in a recognizable format or a datetime object.
- `recur_every` (int): Number of days between each iteration. Default is 1.

### TaskScheduler Class

#### `TaskScheduler()`

Initializes a task scheduler.

#### `create(target: Callable, *args: Any) -> Task`

Creates a new task and adds it to the scheduler.

- `target` (Callable): The function or method to be executed by the task.
- `*args` (Any): Arguments to be passed to the target function.

#### `run_all_tasks()`

Runs all tasks in the scheduler.

## Example

```python
from taskscheduler import TaskScheduler

def daily_task():
    print("This task runs daily!")

# Create a task scheduler
scheduler = TaskScheduler()
scheduler.create(daily_task)

# Schedule a daily task (automatically triggered, no manual execution needed)
daily_task = scheduler.daily(daily_task, recur_every=1)

## Notes

- Currently, only daily tasks are supported.
- The implementation utilizes thread sleeping for improved performance during task scheduling.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.
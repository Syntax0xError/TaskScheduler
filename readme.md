# Task Scheduler

A simple Python task scheduler for running tasks at specified intervals.

## Introduction

The Task Scheduler is a Python module that allows you to schedule and run tasks at specific intervals. It currently supports a `daily` method for running tasks every day.

## Features

- Schedule and run tasks at daily intervals.
- Easy-to-use API for creating and managing tasks.

## Installation

No installation is required. Simply include the `taskscheduler.py` module in your project.

## Usage

1. Import the `TaskScheduler` class:

    ```python
    from taskscheduler import TaskScheduler
    ```

2. Create an instance of `TaskScheduler`:

    ```python
    scheduler = TaskScheduler()
    ```

3. Create a task using the `create` method. Currently, only the `daily` method is supported:

    ```python
    task = scheduler.daily(target_function, *args, recur_every=1)
    ```

    - `target_function`: The function to be executed daily.
    - `*args`: Arguments to be passed to the target function.
    - `recur_every`: Number of days between each iteration (default is 1).

4. Run all scheduled tasks:

    ```python
    scheduler.run_all_tasks()
    ```

## Example

```python
from taskscheduler import TaskScheduler

def daily_task():
    print("This task runs daily!")

# Create a task scheduler
scheduler = TaskScheduler()

# Schedule a daily task
daily_task = scheduler.daily(daily_task, recur_every=1)

# Run all scheduled tasks
scheduler.run_all_tasks()

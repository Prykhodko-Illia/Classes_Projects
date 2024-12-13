
class Project:
    def __init__(self, project_name, project_description):
        self.project_name = project_name
        self.project_description = project_description
        self.tasks = {}

    def add_task(self, title, description, status):
        if title not in self.tasks:
            self.tasks[title] = {"description": description, "status": status}
        else: print(f"There is already a task with title: {title}\n")

    def remove_task(self, title):
        try: del self.tasks[title]
        except KeyError: print(f"There are no task with title: {title}\n")

    def get_task_status(self, title):
        try: return self.tasks[title]["status"]
        except KeyError: print(f"There is no task with title: {title}\n")

    def update_task_status(self, title, new_status):
        try: self.tasks[title]["status"] = new_status
        except KeyError: print(f"There is no task with title: {title}\n")

    def get_tasks_by_status(self, status):
        status_tasks = [x[0] for x in self.tasks.items() if x[1]["status"] == status]
        if status_tasks: return f"Tasks with status - {status}:\n" + ", ".join(status_tasks) + "\n"
        return f"There are no tasks with the status - {status}\n"

    def print_tasks(self):
        print("All tasks:")
        print(", ".join(self.tasks.keys()) + "\n")

project = Project("Website Redesign", "A project for redesigning the company website")
project.add_task("Design Layout", "Create a layout for the new website", "Planned")
project.add_task("Develop Homepage", "Develop the homepage of the website", "In Progress")
project.add_task("Develop Homepage", "Develop the homepage of the website", "In Progress")
project.update_task_status("Design Layout", "Completed")
project.print_tasks()

planned_tasks = project.get_tasks_by_status("Planned")
print(planned_tasks)

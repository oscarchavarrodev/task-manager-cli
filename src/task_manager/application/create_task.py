from task_manager.domain.task import Task


class CreateTaskUseCase:
    def execute(self, title: str, description: str) -> Task:
        return Task.create(title=title, description=description)

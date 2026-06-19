from task_manager.domain.task import Task


class CompleteTaskUseCase:
    def execute(self, task: Task) -> Task:
        task.complete()
        return task

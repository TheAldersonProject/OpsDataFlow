from opsdataflow.track_flow.tracker import Tracker

tracker = Tracker()
tracker.process(
    name="I am a process. My name is ProcessMe.",
    description="My description",
    parent_uuid="123"
)
tracker.__event("I am an event.")
tracker.task()
tracker.__event("I am an event of a task type.")
tracker.step(
    name="I am a step. My name is StepMe.",
    description="My description",
    step_parent_uuid="123")
tracker.__event("I am an event of a task type.")
tracker.end_step()
tracker.__event("Back to task")
tracker.process()
tracker.step()
tracker.__event("I am a new kid step")
tracker.end_task()
tracker.__event("I should be a process event.")

# tracker.process(
#     process_name="I am another process. My name is ProcessMe Again.",
#     process_description="My description is different.",
#     process_parent_uuid=None
# )
# tracker.event("I am a new event.")
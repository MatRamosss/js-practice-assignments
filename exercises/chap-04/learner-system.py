class Learner:
    def __init__(self, learner_id, name, age, marks=None):
        self.learner_id = learner_id
        self.name = name
        self.age = age
        self.marks = marks if marks is not None else []
 
    def __str__(self):
        return f"ID: {self.learner_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}"


class LearnerSystem:
    def __init__(self):
        self.learners = {}

    def add_learner(self, learner):
        self.learners[learner.learner_id] = learner

    def view_learner(self, learner_id):
        return str(self.learners.get(learner_id, "Learner not found."))

    def update_learner(self, learner_id, name=None, age=None, marks=None):
        learner = self.learners.get(learner_id)
        if learner:
            if name:
                learner.name = name
            if age:
                learner.age = age
            if marks is not None:
                learner.marks = marks
            return "Learner updated successfully."
        return "Learner not found."

    def remove_learner(self, learner_id):
        if learner_id in self.learners:
            del self.learners[learner_id]
            return "Learner removed successfully."
        return "Learner not found."




class Person: 
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

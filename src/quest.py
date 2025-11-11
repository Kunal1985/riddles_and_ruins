class Quest:
    def __init__(self, name, objectives):
        self.name = name
        self.objectives = objectives
        self.completed_objectives = []
    
    def check_progress(self):
        return len(self.completed_objectives), len(self.objectives) + len(self.completed_objectives)    

    def complete_objective(self, objective):
        if objective in self.objectives and objective not in self.completed_objectives:
            self.completed_objectives.append(objective)
            self.objectives.remove(objective)
            print(f"Objective '{objective}' completed!")
        else:
            print(f"Objective '{objective}' is either not valid or already completed.")

    def is_completed(self):
        return not len(self.objectives)

    def display_quest_info(self):
        print(f"Quest: {self.name}")
        print("Objectives Completed:")
        for objective in self.completed_objectives:
            print(objective)
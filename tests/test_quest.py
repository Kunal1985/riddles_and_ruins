import pytest
from src.quest import Quest

def test_quest_initialization():
    """Test quest creation and initial state"""
    objectives = ["Riddle", "Combat-1"]
    quest = Quest("Test Quest", objectives)
    
    assert quest.name == "Test Quest"
    assert quest.objectives == objectives
    assert len(quest.completed_objectives) == 0

def test_quest_completion():
    """Test completing quest objectives"""
    quest = Quest("Test Quest", ["Riddle", "Combat-1"])
    
    # Complete first objective
    quest.complete_objective("Riddle")
    assert "Riddle" in quest.completed_objectives
    assert len(quest.completed_objectives) == 1
    
    # Complete second objective
    quest.complete_objective("Combat-1")
    assert "Combat-1" in quest.completed_objectives
    assert quest.is_completed()

def test_quest_progress_tracking():
    """Test quest progress tracking"""
    quest = Quest("Test Quest", ["Riddle", "Combat-1", "Combat-2"])
    
    # Check initial progress
    completed, total = quest.check_progress()
    assert completed == 0
    assert total == 3
    
    # Complete some objectives and check progress
    quest.complete_objective("Riddle")
    quest.complete_objective("Combat-1")
    completed, total = quest.check_progress()
    assert completed == 2
    assert total == 3

def test_duplicate_completion():
    """Test attempting to complete same objective multiple times"""
    quest = Quest("Test Quest", ["Riddle"])
    
    # Complete objective once
    quest.complete_objective("Riddle")
    initial_completion_count = len(quest.completed_objectives)
    
    # Try to complete same objective again
    quest.complete_objective("Riddle")
    assert len(quest.completed_objectives) == initial_completion_count

def test_invalid_objective():
    """Test attempting to complete invalid objective"""
    quest = Quest("Test Quest", ["Riddle"])
    
    # Try to complete non-existent objective
    quest.complete_objective("Invalid")
    assert len(quest.completed_objectives) == 0
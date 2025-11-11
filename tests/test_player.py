import pytest
from src.player import Player
from src.items.inventory import Inventory

def test_player_initialization():
    """Test player initialization with default values"""
    player = Player(name="TestPlayer")
    assert player.name == "TestPlayer"
    assert player.health == 100  # assuming default health is 100
    assert player.current_dungeon == None
    # Check if it's an Inventory instance by checking class name and module path
    assert player.inventory.__class__.__name__ == "Inventory"
    assert "inventory" in player.inventory.__class__.__module__

def test_player_health_management():
    """Test player health modification methods"""
    player = Player(name="TestPlayer")
    initial_health = player.health
    
    # Test damage
    player.take_damage(20)
    assert player.health == initial_health - 20
    
    # Test healing
    player.heal(10)
    assert player.health == initial_health - 10

def test_player_dungeon_progress():
    """Test player dungeon progression"""
    player = Player(name="TestPlayer")
    assert player.current_dungeon == None
    
    player.current_dungeon = 0
    player.stage_complete()
    assert player.current_dungeon == 0
    assert 0 in player.dungeons_completed
    assert 1 in player.next_dungeons  # assuming next dungeon is 1 after completing dungeon 0
    
    # Test multiple stage completions
    player.current_dungeon = 1
    player.stage_complete()
    assert player.current_dungeon == 1
    assert 0 in player.dungeons_completed
    assert 1 in player.dungeons_completed
    assert 2 in player.next_dungeons
    assert 3 in player.next_dungeons

def test_player_inventory_management():
    """Test player inventory operations"""
    player = Player(name="TestPlayer")
    
    # Test adding items
    player.inventory.add_item("Health Potion")
    assert "Health Potion" in player.inventory.items
    assert player.inventory.items["Health Potion"] == 1
    
    # Test using items
    player.take_damage(30)
    damaged_health = player.health
    result = player.inventory.exec_use_item("Health Potion")
    assert "Health Potion" in player.inventory.items
    assert player.inventory.items["Health Potion"] == 0
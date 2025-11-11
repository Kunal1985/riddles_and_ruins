import pytest
from src.items.inventory import Inventory

def test_inventory_initialization():
    """Test inventory creation and initial state"""
    inventory = Inventory()
    assert isinstance(inventory.items, dict)
    assert "Health Potion" in inventory.items
    assert "Battle Potion" in inventory.items
    assert inventory.items["Health Potion"] == 0
    assert inventory.items["Battle Potion"] == 0

def test_add_item():
    """Test adding items to inventory"""
    inventory = Inventory()
    
    # Add existing item
    inventory.add_item("Health Potion")
    assert inventory.items["Health Potion"] == 1
    
    # Add multiple of same item
    inventory.add_item("Health Potion")
    assert inventory.items["Health Potion"] == 2
    
    # Add new item type (not in predefined list)
    inventory.add_item("New Item")
    assert "New Item" not in inventory.items

def test_remove_item():
    """Test removing items from inventory"""
    inventory = Inventory()
    
    # Add and remove item
    inventory.add_item("Health Potion")
    assert inventory.items["Health Potion"] == 1
    inventory.remove_item("Health Potion")
    assert inventory.items["Health Potion"] == 0

def test_use_item():
    """Test using items from inventory"""
    inventory = Inventory()
    
    # Add items to use
    inventory.add_item("Health Potion")
    inventory.add_item("Battle Potion")
    
    # Test using health potion
    initial_health_potions = inventory.items["Health Potion"]
    inventory.exec_use_item("Health Potion")
    assert inventory.items["Health Potion"] == initial_health_potions - 1

def test_show_inventory():
    """Test inventory display"""
    inventory = Inventory()
    
    # Add some items
    inventory.add_item("Health Potion")
    inventory.add_item("Battle Potion")
    inventory.add_item("Health Potion")
    
    # Verify inventory contents
    assert inventory.items["Health Potion"] == 2
    assert inventory.items["Battle Potion"] == 1
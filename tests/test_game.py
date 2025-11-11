import pytest
from src.game import Game
from src.player import Player

@pytest.fixture
def game_setup():
    """Setup a game instance with a player for testing"""
    player = Player("TestPlayer")
    game = Game(player)
    return game, player

def test_game_initialization(game_setup):
    """Test game initialization"""
    game, player = game_setup
    assert game.player == player
    assert game.is_running

def test_game_dungeon_progression(game_setup):
    """Test dungeon progression logic"""
    game, player = game_setup
    
    # Assign initial dungeon and complete
    player.current_dungeon = 0
    player.stage_complete()
    print(player.dungeons_completed)
    assert 0 in player.dungeons_completed

def test_game_completion(game_setup):
    """Test game completion conditions"""
    game, player = game_setup
    
    # Complete all dungeons in valid path1
    valid_path = [1, 3, 5, 6]
    for dungeon in valid_path[:-1]:
        player.current_dungeon = dungeon - 1
        player.stage_complete()
    
    # Assert dungeon completions
    assert player.dungeons_completed == [0, 2, 4]
    
    player = Player("TestPlayer")
    game = Game(player)
    
    # Complete all dungeons in valid path2
    valid_path = [1, 2, 4, 6]
    for dungeon in valid_path[:-1]:
        player.current_dungeon = dungeon - 1
        player.stage_complete()
    
    # Assert dungeon completions
    assert player.dungeons_completed == [0, 1, 3]
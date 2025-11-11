# Riddles & Ruins

## Game Overview
"Riddles & Ruins" is an engaging text-based adventure game where players navigate through a series of dungeons, solving riddles and engaging in combat encounters. The game emphasizes strategic decision-making, resource management, and player choice through branching paths.

## Game Mechanics

### Dungeon Paths
Players must choose one of two possible paths to complete the game:
- Path 1: Dungeons [1 → 3 → 5 → 6]
- Path 2: Dungeons [1 → 2 → 4 → 6]

### Quest System
Each dungeon contains specific quests that must be completed to progress. There are two types of quests:

#### 1. Riddle Quests
- Players are presented with a riddle to solve
- Rewards:
  - Correct answer: Receive a Health Potion (+20 HP when used)
  - Skip option: -20 HP penalty
  
#### 2. Combat Quests
Combat is probability-based with three difficulty levels:

**Level 1**
- Win: -5 HP + Battle Potion reward
- Lose: -10 HP
- Skip: -20 HP penalty

**Level 2**
- Win: -10 HP + Battle Potion reward
- Lose: -20 HP
- Skip: -20 HP penalty

**Level 3**
- Win: -15 HP + Battle Potion reward
- Lose: -30 HP
- Skip: -30 HP penalty

### Items
1. Health Potion
   - Restores 20 HP
   - Obtained by solving riddles
   - Can be used at any time

2. Battle Potion
   - Provides complete protection during combat encounters
   - When active, prevents all health point loss
   - Protects against combat outcomes (win/loss) and skip penalties
   - Can be used at any time during the game
   - Effect lasts for one combat encounter

## Technical Implementation

### Project Structure
The game is built using a modular, object-oriented approach with the following key components:

```
adventure-game/
├── src/
│   ├── main.py           # Game entry point
│   ├── game.py           # Core game loop
│   ├── player.py         # Player state management
│   ├── quest.py          # Quest tracking system
│   ├── dungeons/         # Dungeon implementations
│   ├── encounters/       # Combat and puzzle systems
│   ├── items/           # Inventory management
│   └── utils/           # Helper functions
```

### Key Classes
- `Player`: Manages player state, inventory, and progress
- `Game`: Controls game flow and dungeon progression
- `Quest`: Handles quest objectives and completion
- `Dungeon`: Base class for dungeon implementations
- `Inventory`: Manages items and usage

### Development Journey
1. Initial Structure
   - Basic project skeleton created using GitHub Copilot
   - Core files and basic functionality established

2. Enhancements
   - Added modular design patterns
   - Implemented inheritance for dungeons
   - Created comprehensive quest system
   - Added inventory management
   - Implemented branching paths

3. Optimizations
   - Improved path progression logic
   - Enhanced combat system
   - Added robust error handling
   - Implemented save/load functionality

## Strategic Elements

### Player Choices
1. Path Selection
   - Two distinct paths offer different challenges
   - Each path requires unique strategies

2. Combat Decisions
   - Fight: Risk vs. reward mechanics
   - Skip: Guaranteed penalty but avoid uncertainty

3. Resource Management
   - Health points management
   - Strategic use of health potions
   - Balancing risk in combat

## Tips for Players
1. Health Management
   - Keep track of your HP
   - Save health potions for critical moments
   - Consider skip penalties vs. combat risks

2. Path Strategy
   - Plan your route before starting
   - Each path has different difficulty curves
   - Consider your playstyle (combat vs. puzzles)

3. Combat Tips
   - Higher levels have higher risks and rewards
   - Use battle potions wisely
   - Skip if health is critically low

## Development Notes
- Modular design allows easy addition of new dungeons
- Quest system supports multiple objective types
- Combat system uses probability-based outcomes
- Inventory system handles item management
- Save system tracks progress across sessions

## Testing
### Unit Tests
The project includes comprehensive unit tests for all major components:
- Player tests: Health management, inventory operations, dungeon progression
- Game tests: Path validation, dungeon progression, game completion
- Quest tests: Objective tracking, completion validation
- Inventory tests: Item management, usage mechanics

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_game.py

# Run specific test function
python -m pytest tests/test_game.py::test_game_dungeon_progression

# Run with verbose output
python -m pytest -v tests/

# Show print statements during tests
python -m pytest -s tests/
```

### Test Coverage
Tests verify:
- Valid dungeon paths ([1,3,5,6] and [1,2,4,6])
- Health and inventory management
- Quest completion logic
- Game state transitions
- Error handling for invalid progressions

## Future Enhancements
- Additional dungeon paths
- More quest types
- Enhanced combat mechanics
- New items and rewards
- Achievement system
- Character classes
- Difficulty settings
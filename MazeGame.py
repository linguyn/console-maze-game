
'''Developing a text-based maze game using Python. In this game, the player
will navigate through a maze represented in a grid. The maze consists of 
obstacles(#), open paths(), player(P), and a goal(X). The objective for the 
player is to avoid dead ends to reach the goal. The maze will have small 
open paths in order to raise the difficulty of the game. It will also randomly
generated for replayability, ensuring a unique experience for players.'''


import random  # Import the random module for maze generation

# Maze dimensions
WIDTH, HEIGHT = 20, 10  # Define the width and height of the maze grid

# Maze symbols
WALL = "#"  # Represents obstacles
SPACE = " "  # Represents open paths
PLAYER = "P"  # Represents the player's position
GOAL = "X"  # Represents the goal point

def generate_maze(width, height):
    """Generate a maze with random walls and open spaces."""
    maze = [[WALL if random.random() < 0.3 else SPACE for _ in range(width)] for _ in range(height)]
    maze[0][0] = PLAYER  # Starting position for the player
    maze[height - 1][width - 1] = GOAL  # Goal position
    return maze

def print_maze(maze):
    """Display the maze row by row."""
    for row in maze:
        print("".join(row))  # Combine the symbols in each row into a single string

def is_valid_move(maze, x, y):
    """Check if the move is within bounds and not into a wall."""
    return 0 <= x < WIDTH and 0 <= y < HEIGHT and maze[y][x] in [SPACE, GOAL]

def move_player(maze, x, y, direction):
    """Update the player's position based on the input direction."""
    new_x, new_y = x, y  # Initialize new coordinates
    if direction == "w":  # Move up
        new_y -= 1
    elif direction == "s":  # Move down
        new_y += 1
    elif direction == "a":  # Move left
        new_x -= 1
    elif direction == "d":  # Move right
        new_x += 1

    if is_valid_move(maze, new_x, new_y):  # Check if the new position is valid
        maze[y][x] = SPACE  # Clear the previous player position
        maze[new_y][new_x] = PLAYER  # Update to the new player position
        return new_x, new_y, maze[new_y][new_x] == GOAL  # Check if the goal is reached
    print("Invalid move! You hit a wall or went out of bounds.")  # Error message for invalid moves
    return x, y, False  # Return original position if move fails

def count_walls(maze):
    """Count the total number of walls in the maze."""
    return sum(row.count(WALL) for row in maze)

def count_spaces(maze):
    """Count the total number of open paths in the maze."""
    return sum(row.count(SPACE) for row in maze)

def calculate_progress(x, y):
    """Calculate the player's progress toward the goal as a percentage."""
    total_distance = WIDTH + HEIGHT - 2  # Max steps from (0,0) to (WIDTH-1, HEIGHT-1)
    current_distance = x + y  # Player's distance traveled from (0,0)
    return (current_distance / total_distance) * 100

def play_maze_game():
    """Main function to play the maze game."""
    maze = generate_maze(WIDTH, HEIGHT)  # Generate a random maze
    player_x, player_y = 0, 0  # Starting coordinates of the player
    goal_reached = False  # Track if the goal is reached
    steps = 0  # Track the number of steps taken
    user = str(input("Enter your name: "))
    print(f"Welcome to the Maze Game, {user}!")  # Introduction to the game
    print("Navigate the maze using 'W', 'A', 'S', 'D'. Reach 'X' to win!\n")
    print(f"The maze has {count_walls(maze)} walls and {count_spaces(maze)} open paths.")  # Maze stats
    print_maze(maze)  # Display the initial maze

    while not goal_reached:  # Main loop runs until the player reaches the goal
        move = input("\nMove (W/A/S/D): ").lower()  # Get the player's move
        if move in ["w", "a", "s", "d"]:
            player_x, player_y, goal_reached = move_player(maze, player_x, player_y, move)
            steps += 1  # Increment the step count after each valid move
            progress = calculate_progress(player_x, player_y)  # Calculate progress
            print_maze(maze)  # Display the updated maze
            print(f"Progress: {progress:.2f}%")  # Show progress percentage
        else:
            print("Invalid input! Please use W, A, S, or D.")  # Error message for invalid input

    print(f"\nCongratulations! You reached the goal in {steps} steps!")  # Victory message

# Run the game
if __name__ == "__main__":
    play_maze_game()  # Execute the game when the script is run

class Robot:
    """
    Represents a robot that can move on a grid.

    Attributes:
        num_rows (int): The number of rows in the grid.
        num_cols (int): The number of columns in the grid.
        directions (list): List of valid directions ('N', 'E', 'S', 'W').
        current_row (int): The current row position of the robot.
        current_col (int): The current column position of the robot.
        current_direction (str): The current direction the robot is facing ('N', 'E', 'S', 'W').

    Methods:
        move(command): Move the robot based on the provided command.
        execute_commands(commands): Execute a sequence of commands.
        get_position(): Get the current position and direction of the robot.
    """

    def __init__(self, num_rows, num_cols):
        """
        Initialize the Robot with grid dimensions and initial position.

        Args:
            num_rows (int): The number of rows in the grid.
            num_cols (int): The number of columns in the grid.
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.directions = ['N', 'E', 'S', 'W']
        self.current_row = 0
        self.current_col = 0
        self.current_direction = 'S'

    def move(self, command):
        """
        Move the Robot based on the provided command.

        Args:
            command (str): The command to execute ('N', 'E', 'S', 'W', or 'M').
        """
        if command in self.directions:
            self.current_direction = command
        elif command == 'M':
            if self.current_direction == 'N' and self.current_row > 0:
                self.current_row -= 1
            elif self.current_direction == 'E' and self.current_col < self.num_cols - 1:
                self.current_col += 1
            elif self.current_direction == 'S' and self.current_row < self.num_rows - 1:
                self.current_row += 1
            elif self.current_direction == 'W' and self.current_col > 0:
                self.current_col -= 1

    def execute_commands(self, commands):
        """
        Execute a sequence of commands.

        Args:
            commands (str): A sequence of commands to be executed.
        """
        for command in commands:
            self.move(command)

    def get_position(self):
        """
        Get the current position and direction of the Robot.

        Returns:
            str: A string representing the current position and direction.
        """
        return f"Robot Location: ({self.current_row},{self.current_col},{self.current_direction})"


def main():
    """
    The main function that runs the Robot Simulator program.
    """
    # Define the dimensions of the grid
    num_rows = 4
    num_cols = 5
    
    # Display a welcome message and instructions
    print("Welcome to the Robot Simulator!")
    print("Instructions:")
    print("  - Enter a sequence of commands consisting of 'N', 'E', 'S', 'W', and 'M'.")
    print("  - 'N' to turn North, 'E' to turn East, 'S' to turn South, 'W' to turn West.")
    print("  - 'M' to move one step in the current direction.")
    print("  - The robot starts at position (0,0,S).")
    print(f"  - The grid is {num_cols}x{num_rows}.")

    # Prompt the user for input commands
    commands = input("Enter commands: ").strip().upper()
    
    # Create a robot instance and execute the commands
    robot = Robot(num_rows, num_cols)
    robot.execute_commands(commands)
    
    # Display the robot's final position
    print(robot.get_position())


if __name__ == "__main__":
    main()

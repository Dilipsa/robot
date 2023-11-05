# Robot Simulator

Welcome to the Robot Simulator! This Python program allows you to simulate the movement of a robot on a grid.

## Instructions

1. **Grid Dimensions**: Define the dimensions of the grid (number of rows and columns) when starting the program. This is done in the `main` function.

2. **Commands**:
   - Enter a sequence of commands consisting of 'N', 'E', 'S', 'W', and 'M'.
   - 'N' to turn North, 'E' to turn East, 'S' to turn South, 'W' to turn West.
   - 'M' to move one step in the current direction.

3. **Initial State**: The robot starts at position (0, 0, S) - at the top-left corner of the grid facing South.

4. **Grid Boundaries**: The robot cannot move beyond the boundaries of the grid.

5. **Usage**:
   - Extract the folder.
   - Navigate to the `robot` directory.
   - Execute the Python program using the following command:
   
     ```bash
     python robot_simulator.py
     ```

   - Follow the on-screen instructions to input your commands.
   - The program will display the final position and direction of the robot.

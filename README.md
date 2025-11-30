# Space Traffic Controller

A Python application for managing spacecraft movements and preventing collisions in space.

## Overview

This project simulates a space traffic control system that tracks multiple spacecraft in three-dimensional space and alerts operators when spacecraft come too close to each other.

## Features

- Track multiple spacecraft with 3D positions and velocities
- Collision detection system with configurable safety thresholds
- Real-time position updates
- Visual representation of spacecraft positions
- Status reporting system

## Components

1. **Spacecraft Class**: Represents individual spacecraft with position (x,y,z) and velocity (vx,vy,vz)
2. **SpaceTrafficController Class**: Manages multiple spacecraft and monitors for potential collisions
3. **Main Application**: Demonstrates the system with a sample simulation

## How to Run

1. Navigate to the project directory:
   ```
   cd space-traffic-controller
   ```

2. Run the main application:
   ```
   python src/main.py
   ```

## Customization

You can modify the following parameters in `src/main.py`:

- `collision_threshold`: Minimum safe distance between spacecraft (default: 50.0)
- Initial positions and velocities of spacecraft
- Number of time steps in the simulation

## Classes

### Spacecraft
Represents an individual spacecraft with:
- Unique ID
- 3D position (x, y, z)
- 3D velocity (vx, vy, vz)

Methods:
- `update_position(time_step)`: Updates position based on velocity
- `distance_to(other_spacecraft)`: Calculates distance to another spacecraft

### SpaceTrafficController
Manages multiple spacecraft and prevents collisions:
- Tracks all registered spacecraft
- Monitors distances between spacecraft
- Provides collision alerts
- Generates status reports and visualizations

Methods:
- `add_spacecraft(spacecraft)`: Registers a spacecraft
- `remove_spacecraft(spacecraft_id)`: Removes a spacecraft
- `update_positions(time_step)`: Updates all spacecraft positions
- `check_collisions()`: Identifies potential collisions
- `report_status()`: Prints current status of all spacecraft
- `visualize_space()`: Creates a simple 2D visualization

## Future Enhancements

- Automatic course correction when collisions are detected
- More sophisticated trajectory prediction
- 3D visualization
- Network communication for real-time tracking
- Database integration for persistent spacecraft data
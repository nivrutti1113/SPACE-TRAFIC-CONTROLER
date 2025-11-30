import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from Spacecraft import Spacecraft
from SpaceTrafficController import SpaceTrafficController
import time

def main():
    """
    Main application to demonstrate the space traffic controller.
    """
    print("Initializing Space Traffic Control System...")
    
    # Create a space traffic controller
    controller = SpaceTrafficController(collision_threshold=50.0)
    
    # Create some spacecraft
    apollo = Spacecraft("Apollo", x=0, y=0, z=0, vx=5, vy=3, vz=0)
    enterprise = Spacecraft("Enterprise", x=100, y=50, z=0, vx=-2, vy=1, vz=0)
    millennium_falcon = Spacecraft("Falcon", x=-50, y=-30, z=10, vx=3, vy=-2, vz=1)
    serenity = Spacecraft("Serenity", x=25, y=-75, z=-20, vx=1, vy=4, vz=-1)
    
    # Add spacecraft to the controller
    controller.add_spacecraft(apollo)
    controller.add_spacecraft(enterprise)
    controller.add_spacecraft(millennium_falcon)
    controller.add_spacecraft(serenity)
    
    # Initial status report
    controller.report_status()
    controller.visualize_space()
    
    # Simulate movement over time
    print("Starting space traffic simulation...\n")
    time_step = 1.0  # 1 time unit per iteration
    
    for i in range(10):
        print(f"\n--- Time Step {i+1} ---")
        
        # Update positions
        controller.update_positions(time_step)
        
        # Report status
        controller.report_status()
        
        # Visualize space
        controller.visualize_space()
        
        # Check for collisions
        collisions = controller.check_collisions()
        if collisions:
            print("COLLISION ALERT! Adjusting course...")
            # In a real system, we would adjust velocities here
            # For demo purposes, we'll just pause
            time.sleep(1)
        
        # Pause for readability
        time.sleep(1)
    
    print("\nSimulation complete.")

if __name__ == "__main__":
    main()
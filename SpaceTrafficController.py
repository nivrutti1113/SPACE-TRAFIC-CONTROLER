from Spacecraft import Spacecraft
import math

class SpaceTrafficController:
    """
    Manages multiple spacecraft and prevents collisions in space.
    """
    
    def __init__(self, collision_threshold=100.0):
        """
        Initialize the space traffic controller.
        
        Args:
            collision_threshold (float): Minimum safe distance between spacecraft
        """
        self.spacecraft_list = []
        self.collision_threshold = collision_threshold
    
    def add_spacecraft(self, spacecraft):
        """
        Add a spacecraft to the traffic control system.
        
        Args:
            spacecraft (Spacecraft): The spacecraft to add
        """
        self.spacecraft_list.append(spacecraft)
        print(f"Added {spacecraft}")
    
    def remove_spacecraft(self, spacecraft_id):
        """
        Remove a spacecraft from the traffic control system.
        
        Args:
            spacecraft_id (str): ID of the spacecraft to remove
        """
        for i, craft in enumerate(self.spacecraft_list):
            if craft.id == spacecraft_id:
                removed_craft = self.spacecraft_list.pop(i)
                print(f"Removed {removed_craft}")
                return
        print(f"Spacecraft with ID {spacecraft_id} not found")
    
    def update_positions(self, time_step):
        """
        Update positions of all spacecraft.
        
        Args:
            time_step (float): Time interval for the update
        """
        for spacecraft in self.spacecraft_list:
            spacecraft.update_position(time_step)
    
    def check_collisions(self):
        """
        Check for potential collisions between spacecraft.
        
        Returns:
            list: List of tuples containing pairs of spacecraft that are too close
        """
        collision_pairs = []
        for i in range(len(self.spacecraft_list)):
            for j in range(i + 1, len(self.spacecraft_list)):
                craft1 = self.spacecraft_list[i]
                craft2 = self.spacecraft_list[j]
                distance = craft1.distance_to(craft2)
                
                if distance < self.collision_threshold:
                    collision_pairs.append((craft1, craft2, distance))
                    
        return collision_pairs
    
    def report_status(self):
        """
        Print the current status of all spacecraft.
        """
        print("\n--- Space Traffic Control Report ---")
        if not self.spacecraft_list:
            print("No spacecraft in controlled airspace")
            return
            
        print(f"Tracking {len(self.spacecraft_list)} spacecraft:")
        for spacecraft in self.spacecraft_list:
            print(f"  {spacecraft}")
            
        # Check for collisions
        collisions = self.check_collisions()
        if collisions:
            print("\n!!! COLLISION ALERT !!!")
            for craft1, craft2, distance in collisions:
                print(f"  {craft1.id} and {craft2.id} are {distance:.2f} units apart (threshold: {self.collision_threshold})")
        else:
            print("\nAll spacecraft are at safe distances")
        print("----------------------------------\n")
    
    def visualize_space(self, grid_size=200):
        """
        Create a simple 2D visualization of spacecraft positions.
        
        Args:
            grid_size (int): Size of the visualization grid
        """
        print("\n--- Space Visualization (Top View) ---")
        if not self.spacecraft_list:
            print("No spacecraft to visualize")
            return
            
        # Create empty grid
        grid = [['.' for _ in range(20)] for _ in range(20)]
        
        # Place spacecraft on grid
        for spacecraft in self.spacecraft_list:
            # Normalize coordinates to fit grid
            x_norm = int((spacecraft.x / grid_size) * 10 + 10)
            y_norm = int((spacecraft.y / grid_size) * 10 + 10)
            
            # Ensure coordinates are within bounds
            x_norm = max(0, min(19, x_norm))
            y_norm = max(0, min(19, y_norm))
            
            # Place spacecraft ID on grid (first letter)
            grid[y_norm][x_norm] = spacecraft.id[0] if spacecraft.id else '?'
        
        # Print grid
        print("  " + "".join([f"{i:>2}" for i in range(20)]))
        for i, row in enumerate(grid):
            print(f"{i:>2} " + " ".join(row))
        print("-------------------------------------\n")
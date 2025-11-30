import math

class Spacecraft:
    """
    Represents a spacecraft with position, velocity, and ID.
    """
    
    def __init__(self, spacecraft_id, x=0, y=0, z=0, vx=0, vy=0, vz=0):
        """
        Initialize a spacecraft with position and velocity.
        
        Args:
            spacecraft_id (str): Unique identifier for the spacecraft
            x, y, z (float): Position coordinates in 3D space
            vx, vy, vz (float): Velocity components in 3D space
        """
        self.id = spacecraft_id
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
    def update_position(self, time_step):
        """
        Update the spacecraft's position based on its velocity.
        
        Args:
            time_step (float): Time interval for the update
        """
        self.x += self.vx * time_step
        self.y += self.vy * time_step
        self.z += self.vz * time_step
    
    def distance_to(self, other_spacecraft):
        """
        Calculate the distance to another spacecraft.
        
        Args:
            other_spacecraft (Spacecraft): Another spacecraft to calculate distance to
            
        Returns:
            float: Distance to the other spacecraft
        """
        dx = self.x - other_spacecraft.x
        dy = self.y - other_spacecraft.y
        dz = self.z - other_spacecraft.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)
    
    def __str__(self):
        """
        String representation of the spacecraft.
        """
        return f"Spacecraft {self.id} at ({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
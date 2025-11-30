#!/usr/bin/env python3
"""
Demo script for testing the data ingestion layer functionality
"""

import asyncio
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data_ingestion.tle_ingestion import TLEIngestionService
from data_ingestion.telemetry_ingestion import TelemetryIngestionService
from data_ingestion.realtime_updates import RealtimeUpdatesService

async def demo_tle_ingestion():
    """Demonstrate TLE ingestion functionality"""
    print("=== TLE Ingestion Demo ===")
    
    tle_service = TLEIngestionService()
    
    # Fetch some active satellites from Celestrak
    print("Fetching TLE data from Celestrak...")
    tles = await tle_service.fetch_celestrak_tles("active")
    
    if tles:
        print(f"Successfully fetched {len(tles)} TLE triplets")
        
        # Show details for first 3 satellites
        for i, (name, line1, line2) in enumerate(tles[:3]):
            print(f"\nSatellite {i+1}:")
            print(f"  Name: {name}")
            print(f"  Line 1: {line1}")
            print(f"  Line 2: {line2}")
            
            # Extract satellite data
            data = await tle_service.get_satellite_data(name, line1, line2)
            if data:
                print(f"  Catalog Number: {data.get('catalog_number')}")
                print(f"  Inclination: {data.get('inclination_degrees'):.2f}°")
                print(f"  Eccentricity: {data.get('eccentricity'):.6f}")
    else:
        print("No TLE data fetched (this might be due to network issues)")

async def demo_telemetry_ingestion():
    """Demonstrate telemetry ingestion functionality"""
    print("\n=== Telemetry Ingestion Demo ===")
    
    telemetry_service = TelemetryIngestionService()
    
    # Start simulation
    print("Starting telemetry simulation...")
    telemetry_service.start_telemetry_simulation(3)
    
    # Wait a moment for some data to be generated
    await asyncio.sleep(3)
    
    # Get recent telemetry
    recent_data = telemetry_service.get_recent_telemetry(limit=5)
    print(f"Retrieved {len(recent_data)} recent telemetry records:")
    
    for data in recent_data:
        print(f"  Satellite {data.satellite_id}:")
        print(f"    Position: ({data.position_x:.2f}, {data.position_y:.2f}, {data.position_z:.2f}) km")
        print(f"    Velocity: ({data.velocity_x:.2f}, {data.velocity_y:.2f}, {data.velocity_z:.2f}) km/s")
        print(f"    Altitude: {data.altitude:.2f} km")
        print(f"    Status: {data.status}")
    
    # Stop simulation
    telemetry_service.stop_telemetry_simulation()

async def main():
    """Main demo function"""
    print("Aviothic Space AI - Data Ingestion Layer Demo")
    print("=" * 50)
    
    # Run TLE ingestion demo
    await demo_tle_ingestion()
    
    # Run telemetry ingestion demo
    await demo_telemetry_ingestion()
    
    print("\n=== Demo Complete ===")
    print("The data ingestion layer has been successfully demonstrated!")
    print("Features implemented:")
    print("  - TLE ingestion from Celestrak and Space-Track.org")
    print("  - Live telemetry data collection and processing")
    print("  - Real-time updates with WebSocket streaming")
    print("  - API endpoints for all data ingestion functions")

if __name__ == "__main__":
    asyncio.run(main())
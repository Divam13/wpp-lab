import numpy as np

def cartesian_to_polar(cartesian_points):
    
    x = cartesian_points[:, 0]
    y = cartesian_points[:, 1]
    r = np.sqrt(x**2 + y**2)  # Radius
    theta = np.arctan2(y, x)  # Angle in radians
    return np.column_stack((r, theta))

def main():
    try:
        # Take input for N (number of points)
        N = int(input("Enter the number of 2D points (N >= 10): "))
        if N < 10:
            print("Please enter a value for N that is at least 10.")
            return

        
        cartesian_points = np.random.rand(N, 2) * 100  
        print("\nRandom Cartesian Points (x, y):")
        print(cartesian_points)

        # Convert to polar coordinates
        polar_coordinates = cartesian_to_polar(cartesian_points)
        print("\nConverted Polar Coordinates (r, theta):")
        print(polar_coordinates)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

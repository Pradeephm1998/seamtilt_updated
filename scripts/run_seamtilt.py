from seamtilt.core import calculate_tilt
from seamtilt.utils import validate_angle

def main():
    left = float(input("Enter left seam angle: "))
    right = float(input("Enter right seam angle: "))
    
    if not (validate_angle(left) and validate_angle(right)):
        print("Invalid angles. Must be between -90 and 90 degrees.")
        return

    tilt = calculate_tilt(left, right)
    print(f"Calculated seam tilt: {tilt:.2f} degrees")

if __name__ == "__main__":
    main()

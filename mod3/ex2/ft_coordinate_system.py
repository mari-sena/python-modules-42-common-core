import sys
import math

def get_player_pos() -> None:
	print(
		"Enter new coordinates as floats "
		f"in format 'x,y,z': ", end=""
	)
	coord = input()



def main() -> None:
	print("=== Game Coordinate System ===")
	get_player_pos()

if __name__ == "__main__":
	main()

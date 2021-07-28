def print_grid(arr):
	for i in range(9):
		for j in range(9):
			print(arr[i][j], end = " "),
		print()
# Function to Find the entry in the Grid that is still not used
def find_empty_location(arr, l):
	for row in range(9):
		for col in range(9):
			if(arr[row][col]== 0):
				l[0]= row
				l[1]= col
				return True
	return False
# Returns True or false which indicates whether any assigned entry in the specified row matches the given number.
def used_in_row(arr, row, num):
	for i in range(9):
		if(arr[row][i] == num):
			return True
	return False

# Returns True or false which indicates whether any assigned entry in the specified column matches the given number.
def used_in_col(arr, col, num):
	for i in range(9):
		if(arr[i][col] == num):
			return True
	return False

# Returns true/false which indicates whether any assigned entry within the specified 3x3 box matches the given number
def used_in_box(arr, row, col, num):
	for i in range(3):
		for j in range(3):
			if(arr[i + row][j + col] == num):
				return True
	return False


# Returns true or false which indicates whether it will be valid to assign num to the given row, column.
def check_location_is_safe(arr, row, col, num):
	
# Check if 'num' is not already placed in current row,current column and current 3x3 box
	return (not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,col - col % 3, num))

def solve_sudoku(arr):
	
# 'l' is a list variable that keeps the record of row and col in find_empty_location Function
	l =[0, 0]
	
	# If there is no unassigned location,then we are done
	if(not find_empty_location(arr, l)):
		return True
	
	# Assigning list values to row and col that we got from the above Function
	row = l[0]
	col = l[1]
	for num in range(1, 10):
		if(check_location_is_safe(arr,row, col, num)):
			arr[row][col]= num
			if(solve_sudoku(arr)):
				return True
                        # failure, unmake & try again
			arr[row][col] = 0
			
	# this triggers backtracking	
	return False

# Driver main function to test above functions
if __name__=="__main__":
  grid = []
  r = []
  print("Please enter the values present in the cell and value = 0 for the unassigned cell")
  for i in range(0,9):
    k  = input().split()
    m  = [int(i) for i in k]
    grid.append(m)
  print("the sudoku is (unsolved one)")
  print(grid)
  print("this is the solved sudoku 👇")
  if (solve_sudoku(grid)):
    print_grid(grid)
  else:
    print("no solution exists ")



	

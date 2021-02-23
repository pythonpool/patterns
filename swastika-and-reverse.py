def swastika(row,col): 
	
	for i in range(row): 
		for j in range(col): 
			if(i < row // 2): 
				if (j < col // 2): 
					if (j == 0): 
						print("*", end = "")  
					else: 
						print(" ", end = " ") 
				elif (j == col // 2): 
					print(" *", end = "") 
				else: 
					if (i == 0): 
						print(" *", end = "") 
						
			elif (i == row // 2): 
				print("* ", end = "") 
			else: 
				if (j == col // 2 or j == col - 1): 
					print("* ", end = "") 
				elif (i == row - 1): 
					if (j <= col // 2 or j == col - 1): 
						print("* ", end = "") 
					else: 
						print(" ", end = " ") 
				else: 
					print(" ", end = " ") 
		print() 

def revswastika(row, col): 
      
    for i in range(row):  
        for j in range(col): 
            if (i < row // 2): 
                if (j < col // 2): 
                    if (i == 0 and i < row // 2): 
                        print("* ", end = "") 
                    else: 
                        print(" ", end = " ") 
                elif (j == col // 2): 
                    print("*", end = "") 
                else: 
                    if (i < row // 2 and j < col - 1): 
                        print(" ", end = " ") 
                    if (j == col - 1): 
                        print(" *", end = "") 
            elif (i == row // 2): 
                print("* ", end = "") 
            else: 
                if (j == col // 2 or j == 0): 
                    print("* ", end = "") 
                elif (i == row - 1): 
                    if (j <= col // 2 or j == col): 
                        print(" ", end = " ") 
                    else: 
                        print("* ", end = "") 
                else: 
                    print(" ", end = " ") 
        print()

row = 7; col = 7
print("Swastik Pattern")
swastika(row, col)
print("Swastik Reverse Pattern")
revswastika(row, col)
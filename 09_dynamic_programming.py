def search(word_a, word_b):
    cell = []
    for row in range(len(word_a)):
		cell[row] = row
		for col in range(len(word_a)):
			cell[row][col] = 0
		
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                # Буквы совпадают.
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                # Буквы не совпадают.
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return cell


print(search('fish', 'fosh'))
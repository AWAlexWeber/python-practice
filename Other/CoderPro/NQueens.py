def nqueens_helper(n, row, col, asc_diag, desc_diag, queen_pos):
  if len(queen_pos) == n:
    return queen_pos

  curr_row = len(queen_pos)
  for curr_col in range(n):
    if col[curr_col] and row[curr_row] and asc_diag[curr_row + curr_col] and desc_diag[curr_row - curr_col]:
      col[curr_col] = False
      row[curr_row] = False
      asc_diag[curr_row + curr_col] = False
      desc_diag[curr_row - curr_col] = False

      queen_pos.append((curr_row, curr_col))
      nqueens_helper(n, row, col, asc_diag, desc_diag, queen_pos)

      if len(queen_pos) == n:
        return queen_pos

      # backtrack
      col[curr_col] = True
      row[curr_row] = True
      asc_diag[curr_row + curr_col] = True
      desc_diag[curr_row - curr_col] = True
      queen_pos.pop()

  return queen_pos


def nqueens(n):
  col = [True] * n
  row = [True] * n
  asc_diag = [True] * (n * 2 - 1)
  desc_diag = [True] * (n * 2 - 1)
  return nqueens_helper(n, col, row, asc_diag, desc_diag, [])


print(nqueens(5))
fn main() {
    let sudoku = vec![
        vec!['.', '.', '.', '9', '.', '.', '.', '.', '.'],
        vec!['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        vec!['.', '.', '3', '.', '.', '.', '.', '.', '1'],
        vec!['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        vec!['1', '.', '.', '.', '.', '.', '3', '.', '.'],
        vec!['.', '.', '.', '.', '2', '.', '6', '.', '.'],
        vec!['.', '9', '.', '.', '.', '.', '.', '7', '.'],
        vec!['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        vec!['8', '.', '.', '8', '.', '.', '.', '.', '.'],
    ];
    println!("{}", is_valid_sudoku(sudoku));
}

pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
    let mut res = true;
    for i in 0..board.len() {
        for j in 0..board[0].len() {
            if !res {
                return false;
            }
            if board[i][j] != '.' {
                res = check_row_col(&board, i, j);
            }
        }
    }

    for i in 0..board.len() {
        for j in 0..board[0].len() {
            if !res {
                return false;
            }
            if board[i][j] != '.' {
                res = check_square(&board, i, j);
            }
        }
    }

    true
}

pub fn check_row_col(board: &Vec<Vec<char>>, row: usize, col: usize) -> bool {
    let rows = board.len();
    let cols = board[0].len();

    for i in 0..rows {
        if i == row {
            continue;
        }
        if board[i][col] == board[row][col] {
            return false;
        }
    }
    for i in 0..cols {
        if i == col {
            continue;
        }
        if board[row][i] == board[row][col] {
            return false;
        }
    }
    true
}

pub fn check_square(board: &Vec<Vec<char>>, row: usize, col: usize) -> bool {
    let row_bucket = vec![0, 3, 6, 9];
    let col_bucket = vec![0, 3, 6, 9];

    for i in row_bucket[row / 3]..row_bucket[(row / 3) + 1] {
        for j in col_bucket[col / 3]..col_bucket[(col / 3) + 1] {
            if i == row && j == col {
                continue;
            }
            if board[i][j] == board[row][col] {
                return false;
            }
        }
    }
    true
}

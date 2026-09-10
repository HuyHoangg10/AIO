raw_prices = [" 120 ", "invalid", " 450 \n", "free", " 99 "]

clean_prices = [int(data) for data in raw_prices if data.strip().isdigit()]

matrix = [[0 for _ in range(4)] for _ in range(3)]

student_scores = [
    [8.0, 7.5, 9.0],  
    [6.0, 5.5, 7.0], 
    [9.5, 8.0, 8.5], 
]

print(student_scores[1][2])
student_scores[2][2] = 10.0

matrix_scores = [
    [7.0, -1.0, 8.5],
    [9.0, 6.5, -2.0],
    [5.0, 8.0, 10.0],
]
clean_scores = [score for row in matrix_scores for score in row if score > 0]
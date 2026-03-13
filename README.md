# Matrix Multiplication
An implementation of an algorithm to recursively calculate the multiplication of two $n x n$ matrices. Where the value of $n$ is the number of rows and columns of the two matrices. The value of $n$ also must be a multiple of 2. Traditionally the multiplication of two $n x n$ matrices has a time complexity of $O(n^3)$. Using a Divide and Conquer algorithm such as the one implemented here the time complexity is reduced down to $O(n^{log7})$. The algorithm recursively creates quadrants of the return matrix by using the following formula $$
\begin{bmatrix} I & J \\\\ 
K & L 
\end{bmatrix} = 
\begin{bmatrix} A & B \\\\ 
C & D 
\end{bmatrix} + 
\begin{bmatrix} E & F \\\\ 
G & H 
\end{bmatrix}
$$
# A screenshot of the algorithm's code
![A screenshot of the algorithm](MatrixMultiplierCode.png)
# A screenshot of the main function to run the code (with sample matrices)
![A screenshot of the main function](MatrixMainCode.png)
# A screenshot of the results of the multiplication performed on the sample matrices
![A screenshot of the Results of the matrices in main](MatrixResult.png)

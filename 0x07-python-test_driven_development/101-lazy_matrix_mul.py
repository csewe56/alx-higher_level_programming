import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    - m_a: First matrix
    - m_b: Second matrix

    Returns:
    - Resulting matrix after multiplication
    """
    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except ValueError as ve:
        raise ValueError("shapes {} and {} not aligned: {}"
                         .format(np.shape(m_a), np.shape(m_b), str(ve)))

if __name__ == "__main__":
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[1, 2], [3, 4]])
    result = lazy_matrix_mul(matrix_a, matrix_b)
    print(result)

    matrix_c = np.array([[1, 2]])
    matrix_d = np.array([[3, 4], [5, 6]])
    result = lazy_matrix_mul(matrix_c, matrix_d)
    print(result)


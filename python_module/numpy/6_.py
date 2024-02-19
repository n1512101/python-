import numpy as np

# nanを各列の平均値に変換する関数
def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:,i]
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]
            temp_col[temp_col!=temp_col] = temp_not_nan_col.mean()
    return t1

if __name__ == '__main__':
    t1 = np.arange(12).reshape((3,4)).astype("float")
    t1[1,2:] = np.nan
    print(t1)
    """
    [[ 0.  1.  2.  3.]
    [ 4.  5. nan nan]
    [ 8.  9. 10. 11.]]
    """
    
    t1 = fill_ndarray(t1)
    print(t1)
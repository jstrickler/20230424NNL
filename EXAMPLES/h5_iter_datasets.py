#
import h5py
import numpy as np
import pandas as pd

H5_FILE = '../DATA/hdf5_test.h5'

H5_DATASET = '/arrays/2D int8x9'

hfile = h5py.File(H5_FILE, mode="r")  # open HDF5 file

dset = hfile[H5_DATASET]  # get dataset by path
print(f"type(dset): {type(dset)}")
np_data = np.array(dset)
print(f"np_data: {np_data}")
df  = pd.DataFrame(dset)
print(f"df: {df}")



for i, row in enumerate(dset):  # iterate over rows in dataset (and get row #s)
    print("ROW {}: {}".format(i, row))  # print row
print()

print("Row 1:")
print(dset[1])  # print 2nd row of dataset
print()

print("Column 1:")
print(dset[:, 1])
print()

print("Rows 3 & 4, Columns 5 & 6")
print(dset[3:5, 5:7])

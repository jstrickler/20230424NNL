import h5py as h5
HDF5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
DATASET = '/Domain_03/OSBS/min_1/boom_1/temperature'

with h5.File(HDF5_FILE) as hdf5_file:  # open file
    print("HDF5 File object: {}".format(hdf5_file))
    ds = hdf5_file[DATASET]  # dataset is 1-dimensional -- each row is compound type
    print()
    print("dataset: {}".format(ds[:]))
    print()
    print("len(dataset): {}".format(len(ds)))
    print("dataset.shape: {}".format(ds.shape))
    print("dataset.ndim: {}".format(ds.ndim))
    print("dataset[0]: {}".format(ds[0]))

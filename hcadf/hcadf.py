"""
hcadataframe is a module for accessing data in HCA using the familiar pandas
interface.

usage:

```
import hcadf

df = hcadf.df("MyStudyId")
df.describe()
```

"""

import pandas as pd
import argparse


def df(bundle_id):
    """
    Takes a bundle_id, downloads the HDF5 file, and returns it as a dataframe.
    :param bundle_id:
    :return:
    """
    # List the files of the bundle

    # Download the hdf5 file to memory

    # load using pandas and return as dataframe

    return pd.Dataframe()

def download_bundle_hdf5(bundle_id, path):
    """
    Lists the files of a bundle and downloads the hdf5 that is expected to
    be the sample-feature matrix.

    :param bundle_id:   The location of the bundle.
    :param path:        The location of the resulting hdf5
    :return:
    """
    # List the files of the bundle

    # Download the hdf5 to the path

    return


def main(args=None):
    """
    Downloads an HDF5 from the bundle location to the specified directory.

    Accepts the UUID of the bundle that is expected to contain a gene-cell
    matrix.

    :param args:
    :return:
    """
    parser = argparse.ArgumentParser(
        description='Download an HDF5 from the Human Cell Atlas.')
    parser.add_argument("bundle_id", type=str,
                        help="The study identifier is located.")

    parsed = parser.parse_args(args)
    print(parsed)
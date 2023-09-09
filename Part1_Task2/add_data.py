import pandas as pd

def add_data(df1,df2):
    """Add new data to the existing dataframe.

        Parameters
        ----------
        df1 : existing dataframe of shape (n_samples_1,n_features)
        df2 : new data of shape (n_samples_2,n_features)

        Returns
        -------
        df3: DataFrame of shape (n_samples_1+n_samples_2,n_features)

        Examples
        --------
        >>> from add_data import add_data
        >>> import pandas as pd
        >>> df1 = pd.DataFrame({"Col1":[1,2,3],"Col2":[4,5,6]})
        >>> df2 = pd.DataFrame({"Col1":[1,2],"Col2":[4,5]})
        >>> print(add_data(df1,df2))
            Col1  Col2
        0     1     4
        1     2     5
        2     3     6
        3     1     4
        4     2     5
        """
    df3 = pd.concat([df1, df2], ignore_index = True)
    return df3
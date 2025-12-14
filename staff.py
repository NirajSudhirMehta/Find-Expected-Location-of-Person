import os
import pandas as pd

class Staffs():
    """staff master"""

    def __init__(self):
        """Initialize instance attributes."""
        self.__staff_csv_file = os.path.join(os.path.dirname(__file__), r"data/staffs.csv")
        self.__staff_df = pd.DataFrame()
        self.__staff_df = pd.read_csv(self.__staff_csv_file)

    # Instance method
    def method(self, arg):
        """Do something with the instance."""
        return f"class method"

    def search(self, search_str:str):
        """find in staff df"""
        # print(self.__staff_df)
        search_list = [x for x in search_str.split(" ") if x]
        # print(search_list)

        # create a single string per row from all columns
        row_text = self.__staff_df.astype(str).agg(" ".join, axis=1).str.lower()

        # require all items present in the same row
        mask = pd.Series(True, index=self.__staff_df.index)
        for item in search_list:
            mask &= row_text.str.contains(item.lower(), na=False)

        result = self.__staff_df[mask]

        # print(self.__staff_df)
        # print(search_list)
        # print(result)
        return result

    # Class method: receives the class (cls)
    @classmethod
    def from_string(cls, s):
        parts = s.split(',')
        return cls(parts[0], parts[1:])

    # Static method: no implicit first arg
    @staticmethod
    def helper(x):
        return x * 2

    # Property: computed attribute with getter/setter
    @property
    def value(self):
        return self._private

    @value.setter
    def value(self, v):
        if v < 0:
            raise ValueError("value must be >= 0")
        self._private = v


def main():

    staff_master = Staffs()
    # staff_master.search('mehta 123')
    print(staff_master.search('mehta 12'))


if __name__ == "__main__":
    main()


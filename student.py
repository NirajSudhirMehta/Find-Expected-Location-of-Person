import os
import pandas as pd

class Students():
    """student master"""

    def __init__(self):
        """Initialize instance attributes."""
        self.__student_csv_file = os.path.join(os.path.dirname(__file__), r"data/students.csv")
        self.__student_df = pd.DataFrame()
        print(self.__student_csv_file)
        self.__student_df = pd.read_csv(self.__student_csv_file)
        print(self.__student_df)

    # Instance method
    def method(self, arg):
        """Do something with the instance."""
        return f"class method"

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

    student_master = Students()

if __name__ == "__main__":
    main()

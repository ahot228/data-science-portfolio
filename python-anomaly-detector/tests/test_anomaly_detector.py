import unittest
from src.anomaly_detector import (employees, sales, students)

def check_no_nulls(df, column):
    return df[column].notna().all()

def check_no_duplicates(df, column):
    return df[column].is_unique

def check_schema(df, expected_columns):
    return set(df.columns) == set(expected_columns)


class TestDataChecks(unittest.TestCase):

    def setUp(self):
        self.employees = employees

    def test_no_nulls(self):
        self.assertTrue(check_no_nulls(self.employees, "name"))

    def test_no_duplicates(self):
        self.assertTrue(check_no_duplicates(self.employees, "id"))

    def test_schema_valid(self):
        expected = ["id", "name", "age", "salary"]
        self.assertTrue(check_schema(self.employees, expected))


def test_no_nulls():
    assert check_no_nulls(employees, "name")
    assert check_no_nulls(sales, "customer")
    assert check_no_nulls(students, "name")

def test_no_duplicates():
    assert check_no_duplicates(employees, "id")
    assert check_no_duplicates(sales, "order_id")
    assert check_no_duplicates(students, "student_id")

def test_schema_valid():
    assert check_schema(employees, ["id", "name", "age", "salary"])
    assert check_schema(sales, ["order_id","customer", "region", "units_sold", "revenue"])
    assert check_schema(students, ["student_id","name", "math_score", "science_score", "grade"])

def test_no_negative_ages():
    assert (employees["age"] >= 0).all()
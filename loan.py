# test_oop_loan_pmt.py

from oop_loan_pmt import LoanCalculator
import pytest


# Unit tests
def test_calculate_monthly_interest():
    loan_calculator = LoanCalculator(100000, 0.06, 30)
    assert loan_calculator.calculate_monthly_interest() == 500.0

def test_calculate_monthly_principal():
    loan_calculator = LoanCalculator(100000, 0.06, 30)
    assert loan_calculator.calculate_monthly_principal() == 99.55

def test_calculate_monthly_payment():
    loan_calculator = LoanCalculator(100000, 0.06, 30)
    assert loan_calculator.calculate_monthly_payment() == 599.55


# Functional tests
def test_loan_calculator_with_zero_loan_amount():
    with pytest.raises(ValueError):
        loan_calculator = LoanCalculator(0, 0.06, 30)

def test_loan_calculator_with_negative_loan_amount():
    with pytest.raises(ValueError):
        loan_calculator = LoanCalculator(-100000, 0.06, 30)

def test_loan_calculator_with_zero_interest_rate():
    with pytest.raises(ValueError):
        loan_calculator = LoanCalculator(100000, 0, 30)

def test_loan_calculator_with_negative_interest_rate():
    with pytest.raises(ValueError):
        loan_calculator = LoanCalculator(100000, -0.06, 30)

def test_loan_calculator_with_zero_years():
    with pytest.raises(ValueError):
        loan_calculator = LoanCalculator(100000, 0.06, 0)

def test_loan_calculator_with_negative_years():
    with pytest.raises(ValueError):
        loan_calculator = LoanCalculator(100000, 0.06, -30)

def test_calculate_monthly_payment_with_rounding():
    loan_calculator = LoanCalculator(99999.99, 0.06, 30)
    assert loan_calculator.calculate_monthly_payment() == 599.55


# Coverage tests
def test_coverage():
    loan_calculator = LoanCalculator(100000, 0.06, 30)
    assert loan_calculator.calculate_monthly_interest() == 500.0
    assert loan_calculator.calculate_monthly_principal() == 99.55
    assert loan_calculator.calculate_monthly_payment() == 599.55
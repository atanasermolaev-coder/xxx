import pytest
from xxx import monthly_payment, overpayment


def test_payment_with_rate():
    result = monthly_payment(1_000_000, 12, 1)
    assert result == pytest.approx(88848.79, abs=0.01)


def test_payment_zero_rate():
    assert monthly_payment(1_200_000, 0, 1) == 100_000


def test_overpayment_positive():
    assert overpayment(1_000_000, 12, 1) > 0


def test_overpayment_zero_rate():
    assert overpayment(1_000_000, 0, 5) == pytest.approx(0)


def test_bad_amount():
    with pytest.raises(ValueError):
        monthly_payment(-5, 10, 1)


def test_bad_years():
    with pytest.raises(ValueError):
        monthly_payment(1000, 10, 0)

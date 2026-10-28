import pytest
from xxx import monthly_payment, overpayment


def test_payment_known_value():
    # 1 млн под 12% на 1 год -> примерно 88848.79 в месяц
    result = monthly_payment(1_000_000, 12, 1)
    assert result == pytest.approx(88848.79, abs=0.01)


def test_payment_zero_rate():
    # без процентов просто делим сумму на количество месяцев
    result = monthly_payment(1_200_000, 0, 1)
    assert result == pytest.approx(100_000, abs=0.01)


def test_overpayment_known_value():
    # 88848.79 * 12 - 1_000_000 -> примерно 66185.46
    result = overpayment(1_000_000, 12, 1)
    assert result == pytest.approx(66185.46, abs=1)


def test_overpayment_zero_rate():
    # без процентов переплаты нет
    result = overpayment(1_000_000, 0, 5)
    assert result == pytest.approx(0, abs=0.01)


def test_overpayment_matches_payment():
    # переплата = все платежи минус сумма кредита
    amount, rate, years = 3_000_000, 9, 10
    total = monthly_payment(amount, rate, years) * years * 12
    result = overpayment(amount, rate, years)
    assert result == pytest.approx(total - amount, abs=0.01)


def test_longer_term_means_smaller_payment():
    short = monthly_payment(2_000_000, 10, 5)
    long = monthly_payment(2_000_000, 10, 20)
    assert long < short


def test_higher_rate_means_bigger_payment():
    low = monthly_payment(2_000_000, 5, 15)
    high = monthly_payment(2_000_000, 15, 15)
    assert high > low


def test_bad_amount():
    with pytest.raises(ValueError):
        monthly_payment(-5, 10, 1)


def test_bad_years():
    with pytest.raises(ValueError):
        monthly_payment(1000, 10, 0)


def test_bad_rate():
    with pytest.raises(ValueError):
        monthly_payment(1000, -1, 1)
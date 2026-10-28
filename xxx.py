def monthly_payment(amount, annual_rate, years):
    """Ежемесячный аннуитетный платёж."""
    if amount <= 0 or years <= 0 or annual_rate < 0:
        raise ValueError("Неверные входные данные")
    months = years * 12
    rate = annual_rate / 100 / 12
    if rate == 0:
        return amount / months
    k = (1 + rate) ** months
    return amount * rate * k / (k - 1)


def overpayment(amount, annual_rate, years):
    """Сколько переплатим банку сверх суммы кредита."""
    total = monthly_payment(amount, annual_rate, years) * years * 12
    return total - amount


def main():
    amount = float(input("Сумма кредита: "))
    rate = float(input("Ставка, % годовых: "))
    years = int(input("Срок, лет: "))
    print(f"Платёж в месяц: {monthly_payment(amount, rate, years):.2f}")
    print(f"Переплата: {overpayment(amount, rate, years):.2f}")


if __name__ == "__main__":
    main()

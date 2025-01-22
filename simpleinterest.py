def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
principal = int(input("Enter the principal amount:"))
rate = int(input("Enter the rate of interest:"))
time = int(input("Enter the time in years:"))
print(f"Simple Interest ({principal}, {rate}, {time} years):", simple_interest(principal, rate, time))
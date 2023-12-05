def month(n):
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_name[n - 1]

m_num = int(input("Enter month number: "))
print("Month name:", month(m_num))
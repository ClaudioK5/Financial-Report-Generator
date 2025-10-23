import subprocess
from generate_report import generate_financial_report

balance_sheet_process = subprocess.run(['python', 'Balance sheet Equity/main.py'], capture_output=True, text=True)

final_sum = float(balance_sheet_process.stdout.strip())

balance_sheet_process_liabilities = subprocess.run(['python', 'Balance sheet Liabilities/main.py'], capture_output=True, text=True)

final_sum_liabilities = float(balance_sheet_process_liabilities.stdout.strip())

company_equity = final_sum - final_sum_liabilities

print(final_sum_liabilities)

net_profits_process = subprocess.run(['python', 'Net Profits/main.py'], capture_output=True, text=True)

net_profits = float(net_profits_process.stdout.strip().splitlines()[0])

total_cost = float(net_profits_process.stdout.strip().splitlines()[1])

total_revenue = float(net_profits_process.stdout.strip().splitlines()[2])

generate_financial_report(net_profits, total_revenue, total_cost, final_sum, final_sum_liabilities, company_equity)


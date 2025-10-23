from database import SessionLocal
from models import LiabilityItem

db = SessionLocal()

try:

    items = db.query(LiabilityItem).all()

    final_sum_liabilities = sum(item.amount for item in items if not item.is_paid)

    print(final_sum_liabilities)


finally:

    db.close()

from database import SessionLocal
from models import InventoryItem

db = SessionLocal()

try:

    items = db.query(InventoryItem).all()

    final_sum = sum(item.quantity * item.price for item in items)

    print(final_sum)


finally:

    db.close()


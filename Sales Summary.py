import sqlite3
 

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales(
      product TEXT,
      quantity INTEGER,
      price REAL
    )
''')




sample_data = [
    ('Product A',10,10.00),
    ('Product B',5,25.00),
    ('Product A',3,10.00),
    ('Product C',2,50.00),
]
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", sample_data)
conn.commit()



cursor.execute("SELECT SUM(quantity * price) FROM sales")
total_revenue = cursor.fetchone()[0] or 0
 

cursor.execute("select sum(quantity) from sales")
total_items = cursor.fetchone()[0] or 0
 

cursor.execute("""
    select product, sum(quantity) as total_quantity, 
           sum(quantity * price) as total_revenue
    from sales
    group by product
    order by total_revenue DESC
""")
sales_by_product = cursor.fetchall()
 

print("Basic Sales Summary")
print(f"Total Revenue: Rs{total_revenue:.2f}")
print(f"Total Items Sold: {total_items}\n")
 
print("Sales by Product:")
for product, qty, revenue in sales_by_product:
    print(f"- {product}: {qty} items, Rs{revenue:.2f}")
 

conn.close()

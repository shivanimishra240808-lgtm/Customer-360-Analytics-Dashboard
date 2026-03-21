
CREATE TABLE Orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP,
    order_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE Products (
    product_id VARCHAR(20),
    product_name TEXT,
    price FLOAT
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id VARCHAR(20),
    payment_method VARCHAR(20),
    payment_status VARCHAR(20),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

select * from Payments;
select * from Products;
select * from Orders;
select * from Customers;

--TOTAL CUSTOMERS
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM customers;

-- TOTAL REVENUE
SELECT ROUND(SUM(total_spent), 2) AS total_revenue
FROM customers;

-- TOTAL ORDERS
SELECT COUNT(order_id) AS total_orders
FROM orders;

-- AVG ORDER VALUE
SELECT 
    ROUND(SUM(total_spent) / COUNT(order_id), 2) AS avg_order_value
FROM orders;

--TOP SPENDING CUSTOMER
SELECT customer_id, SUM(total_spent) AS total_spent
FROM customers
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 1;

-- TOP 5 COUNTRIES BY REVENUE
SELECT country, SUM(total_spent) AS revenue
FROM customers
GROUP BY country
ORDER BY revenue DESC
LIMIT 5;


-- CUSTOMER SEGMENTATION
SELECT customer_id,
       SUM(total_spent) AS total_spent,
       CASE 
           WHEN SUM(total_spent) > 50000 THEN 'High Value'
           WHEN SUM(total_spent) >= 10000 THEN 'Medium Value'
           ELSE 'Low Value'
       END AS segment
FROM customers
GROUP BY customer_id;


--MONTHLY REVENUE TREND
SELECT 
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(total_spent) AS monthly_revenue
FROM orders
GROUP BY month
ORDER BY month;

--REPEAT CUSTOMERS
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1;

--REPEAT CUSTOMER COUNT
SELECT COUNT(*) AS repeat_customers
FROM (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(order_id) > 1
) AS subquery;


--REVENUE BY SEGMENT
SELECT 
    CASE 
        WHEN total_spent > 50000 THEN 'High Value'
        WHEN total_spent >= 10000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS segment,
    SUM(total_spent) AS revenue
FROM customers
GROUP BY segment;


-- COUNTRY-WISE CUSTOMER COUNT
SELECT country, COUNT(customer_id) AS total_customers
FROM customers
GROUP BY country
ORDER BY total_customers DESC;


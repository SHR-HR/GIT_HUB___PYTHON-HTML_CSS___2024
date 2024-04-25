-- SELECT father.user_text , child.user_text 
-- FROM user_comments father
-- LEFT JOIN user_comments child ON child.user_comment_id = father.comment_connect_id


-- SELECT *
-- FROM products 
-- JOIN categories ON products.category_id = categories.category_id
-- JOIN suppliers ON products.supplier_id = suppliers.supplier_id


-- CREATE TABLE user_comments
-- (
-- user_comment_id SERIAL PRIMARY KEY,
-- user_text TEXT NOT NULL,
-- comment_connect_id INT REFERENCES user_comments(user_comment_id)	
-- )



-- SELECT category_name, product_name
-- FROM products
-- LEFT JOIN categories ON products.category_id = categories.category_id
-- ORDER BY category_name

-- SELECT last_name, orders.ship_name 
-- FROM employees
-- LEFT JOIN orders ON orders.employee_id = employees.employee_id


-- SELECT ship_name, employees.first_name 
-- FROM orders
-- LEFT JOIN employees ON orders.employee_id = employees.employee_id
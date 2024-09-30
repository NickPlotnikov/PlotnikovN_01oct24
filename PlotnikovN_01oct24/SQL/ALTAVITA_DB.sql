INSERT INTO Categories (category_id, category_name) VALUES
(1, 'Фрукты'),
(2, 'Овощи'),
(3, 'Зерновые'),
(4, 'Молочные продукты');

INSERT INTO Products (product_id, product_name, category_id, calories, price) VALUES
(1, 'Яблоко', 1, 52, 1.00),
(2, 'Банан', 1, 89, 1.20),
(3, 'Морковь', 2, 41, 0.80),
(4, 'Огурец', 2, 16, 0.50),
(5, 'Рис', 3, 130, 2.00),
(6, 'Молоко', 4, 42, 1.50);

INSERT INTO Nutritional_Information (product_id, protein, carbohydrates, fat, fiber) VALUES
(1, 0.3, 14.0, 0.2, 2.4),
(2, 1.1, 23.0, 0.3, 2.6),
(3, 0.9, 10.0, 0.2, 2.8),
(4, 0.7, 3.6, 0.1, 0.5),
(5, 2.7, 28.0, 0.3, 0.4),
(6, 3.4, 5.0, 1.0, 0.0);
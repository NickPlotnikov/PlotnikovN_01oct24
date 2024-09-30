CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category_id INT,
    calories INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Nutritional_Information (
    product_id INT,
    protein DECIMAL(10, 2),
    carbohydrates DECIMAL(10, 2),
    fat DECIMAL(10, 2),
    fiber DECIMAL(10, 2),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

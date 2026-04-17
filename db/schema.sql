-- Create locations table
CREATE TABLE locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(50)
);

-- Create traffic_data table
CREATE TABLE traffic_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    location_id INT,
    vehicle_count INT,
    avg_speed FLOAT,
    weather VARCHAR(20),
    accident INT,
    congestion INT,
    hour INT,
    day VARCHAR(10),
    traffic_level VARCHAR(10),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);
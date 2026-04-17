-- ========================================
-- BASIC JOIN (verify data)
-- ========================================
SELECT l.location_name, t.vehicle_count, t.avg_speed
FROM traffic_data t
JOIN locations l ON t.location_id = l.location_id
LIMIT 10;


-- ========================================
-- AVG TRAFFIC PER LOCATION
-- ========================================
SELECT l.location_name, AVG(t.vehicle_count) AS avg_traffic
FROM traffic_data t
JOIN locations l ON t.location_id = l.location_id
GROUP BY l.location_name
ORDER BY avg_traffic DESC;


-- ========================================
-- HIGH CONGESTION AREAS
-- ========================================
SELECT l.location_name, COUNT(*) AS congestion_count
FROM traffic_data t
JOIN locations l ON t.location_id = l.location_id
WHERE t.congestion = 1
GROUP BY l.location_name
ORDER BY congestion_count DESC;


-- ========================================
-- TRAFFIC BY HOUR
-- ========================================
SELECT t.hour, AVG(t.vehicle_count) AS avg_traffic
FROM traffic_data t
GROUP BY t.hour
ORDER BY t.hour;


-- ========================================
-- TRAFFIC BY LOCATION + HOUR (ADVANCED GROUP)
-- ========================================
SELECT l.location_name, t.hour, AVG(t.vehicle_count) AS avg_traffic
FROM traffic_data t
JOIN locations l ON t.location_id = l.location_id
GROUP BY l.location_name, t.hour
ORDER BY t.hour;


-- ========================================
-- WEATHER IMPACT ON TRAFFIC
-- ========================================
SELECT weather, AVG(vehicle_count) AS avg_traffic
FROM traffic_data
GROUP BY weather;


-- ========================================
-- WINDOW FUNCTION (VERY ADVANCED)
-- ========================================
SELECT location_name, avg_traffic,
       RANK() OVER (ORDER BY avg_traffic DESC) AS rank_position
FROM (
    SELECT l.location_name, AVG(t.vehicle_count) AS avg_traffic
    FROM traffic_data t
    JOIN locations l ON t.location_id = l.location_id
    GROUP BY l.location_name
) sub;


-- ========================================
-- PEAK HOURS DETECTION
-- ========================================
SELECT hour, COUNT(*) AS traffic_events
FROM traffic_data
GROUP BY hour
ORDER BY traffic_events DESC
LIMIT 5;
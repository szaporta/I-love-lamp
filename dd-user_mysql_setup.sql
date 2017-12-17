CREATE USER 'datadog'@'localhost' IDENTIFIED BY 'hKsJzswSeY=J88vSQixGdxb1';
GRANT REPLICATION CLIENT ON *.* TO 'datadog'@'localhost' WITH MAX_USER_CONNECTIONS 5;
GRANT PROCESS ON *.* TO 'datadog'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'datadog'@'localhost'

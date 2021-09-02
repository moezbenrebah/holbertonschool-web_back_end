-- this script ranks country origin bands bu the number of funs
-- the script can be executed on any db

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

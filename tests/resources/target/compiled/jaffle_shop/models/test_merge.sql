

WITH s AS (
    SELECT
      "x" AS col1,
      "y" AS col2,
      "z" AS col3,
)

SELECT
  CONCAT(col1, ":::", col2) AS _unique_key,
  col1,
  col2,
  col3,
FROM s
# python_disnet_sql_access
Programmatic access to the DISNET database (https://disnet.ctb.upm.es/) using the python script practicasBBDD.py\
Upon running the script, a visual menu will appear to facilitate access and further queries to users not familiar with SQL.

Imported python modules for this: 
- sys, 
- os, 
- tabulate, 
- mysql.connector


\
Information and tools provided by this programmatic access:
1. Database information
2. Drugs information
3. Disesases information
4. Fenotypical effects information
5. Targets information
6. Insertions
7. Deletions
8. Modifications

...
### MySQL queries 
Query 1A: 
```
SELECT
    (SELECT
            COUNT(*)
        FROM
            drug) AS NumDrugs,
    (SELECT
            COUNT(*)
        FROM
            disease) AS NumDiseases,
    (SELECT
            COUNT(*)
        FROM
            phenotype_effect) AS PhenoEff,
    (SELECT
            COUNT(*)
        FROM
            target) AS NumTargets
```

Query 1B:
```
SELECT
    drug_id,
    drug_name,
    molecular_type,
    chemical_structure,
    inchi_key
FROM
    drug
WHERE
    drug_id IS NOT NULL
        AND drug_name IS NOT NULL
        AND molecular_type IS NOT NULL
        AND chemical_structure IS NOT NULL
LIMIT 10

    
    SELECT
        disease_id, disease_name
FROM
        disease
WHERE
        disease_id IS NOT NULL
            AND disease_name IS NOT NULL
LIMIT 10


SELECT
    phenotype_id, phenotype_name
FROM
    phenotype_effect
WHERE
    phenotype_id IS NOT NULL
        AND phenotype_name IS NOT NULL
LIMIT 10


    SELECT
        target_id, target_name_pref, target_type, target_organism
FROM
        target
WHERE
    target_id IS NOT NULL
        AND target_name_pref IS NOT NULL
        AND target_type IS NOT NULL
        AND target_organism IS NOT NULL
LIMIT 10

```

Query 2A:
```
SELECT
    drug_name, molecular_type, chemical_structure, inchi_key
FROM
    drug
WHERE
    drug_id = %s
```

Query 2B:
```
SELECT
    synonymous.synonymous_name
FROM
    synonymous,
    drug
WHERE
    drug.drug_name = %s
        AND synonymous.drug_id = drug.drug_id
```

Query 2C:
```
SELECT
    ATC_code_id
FROM
    ATC_code
WHERE
    drug_id = %s
```

Query 3A:
```
SELECT
    drug.drug_id, drug.drug_name
FROM
    drug,
    disease,
    drug_disease
WHERE
    disease.disease_name = %s
        AND drug_disease.drug_id = drug.drug_id
        AND disease.disease_id = drug_disease.disease_id
```

Query 3B:
```
SELECT
    disease_name, drug_name, inferred_score
FROM
    drug_disease,
    drug,
    disease
WHERE
    drug_disease.disease_id = disease.disease_id
        AND drug_disease.drug_id = drug.drug_id
ORDER BY inferred_score DESC
LIMIT 1
```

Query 4A*:
```
SELECT
    phenotype_effect.phenotype_id,
    phenotype_effect.phenotype_name
FROM
    phenotype_effect,
    drug_phenotype_effect
WHERE
    drug_phenotype_effect.drug_id = %s
        AND drug_phenotype_effect.phenotype_type = %s
        AND phenotype_effect.phenotype_id = drug_phenotype_effect.phenotype_id
```
*Upon execution in the Python script I provide as a string "INDICATION", apart from the own query and inputs

Query 4B*:
```
SELECT
    phenotype_effect.phenotype_id,
    phenotype_effect.phenotype_name
FROM
    phenotype_effect,
    drug_phenotype_effect
WHERE
    drug_phenotype_effect.drug_id = %s
        AND drug_phenotype_effect.phenotype_type = %s
        AND phenotype_effect.phenotype_id = drug_phenotype_effect.phenotype_id
```
*Upon execution in the Python script I provide as a string "SIDE EFFECT", apart from the own query and inputs

    
Query 5A:
```
SELECT
    target_name_pref
FROM
    target
WHERE
    target_type = %s
ORDER BY target_name_pref ASC
LIMIT 20
```

Query 5B:
```
SELECT
    target_organism, COUNT(target_id) AS num_targets
FROM
    target
GROUP BY target_organism
ORDER BY COUNT(target_id) DESC
LIMIT 1
```

Query 6:
```
SELECT
    drug_disease.inferred_score,
    drug.drug_name,
    disease.disease_name
FROM
    drug_disease,
    drug,
    disease
WHERE
    drug_disease.disease_id = disease.disease_id
        AND drug_disease.drug_id = drug.drug_id
        AND drug_disease.inferred_score IS NOT NULL
ORDER BY drug_disease.inferred_score ASC
LIMIT 10

DELETE FROM drug_disease
WHERE
    (drug_disease.drug_id , drug_disease.disease_id) IN (SELECT
        *
    FROM
        (SELECT
            drug_disease.drug_id, drug_disease.disease_id
        FROM
            drug, disease, drug_disease
        
        WHERE
            drug.drug_name = %s
            AND disease.disease_name = %s
            AND drug_disease.drug_id = drug.drug_id
            AND drug_disease.disease_id = disease.disease_id) pepito)
```

Query 7:
```
INSERT INTO disease 
VALUES (%s,%s,%s)


INSERT INTO drug_disease(
SELECT %s, drug.drug_id, 3, NULL, NULL 
FROM drug
WHERE drug.drug_name=%s)
```

Query 8*:
```
UPDATE drug_phenotype_effect
SET score=0
WHERE phenotype_type=%s and score<%s
```
*Upon execution in the Python script I provide as a string "SIDE EFFECT", apart from the own query and inputs

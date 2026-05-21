~) Lab Write-up: SQL Injection (WHERE Clause)

## Overview
This write-up documents the exploitation of an SQL injection vulnerability found within a product category filter. The objective was to manipulate a database query to bypass existing security filters and retrieve data that should remain hidden (unreleased products).

## Vulnerability Analysis
The target application utilizes a vulnerable SQL query structure:
`SELECT * FROM products WHERE category = '[USER_INPUT]' AND released = 1`

By injecting a malicious payload, I was able to alter the logic of the `WHERE` clause.

## The Payload
`Gifts' OR 1=1--`

### Technical Explanation
1. **The Injection:** By inserting `'` (single quote), I terminated the original category string.
2. **Logic Bypass:** The `OR 1=1` statement creates a condition that is always true, effectively overriding the category restriction.
3. **Commentary:** The `--` sequence (SQL comment) renders the remaining part of the original query (`AND released = 1`) inactive.

The resulting query becomes:
`SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1`



## Evidence of Success
The application responded by displaying all products, including those marked as "unreleased," confirming that the logic bypass was successful.

![Lab Success Proof](https://github.com/panjipras36-star/redteam-security-/blob/main/images/Sql_injection1.jpeg?raw=true)

## Remediation
To prevent this vulnerability, the application should:
- Use **Parameterized Queries (Prepared Statements)** to ensure user input is treated as data, not executable code.
- Implement strict input validation and sanitization.
- Adopt a "Defense in Depth" approach for database access.

---
*Disclaimer: This lab was performed in a controlled, educational environment provided by PortSwigger Web Security Academy for ethical hacking training purposes only.*

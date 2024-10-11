import re

def extract_sql_from_query(response: str) -> str:
    """
    Extracts an SQL query from a GPT-4 response formatted with SQL code blocks.

    The expected response format is:
    ```sql
    {SQL query goes here}
    ```

    Args:
        response (str): The full response containing the SQL query.

    Returns:
        str: The extracted SQL query. If no query is found, returns an empty string.
    """
    # Use regex to match SQL code block between ```sql and ```
    match = re.search(r'```sql(.*?)```', response, re.DOTALL)

    if match:
        # Extract the matched content and strip whitespace.
        sql_content = match.group(1).strip()
        # If the content starts with 'SQLQuery:', remove it
        if sql_content.startswith('SQLQuery:'):
            sql_query = sql_content[len('SQLQuery:'):].lstrip()
        else:
            sql_query = sql_content

        return sql_query
    
    # Return an empty string if no match is found
    return ''
from typing import Optional, List, Dict, Any
from datetime import date, datetime
from google.cloud import bigquery, storage


def _jsonify_row(row: dict) -> dict:
    return {
        k: (v.isoformat() if isinstance(v, (date, datetime)) else v)
        for k, v in row.items()
    }


def bigquery_tool(query: str, params: Optional[dict] = None) -> List[Dict[str, Any]]:
    """
    Run a BigQuery SQL query and return results as a list of dicts, using Cloud Run IAM auth.
    """
    try:
        print("Executing BigQuery query...")
        client = bigquery.Client()      # This line: no client secret needed
        job_config = bigquery.QueryJobConfig()
        if params:
            job_config.query_parameters = [
                bigquery.ScalarQueryParameter(k, "STRING", v) for k, v in params.items()
            ]
        print(f"Executing query: {query} with params: {params}")
        query_job = client.query(query, job_config=job_config)
        results = [_jsonify_row(dict(row)) for row in query_job.result()]
        if not results:
            return [{
                "message": "No data found matching your query. Please check your parameters or try again with a different request.",
                "data": []
            }]
        return results
    except Exception as e:
        return [{
            "error": "Query failed to execute",
            "reason": str(e)
        }]

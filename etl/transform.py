import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform(data):
    df = pd.DataFrame(data)
    logging.info("DataFrame created from JSON")

    # Example Transformation: Count posts per user
    agg_df = df.groupby("userId").agg(posts_count=("id", "count")).reset_index()
    logging.info("Aggregation complete: posts per user")

    return agg_df

if __name__ == "__main__":
    from extract import extract
    raw = extract()
    transformed = transform(raw)
    print(transformed.head())


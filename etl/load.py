import logging

logging.basicConfig(level=logging.INFO)

def load(df, path="data/output.csv"):
    df.to_csv(path, index=False)
    logging.info(f"Data written to {path}")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    data = extract()
    transformed = transform(data)
    load(transformed)


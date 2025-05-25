from transform import transform

def test_transform():
    sample_data = [
        {"userId": 1, "id": 1, "title": "title1", "body": "body1"},
        {"userId": 1, "id": 2, "title": "title2", "body": "body2"},
        {"userId": 2, "id": 3, "title": "title3", "body": "body3"}
    ]
    df = transform(sample_data)
    assert "posts_count" in df.columns
    assert df.loc[df["userId"] == 1, "posts_count"].values[0] == 2


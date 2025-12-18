from data_loader import load_csv
from preprocessing import drop_rows_with_missing_values, column_names_to_snake_case
from features import categorize_column, add_word_count_col
from metrics import class_counts, basic_statistical_metrics

def main() -> None:
    """
    Run the full data processing pipeline:
    load data → preprocess → feature engineering → compute metrics.
    """
    cat_col = "emotion"
    str_col = "text"
    data_path = "data/text_emotion.csv"

    data = load_csv(data_path)
    data = drop_rows_with_missing_values(data)
    data = column_names_to_snake_case(data)
    data = categorize_column(data, cat_col)
    data = add_word_count_col(data, str_col)

    counts = class_counts(data, cat_col)
    stats = basic_statistical_metrics(data, "word_count")

    print(data.head())
    print(counts)
    print(stats)


if __name__ == "__main__":
    main()

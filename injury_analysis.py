from transformers import pipeline

def feature_extraction(df):
    sentiment_analyzer = pipeline(
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    )
    ner_model = pipeline("new", aggregation_strategy = "simple")
    df["sebtiment"] = df["Combined"].apply(lambda x: sentiment_analyzer(x)[0]['label'])
    df["ner_entities"] = df["Combined"].apply(ner_model)
    sentiment_map = {"POSITIVE": 1, "NEGATIVE": 0}
    df['sentiment_numeric'] = df['sentiment'].map(sentiment_map)
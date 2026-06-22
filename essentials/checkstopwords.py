from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import TfidfVectorizer

# Ambil daftar stopword bahasa Indonesia dari Sastrawi
stop_factory = StopWordRemoverFactory()
indonesian_stopwords = stop_factory.get_stop_words()

# Buat vectorizer
vectorizer = TfidfVectorizer(stop_words=indonesian_stopwords, max_features=5000)
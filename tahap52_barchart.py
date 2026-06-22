import matplotlib.pyplot as plt

# Data dari hasil evaluasi
labels = ["Prediction Accuracy", "Precision", "Recall", "F1-Score"]
values = [0.33, 0.11, 0.33, 0.17]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, values, color=['#4CAF50', '#2196F3', '#FFC107', '#F44336'])
plt.ylim(0, 1)
plt.title("Evaluasi Prediksi Solusi – TF-IDF + Majority Voting")
plt.ylabel("Score")

# Tambahkan label di atas bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f"{yval:.2f}", ha='center', va='bottom')

plt.tight_layout()
plt.savefig("data/eval/prediction_performance_chart.png")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
response_ids = np.arange(1, 11)

# Non-RAG Model Data
non_rag_response_times = [30, 28, 27, 27, 26, 29, 30, 29, 28, 25]
non_rag_hallucinations = [2, 2, 3, 3, 2, 3, 4, 3, 4, 4]

# RAG Model Data
rag_response_times = [12, 12.5, 11.8, 12.2, 10.9, 14, 13.2, 12.6, 13.9, 14.5]
rag_hallucinations = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]

# Create the figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Response Time for Non-RAG
axs[0, 0].plot(response_ids, non_rag_response_times, marker='o', linestyle='-', color='r', label="Non-RAG Model")
axs[0, 0].set_title("Response Time (Non-RAG)")
axs[0, 0].set_xlabel("Response ID")
axs[0, 0].set_ylabel("Time (seconds)")
axs[0, 0].legend()
axs[0, 0].grid(True)

# Hallucinations for Non-RAG
axs[0, 1].bar(response_ids, non_rag_hallucinations, color='orange', label="Non-RAG Model")
axs[0, 1].set_title("Hallucinations per Response (Non-RAG)")
axs[0, 1].set_xlabel("Response ID")
axs[0, 1].set_ylabel("Number of Hallucinations")
axs[0, 1].legend()

# Response Time for RAG
axs[1, 0].plot(response_ids, rag_response_times, marker='o', linestyle='-', color='g', label="RAG Model")
axs[1, 0].set_title("Response Time (RAG)")
axs[1, 0].set_xlabel("Response ID")
axs[1, 0].set_ylabel("Time (seconds)")
axs[1, 0].legend()
axs[1, 0].grid(True)

# Hallucinations for RAG
axs[1, 1].bar(response_ids, rag_hallucinations, color='blue', label="RAG Model")
axs[1, 1].set_title("Hallucinations per Response (RAG)")
axs[1, 1].set_xlabel("Response ID")
axs[1, 1].set_ylabel("Number of Hallucinations")
axs[1, 1].legend()

# Adjust layout
plt.tight_layout()
plt.show()

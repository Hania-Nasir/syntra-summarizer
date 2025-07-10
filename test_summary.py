from transformers import pipeline

# Create summarizer
summarizer = pipeline("summarization")

# Sample text
text = """
Artificial Intelligence (AI) has rapidly transformed the way businesses operate across various industries. 
From automating customer service with chatbots to enhancing decision-making using data analytics, 
AI tools are becoming essential in daily operations. As companies continue to adopt these technologies, 
it's crucial for them to understand the ethical and strategic implications involved. 
This includes issues like data privacy, transparency, and the need for human oversight in critical tasks.
"""

# Summarize and print
summary = summarizer(text, max_length=60, min_length=25, do_sample=False)
print(summary[0]['summary_text'])

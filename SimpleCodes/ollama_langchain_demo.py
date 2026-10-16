from langchain_ollama import ChatOllama

model = ChatOllama(model="gpt-oss:120b-cloud")
# output = model.invoke("What is the capital of France?")
output = model.invoke("What is multiplication of 12345 and 56789?")
print(output.content)

"""
Output:
The product is  

\[
12345 \times 56789 = 701{,}060{,}205.
\]
"""
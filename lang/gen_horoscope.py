from transformers import pipeline

horo = pipeline('text-generation',model='./gpt2-horo', tokenizer='dbmdz/german-gpt2')

result = horo('Ihre')[0]['generated_text']

print(result)

from transformers import pipeline
import time

horo = pipeline('text-generation',
                model='./gpt2-horo',
                tokenizer='dbmdz/german-gpt2',
              )

result = horo('Ihr Horoskop:', num_return_sequences=3, max_length=50, return_full_text=False)[0]['generated_text']

time_stamp = time.strftime("%d %b %Y %H:%M:%S", time.gmtime())
# result_file = open("generated_horoscopes", "a")
# result_file.write(time_stamp + result)
print(time_stamp + "\t" + result + "\n")

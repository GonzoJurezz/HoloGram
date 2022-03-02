from transformers import pipeline
import time


def gen_horoscope():


    horo = pipeline('text-generation',
                    model='./gpt2-horo',
                    tokenizer='dbmdz/german-gpt2',
                    )

    horo.model.config.pad_token_id = horo.model.config.eos_token_id

    result = horo('Ihr Horoskop für heute ist:', use_auth_token=True, max_length=50, truncation=True, return_full_text=False, )[0]['generated_text']

    time_stamp = time.strftime("%d %b %Y %H:%M:%S", time.gmtime())
    # result_file = open("generated_horoscopes", "a")
    # result_file.write(time_stamp + result)
    return time_stamp + "\t" + result + "\n"


if __name__ == '__main__':
    gen_horoscope()

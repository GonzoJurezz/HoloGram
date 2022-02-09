import os
from transformers import AutoTokenizer
from transformers import DataCollatorForLanguageModeling, TextDataset
#from datasets import load_dataset
from transformers import Trainer, TrainingArguments, AutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained("dbmdz/german-gpt2")
model = AutoModelForCausalLM.from_pretrained("dbmdz/german-gpt2")

train_path = 'train_data.txt'
test_path = 'test_data.txt'

training_args = TrainingArguments(
    output_dir="./gpt2-horo", #The output directory
    overwrite_output_dir=True, #overwrite the content of the output directory
    num_train_epochs=3, # number of training epochs
    per_device_train_batch_size=1,#32, # batch size for training
    per_device_eval_batch_size=1,#64,  # batch size for evaluation
    eval_steps = 400, # Number of update steps between two evaluations.
    save_steps=800, # after # steps model is saved
    warmup_steps=500,# number of warmup steps for learning rate scheduler
    prediction_loss_only=True,
    optim='adamw_torch'
)


def main():

    #TODO: use load_dataset instead of depricated TextDataset

    # dataset = load_dataset('text', data_files={'train': train_path,
    #                                            'test': test_path})

    # _dataset = dataset
    # dataset = dataset['train']
    # print("dataset[0]                 "+str(dataset[0]             ))
    # print("dataset.shape              "+str(dataset.shape          ))
    # print("dataset.num_columns        "+str(dataset.num_columns  ))
    # print("dataset.num_rows           "+str(dataset.num_rows    ))
    # print("len(dataset)               "+str(len(dataset)        ))
    # print("dataset.column_names       "+str(dataset.column_names ))
    # print("dataset.features           "+str(dataset.features    ))

    # dataset = _dataset



    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=train_path,
        block_size=16)

    test_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=test_path,
        block_size=16)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        # train_dataset=dataset['train'],
        # eval_dataset=dataset['test'],
        train_dataset=train_dataset,
        eval_dataset=test_dataset
    )

    trainer.train()
    trainer.save_model()


if __name__ == '__main__':
    main()

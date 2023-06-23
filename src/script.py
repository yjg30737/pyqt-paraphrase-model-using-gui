import torch
from huggingface_hub import scan_cache_dir
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model_name = 'tuner007/pegasus_paraphrase'

def get_response(num_beams, num_return_sequences, context):
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

    batch = tokenizer([context],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
    translated = model.generate(**batch,max_length=60,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1.5)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text

def is_model_exists():
    cache_dir_result = scan_cache_dir()
    for i in cache_dir_result.repos:
        if model_name == i.repo_id:
            return True
    return False

def remove_model():
    commit_hashes = []
    cache_dir_result = scan_cache_dir()
    for i in cache_dir_result.repos:
        if model_name == i.repo_id:
            for j in i.revisions:
                commit_hashes.append(j.commit_hash)
    delete_strategy = cache_dir_result.delete_revisions(*commit_hashes)
    print("Will free " + delete_strategy.expected_freed_size_str)
    delete_strategy.execute()

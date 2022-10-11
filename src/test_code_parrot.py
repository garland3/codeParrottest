# %%

# from transformers import AutoTokenizer, AutoModelWithLMHead
  
# tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
# model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")

# inputs = tokenizer("def hello_world():", return_tensors="pt")
# outputs = model(**inputs)

# # %%
# outputs

# # %%

# p = tokenizer.decode
# # %%

# # preds = tokenizer.batch_decode(outputs, skip_special_tokens=True)

# preds = [pred.strip() for pred in preds]
# %%


from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
from transformers import pipeline
# %%
model_ckpt = "codeparrot/codeparrot"
model = AutoModelForCausalLM.from_pretrained(model_ckpt, low_cpu_mem_usage=True)
# %%
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
# %%
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# %%
gen_prompt =r"""from pathlib import Path
def get_folders(path):"""
gen_kwargs = {}
# gen_kwargs["do_sample"]='Sample'
# gen_kwargs["max_new_tokens"]=256
# gen_kwargs["temperature"]=0.1
# gen_kwargs["top_k"] =0
# gen_kwargs["top_p"] =0
# gen_kwargs["pad_token_id"] ='eos_token_id'

generated_text = pipe(gen_prompt, **gen_kwargs)[0]['generated_text']
# %%
generated_text
# %%

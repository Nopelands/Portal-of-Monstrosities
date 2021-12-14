# remember to
# pip install tensorflow
# pip install transformers

from transformers import GPTJForCausalLM, AutoTokenizer
import tensorflow

model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", revision="float16", torch_dtype=tf.float16, low_cpu_mem_usage=True)
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
context = "This is a test"

input_ids = tokenizer(context, return_tensors="pt").input_ids
gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=100,)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)
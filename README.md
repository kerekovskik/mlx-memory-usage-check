# install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

# Run LLM Genereation without Cache Limit

This is the default behavior of mlx_lm. Notice the high cache memory usage. MLX Cache is set to 0 by default, which means unlimited so MLX will use as much memory as it can get.

```
python3  memory_check.py --input 3blue1brown_attention.txt --output response.txt --model /Users/kerekovskik/hf/Meta-Llama-3-8B-Instruct-MLX --cache-limit 0
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
MLX Memory Pre-Generation: 15316.51 MB
MLX Cache Memory Pre-Generation: 0.00 MB
MLX Total Memory Pre-Generation: 15316.51 MB
MLX Memory Post-Generation: 16150.47 MB
MLX Cache Memory Post-Generation: 53876.89 MB
MLX Total Memory Post-Generation: 70027.36 MB
Input Tokens: 7522
Peak MLX Memory: 29326.617294311523 MB
```

# Run LLM Generation Without Cache Limit 

Memory usage is successfully controlled by setting a cache limit for MLX. The program does end with a non-0 return code because of some issue that occurs after token generation is complete.

```
python3  memory_check.py --input 3blue1brown_attention.txt --output response.txt --model /Users/kerekovskik/hf/Meta-Llama-3-8B-Instruct-MLX --cache-limit 1
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
MLX Memory Pre-Generation: 15316.51 MB
MLX Cache Memory Pre-Generation: 0.00 MB
MLX Total Memory Pre-Generation: 15316.51 MB
MLX Memory Post-Generation: 16358.98 MB
MLX Cache Memory Post-Generation: 1024.51 MB
MLX Total Memory Post-Generation: 17383.49 MB
Input Tokens: 7522
Peak MLX Memory: 29326.617294311523 MB
libc++abi: terminating due to uncaught exception of type std::__1::system_error: mutex lock failed: Invalid argument
zsh: abort      python3 memory_check.py --input 3blue1brown_attention.txt --output  --model  
```
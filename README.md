# install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

# Run LLM Generation WITHOUT Cache Limit

This is the default behavior of MLX. Notice the high cache memory usage. MLX Cache is set to 0 by default, which unfortunately results in MLX gobbling up all available memory on my machine. Documentation reference: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.metal.set_cache_limit.html

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

During the course of generating a response, it reserved ~53GB of memory in the MLX cache.

# Run LLM Generation WITH Cache Limit 

Memory usage is successfully controlled by setting a cache limit for MLX.  

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
```

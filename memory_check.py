import mlx_lm
import argparse
import mlx


def main(args):
    model, tokenizer = mlx_lm.load(
        args.model,
        tokenizer_config={"trust_remote_code": True}
    )

    prompt = open(args.input, 'r').read()
    
    if args.cache_limit > 0:
        cache_limit_gb = args.cache_limit * 1024 * 1024 * 1024
        mlx.core.metal.set_cache_limit(cache_limit_gb)

    chat = [
       {"role": "system", "content": "You are a sophisticated AI model who assists the user with all tasks."},
       {"role": "user", "content": prompt},
    ]

    prompt_tokenized = tokenizer.apply_chat_template(chat, tokenize=True)
    input_tokens = len(prompt_tokenized)
    
    parsed_chat = tokenizer.apply_chat_template(chat, tokenize=False)

    max_output_tokens = 8192 - input_tokens

    mlx_memory_pre_gen_mb = mlx.core.metal.get_active_memory()/1024/1024
    mlx_cache_memory_pre_gen_mb = mlx.core.metal.get_cache_memory()/1024/1024
    total_mem_pregen_mb = mlx_memory_pre_gen_mb + mlx_cache_memory_pre_gen_mb
    response = mlx_lm.generate(model, tokenizer, prompt=parsed_chat, verbose=False, temp=args.temp, max_tokens=max_output_tokens)
    mlx_memory_post_gen_mb = mlx.core.metal.get_active_memory()/1024/1024
    mlx_cache_memory_post_gen_mb = mlx.core.metal.get_cache_memory()/1024/1024
    total_mem_postgen_mb = mlx_memory_post_gen_mb + mlx_cache_memory_post_gen_mb
    peak_memory = mlx.core.metal.get_peak_memory()/1024/1024
    open(args.output, 'w').write(response)
    
    print(f"MLX Memory Pre-Generation: {mlx_memory_pre_gen_mb:.2f} MB")
    print(f"MLX Cache Memory Pre-Generation: {mlx_cache_memory_pre_gen_mb:.2f} MB")
    print(f"MLX Total Memory Pre-Generation: {total_mem_pregen_mb:.2f} MB")
    print(f"MLX Memory Post-Generation: {mlx_memory_post_gen_mb:.2f} MB")
    print(f"MLX Cache Memory Post-Generation: {mlx_cache_memory_post_gen_mb:.2f} MB")
    print(f"MLX Total Memory Post-Generation: {total_mem_postgen_mb:.2f} MB")
    print(f"Input Tokens: {input_tokens}")
    print(f"Peak MLX Memory: {peak_memory} MB")
    

def build_args():
    parser = argparse.ArgumentParser(description='Memory Check')
    parser.add_argument('--model', type=str, help='Model Path', required=True)
    parser.add_argument('--input', type=str, help='Path to file containing prompt.', required=True)
    parser.add_argument('--output', type=str, help='Path to file to write output to.', required=True)
    parser.add_argument('--trust_remote_code', help='Trust remote code', action='store_true')
    parser.add_argument('--cache-limit', type=int, help='MLX Cache limit (GB)', default=0)
    parser.add_argument('--temp', type=float, help='Temperature', default=0.5)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main(build_args())



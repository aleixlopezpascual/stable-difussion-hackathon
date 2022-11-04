# Run the model
python3 scripts/txt2img.py \
--prompt 'A photorealistc bowl of edamame award winning gourmet photography' \
--outdir ../outputs/award_wining_edamame/ \
--H 512 --W 512 \
--n_samples 4 \
--config configs/stable-diffusion/glovo.yaml \
--ckpt logs/2022-10-06T00-41-26_glovo/checkpoints/last.ckpt



from stable_diffusion_videos.stable_diffusion_walk import walk

prompts = [
    "Uramaki De Salmon Y Aguacate Masago",
    "Gyozas de Verduras",
    "Edamame",
    "Futomaki de langostino en tempura",
    "Nigiris de salmón",
    "4 makis de salmón picante"
]

prompt_n_seed = {
    "Uramaki De Salmon Y Aguacate Masago": 743,
    "Gyozas de Verduras": 140,
    "Edamame": 40,
    "Futomaki de langostino en tempura": 560,
    "Nigiris de salmón": 996,
    "4 makis de salmón picante": 283,
}


walk(prompts=list(prompt_n_seed.keys()), 
     seeds=list(prompt_n_seed.values()),
     make_video=True, 
     name="asianevolution",
     num_steps=200,
     use_lerp_for_text=True,
     upscale=True
     )
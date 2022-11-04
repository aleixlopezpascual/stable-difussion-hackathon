from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

class opt:
    pass

opt.from_file = "scripts/david/prompts_file.txt"
#opt.from_file = False
#opt.prompt = "Edamame"
batch_size = 4

if not opt.from_file:
        prompt = opt.prompt
        assert prompt is not None
        data = [batch_size * [prompt]]

else:
    print(f"reading prompts from {opt.from_file}")
    with open(opt.from_file, "r") as f:
        data = f.read().splitlines()
        #data = list(chunk(data, batch_size))
        data = [batch_size * [xx] for xx in data]

data = [list(xx) for xx in data]
print(data)
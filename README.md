# JOJO-ArgumentParser
Make python built-in library "argparse" easier!

# Quickstart 

Take following code as an example: 

```python
from dataclasses import dataclass 
import jojo_argparse 


@dataclass 
class Config:
    lr: float = 0.001  # default value
    batch_size: int = 64 
    num_epochs: int = 100 
    
    
config = jojo_argparse.parse_args(Config) 
print(config.lr, config.batch_size, config.num_epochs)
```

Then you can run the code with arguments: 

```bash
python example.py --lr 0.05 --batch_size 1024 
```

The output will be: 

```
0.05 1024 100
```
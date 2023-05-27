from dataclasses import dataclass 
import jojo_argparse 


@dataclass 
class Config:
    lr: float = 0.001  # default value
    batch_size: int = 64 
    num_epochs: int = 100 
    
    
config = jojo_argparse.parse_args(Config) 
print(config.lr, config.batch_size, config.num_epochs)

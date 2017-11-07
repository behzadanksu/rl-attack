# Crafting Adversarial Example Attacks on Policy Learners 


Based on OpenAI Baselines.

### Dependencies
- Python 3
- cleverhans v2.0.0

```
pip install -e git+http://github.com/tensorflow/cleverhans.git#egg=cleverhans
```

- others (e.g., gym, baselines, ...)

```
git clone https://github.com/behzadanksu/rl-attack.git
cd rl-attack
pip install -e .
```

### Examples
Test time attack:

```
python3 -m baselines.deepq.experiments.atari.enjoy-adv --model-dir ./data/enduro-p-1/model-4000 --env Enduro --attack fgsm --video ./p1.mp4
```

Training time attack - no parameter noise:

```
python3 -m baselines.deepq.experiments.atari.train --save-dir ./data/endure-nop-1 --env Enduro --save-freq 1e5 --attack fgsm --attack-init 1e6 --attack-freq 1
```

Training time attack - with parameter noise:

```
python3 -m baselines.deepq.experiments.atari.train --save-dir ./data/endure-nop-1 --env Enduro --save-freq 1e5 --param-noise --attack fgsm --attack-init 1e6 --attack-freq 1
```


# Crafting Adversarial Example Attacks on Policy Learners 


Framework for experimental analysis of adversarial example attacks on policy learning in Deep RL. Attack methodologies are based on our paper "Vulnerability of Deep Reinforcement Learning to Policy Induction Attacks" (Behzadan & Munir, 2017 - https://arxiv.org/abs/1701.04143 ).  

This project provides an interface between OpenAI's RL Baselines and the Cleverhans framework for crafting adversarial examples. We would also like to thank Yen-Chen Lin et al.'s work on `RL-Attack-Detection <https://github.com/yenchenlin/rl-attack-detection>` for inspiring simpler solutions to test-time attacks.

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
Current version includes only DQN attacks.

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


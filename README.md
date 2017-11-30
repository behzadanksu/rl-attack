# Crafting Adversarial Example Attacks on Policy Learners 


Framework for experimental analysis of adversarial example attacks on policy learning in Deep RL. Attack methodologies are based on our paper "Vulnerability of Deep Reinforcement Learning to Policy Induction Attacks" (Behzadan & Munir, 2017 - https://arxiv.org/abs/1701.04143 ).  

This project provides an interface between [@openai/baselines](https://github.com/openai/baselines) and [@tensorflow/cleverhans](https://github.com/tensorflow/cleverhans) to facilitate the crafting and implementation of adversarial example attacks on deep RL algorithms. We would also like to thank [@andrewliao11/NoisyNet-DQN](https://github.com/andrewliao11/NoisyNet-DQN) for inspiring solutions to implementing the [NoisyNet](https://arxiv.org/abs/1706.10295) algorithm for DQN.

### Dependencies
- Python 3
- cleverhans v2.0.0

```
pip install -e git+http://github.com/tensorflow/cleverhans.git#egg=cleverhans
```

- others (e.g., gym, ...)

```
git clone https://github.com/behzadanksu/rl-attack.git
cd rl-attack
pip install -e .
```

### Examples
Current version includes only DQN attacks.

Test-time, No attack, testing a DQN model of Breakout trained without parameter noise:

```
$> python3 enjoy-adv.py --env Breakout --model-dir ./data/Breakout/model-173000 --video ./Breakout.mp4
```

Test-time, No attack, testing a DQN model of Breakout trained with parameter noise (NoisyNet implementation):
```
$> python3 enjoy-adv.py --env Breakout --noisy --model-dir ./data/Breakout/model-173000 --video ./Breakout.mp4
```

Test-time, Whitebox FGSM attack, testing a DQN model of Breakout trained without parameter noise:
```
$> python3 enjoy-adv.py --env Breakout --model-dir ./data/Breakout/model-173000 --attack fgsm --video ./Breakout.mp4
```

Test-time, Whitebox FGSM attack, testing a DQN model of Breakout trained with parameter noise (NoisyNet implementation):
```
$> python3 enjoy-adv.py --env Breakout --noisy --model-dir ./data/Breakout/model-173000 --attack fgsm --video ./Breakout.mp4
```

Test-time, Blackbox FGSM attack, testing a DQN model of Breakout trained without parameter noise:
```
$> python3 enjoy-adv.py --env Breakout --model-dir ./data/Breakout/model-173000 --attack fgsm --blackbox --model-dir2 ./data/Breakout/model-173000-2 --video ./Breakout.mp4
```

Test-time, Blackbox FGSM attack, testing a DQN model of Breakout trained with parameter noise (NoisyNet implementation), replica model trained without parameter noise:
```
$> python3 enjoy-adv.py --env Breakout --noisy --model-dir ./data/Breakout/model-173000 --attack fgsm --blackbox --model-dir2 ./data/Breakout/model-173000-2 --video ./Breakout.mp4
```

Test-time, Blackbox FGSM attack, testing a DQN model of Breakout trained with parameter noise (NoisyNet implementation), replica model trained with parameter noise:
```
$> python3 enjoy-adv.py --env Breakout --noisy --model-dir ./data/Breakout/model-173000 --attack fgsm --blackbox --model-dir2 ./data/Breakout/model-173000-2 --noisy2 --video ./Breakout.mp4
```

Training-time, Whitebox attack, no parameter noise, injecting adversarial exam at every 2 step:

```
$> python3 train.py --env Breakout --save-dir ./data/Breakout/ --attack fgsm --num-steps 200000000 --attack-freq 2 
```

Training-time, Whitebox attack, NoisyNet parameter noise, injecting adversarial exam at every 1 step:

```
$> python3 train.py --env Breakout --noisy --save-dir ./data/Breakout/ --attack fgsm --num-steps 200000000 --attack-freq 1
```

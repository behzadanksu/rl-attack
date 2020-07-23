import tensorflow.compat.v1 as tf
import tensorflow.contrib.layers as layers
from rlattack.common.tf_util import noisy_dense
from cleverhans.model import Model

class model(Model):
    def __init__(self, img_in, nb_classes, scope, noisy=False, reuse=False, concat_softmax=False, **kwargs):
        del kwargs
        self.scope = scope
        self.num_actions = nb_classes
        self.noisy = noisy
        #self.reuse = reuse
        self.reuse = tf.AUTO_REUSE
        self.concat_softmax = concat_softmax
        #self.img_in = img_in
        Model.__init__(self, scope, nb_classes, locals())

        #self.fprop(tf.placeholder(tf.float32, [128, 28, 28, 1]))
        #self.fprop (img_in)
        #self.needs_dummy_fprop = True
        self.fprop (img_in)
        train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.scope+"/convnet")
        train_vars += tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.scope+"/action_value")
        self.params = train_vars
        #self.params = self.get_params()

    def fprop(self, img_in, **kwargs):
        del kwargs
        #def model(img_in, num_actions, scope, noisy=False, reuse=False, concat_softmax=False):
        """As described in https://storage.googleapis.com/deepmind-data/assets/papers/DeepMindNature14236Paper.pdf"""
        with tf.variable_scope(self.scope, reuse=self.reuse):
            out = img_in
            with tf.variable_scope("convnet"):
                # original architecture
                out = layers.convolution2d(out, num_outputs=32, kernel_size=8, stride=4, activation_fn=tf.nn.relu)
                out = layers.convolution2d(out, num_outputs=64, kernel_size=4, stride=2, activation_fn=tf.nn.relu)
                out = layers.convolution2d(out, num_outputs=64, kernel_size=3, stride=1, activation_fn=tf.nn.relu)
            out = layers.flatten(out)

            with tf.variable_scope("action_value"):
                if self.noisy:
                    # Apply noisy network on fully connected layers
                    # ref: https://arxiv.org/abs/1706.10295
                    out = noisy_dense(out, name='noisy_fc1', size=512, activation_fn=tf.nn.relu)
                    out = noisy_dense(out, name='noisy_fc2', size=self.num_actions)
                else:
                    out = layers.fully_connected(out, num_outputs=512, activation_fn=tf.nn.relu)
                    out = layers.fully_connected(out, num_outputs=self.num_actions, activation_fn=None)
                #V: Softmax - inspired by deep-rl-attack #
                #if concat_softmax:
                #prob = tf.nn.softmax(out)
            #return out
            return {self.O_LOGITS: out, self.O_PROBS: tf.nn.softmax(logits=out)}


def dueling_model(img_in, num_actions, scope, noisy=False, reuse=False, concat_softmax=False):
    """As described in https://arxiv.org/abs/1511.06581"""
    with tf.variable_scope(scope, reuse=reuse):
        out = img_in
        with tf.variable_scope("convnet"):
            # original architecture
            out = layers.convolution2d(out, num_outputs=32, kernel_size=8, stride=4, activation_fn=tf.nn.relu)
            out = layers.convolution2d(out, num_outputs=64, kernel_size=4, stride=2, activation_fn=tf.nn.relu)
            out = layers.convolution2d(out, num_outputs=64, kernel_size=3, stride=1, activation_fn=tf.nn.relu)
        out = layers.flatten(out)

        with tf.variable_scope("state_value"):
            if noisy:
                # Apply noisy network on fully connected layers
                # ref: https://arxiv.org/abs/1706.10295
                state_hidden = noisy_dense(out, name='noisy_fc1', size=512, activation_fn=tf.nn.relu)
                state_score = noisy_dense(state_hidden, name='noisy_fc2', size=1)
            else:
                state_hidden = layers.fully_connected(out, num_outputs=512, activation_fn=tf.nn.relu)
                state_score = layers.fully_connected(state_hidden, num_outputs=1, activation_fn=None)
        with tf.variable_scope("action_value"):
            if noisy:
                # Apply noisy network on fully connected layers
                # ref: https://arxiv.org/abs/1706.10295
                actions_hidden = noisy_dense(out, name='noisy_fc1', size=512, activation_fn=tf.nn.relu)
                action_scores = noisy_dense(actions_hidden, name='noisy_fc2', size=num_actions)
            else:
                actions_hidden = layers.fully_connected(out, num_outputs=512, activation_fn=tf.nn.relu)
                action_scores = layers.fully_connected(actions_hidden, num_outputs=num_actions, activation_fn=None)
            action_scores_mean = tf.reduce_mean(action_scores, 1)
            action_scores = action_scores - tf.expand_dims(action_scores_mean, 1)

        return state_score + action_scores

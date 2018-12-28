import logging

from rasa_core.policies.keras_policy import KerasPolicy
from policy.attention_keras import Attention, Position_Embedding
from keras.models import Model, load_model
from keras.layers import *

from typing import Text, Any
import json
import os
from rasa_core import utils
import tensorflow as tf
import io
from rasa_core.featurizers import TrackerFeaturizer

try:
    import cPickle as pickle
except ImportError:
    import pickle


logger = logging.getLogger(__name__)

class AttentionPolicy(KerasPolicy):
    def model_architecture(self, input_shape, output_shape):
        S_inputs = Input(shape=input_shape)

        embeddings = Position_Embedding()(S_inputs)
        """
            nb_head = 8 超参可设定
            size_per_head = 16 超参可设定
        """
        O_seq = Attention(16, 64)([embeddings, embeddings, embeddings])
        O_seq = GlobalAveragePooling1D()(O_seq)
        O_seq = Dropout(0.5)(O_seq)
        outputs = Dense(units=output_shape[-1], activation='softmax')(O_seq)

        model = Model(inputs=S_inputs, outputs=outputs)

        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        logger.debug(model.summary())
        return model

    @classmethod
    def load(cls, path: Text) -> 'KerasPolicy':
        from keras.models import load_model

        if os.path.exists(path):
            featurizer = TrackerFeaturizer.load(path)
            meta_path = os.path.join(path, "keras_policy.json")
            if os.path.isfile(meta_path):
                meta = json.loads(utils.read_file(meta_path))
                model_file = os.path.join(path, meta["model"])

                graph = tf.Graph()
                with graph.as_default():
                    session = tf.Session()
                    with session.as_default():
                        model = load_model(model_file,  custom_objects={
                            'Position_Embedding': Position_Embedding,
                            'Attention': Attention})

                return cls(featurizer=featurizer,
                           model=model,
                           graph=graph,
                           session=session,
                           current_epoch=meta["epochs"])
            else:
                return cls(featurizer=featurizer)
        else:
            raise Exception("Failed to load dialogue model. Path {} "
                            "doesn't exist".format(os.path.abspath(path)))

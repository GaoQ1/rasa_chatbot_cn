import logging

from typing import Text, Any
import json
import os
import tensorflow as tf
import warnings

from rasa.core.policies.keras_policy import KerasPolicy
import rasa.utils.io
from rasa.core import utils
from rasa.core.featurizers import TrackerFeaturizer

from .attention_keras import Attention, Position_Embedding

try:
    import cPickle as pickle
except ImportError:
    import pickle


logger = logging.getLogger(__name__)

class AttentionPolicy(KerasPolicy):
    def model_architecture(self, input_shape, output_shape):
        from keras.models import Model, load_model
        from keras.layers import Input, GlobalAveragePooling1D, Dropout, Dense

        S_inputs = Input(shape=input_shape)

        embeddings = S_inputs
        # embeddings = Position_Embedding()(S_inputs)
        """
            nb_head = 8 超参可设定
            size_per_head = 16 超参可设定
        """
        O_seq = Attention(16, 64)([embeddings, embeddings, embeddings])
        O_seq = Attention(16, 64)([O_seq, O_seq, O_seq])
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
    def load(cls, path: Text) -> "KerasPolicy":
        from keras.models import load_model

        if os.path.exists(path):
            featurizer = TrackerFeaturizer.load(path)
            meta_file = os.path.join(path, "keras_policy.json")
            if os.path.isfile(meta_file):
                meta = json.loads(rasa.utils.io.read_file(meta_file))

                tf_config_file = os.path.join(path, "keras_policy.tf_config.pkl")
                with open(tf_config_file, "rb") as f:
                    _tf_config = pickle.load(f)

                model_file = os.path.join(path, meta["model"])

                graph = tf.Graph()
                with graph.as_default():
                    session = tf.Session(config=_tf_config)
                    with session.as_default():
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            model = load_model(model_file, custom_objects={
                                'Position_Embedding': Position_Embedding,
                                'Attention': Attention})

                return cls(
                    featurizer=featurizer,
                    priority=meta["priority"],
                    model=model,
                    graph=graph,
                    session=session,
                    current_epoch=meta["epochs"],
                )
            else:
                return cls(featurizer=featurizer)
        else:
            raise Exception(
                "Failed to load dialogue model. Path {} "
                "doesn't exist".format(os.path.abspath(path))
            )

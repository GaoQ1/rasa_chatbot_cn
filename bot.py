from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy.mobile_policy import MobilePolicy
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy

from rasa_core.policies.embedding_policy import EmbeddingPolicy

logger = logging.getLogger(__name__)


def train_dialogue_keras(domain_file="mobile_domain.yml",
                   model_path="models/dialogue_keras",
                   training_data_file="data/mobile_edit_story.md"):

    fallback = FallbackPolicy(
        fallback_action_name="action_default_fallback",
        nlu_threshold=0.5,
        core_threshold=0.3
    )
    
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5),
                            MobilePolicy(), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=100,
            batch_size=16,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent

def train_dialogue_embed(domain_file="mobile_domain.yml",
                   model_path="models/dialogue_embed",
                   training_data_file="data/mobile_edit_story.md"):

    fallback = FallbackPolicy(
        fallback_action_name="action_default_fallback",
        nlu_threshold=0.5,
        core_threshold=0.3
    )
    
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5),
                            EmbeddingPolicy(epochs=100), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/rasa_dataset_training.json')
    trainer = Trainer(config.load("configs/nlu_embedding_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory


def train_nlu_gao():
    from rasa_nlu_gao.training_data import load_data
    from rasa_nlu_gao import config
    from rasa_nlu_gao.model import Trainer

    training_data = load_data('data/rasa_dataset_training.json')
    trainer = Trainer(config.load("configs/config_embedding_bilstm.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu_gao/',
                                      fixed_model_name="current")

    return model_directory


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue-keras", "train-dialogue-embed", "train-nlu-gao"],
            help="what the bot should do ?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-nlu-gao":
        train_nlu_gao()
    elif task == "train-dialogue-keras":
        train_dialogue_keras()
    elif task == "train-dialogue-embed":
        train_dialogue_embed()

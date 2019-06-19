from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import warnings

from builtins import str
from typing import Any
from typing import Dict
from typing import Optional
from typing import Text

from rasa.nlu import utils
from rasa.nlu.extractors import EntityExtractor
from rasa.nlu.model import Metadata
from rasa.nlu.training_data import Message
from rasa.nlu.training_data import TrainingData
from rasa.nlu.utils import write_json_to_file
import itertools


class JiebaPsegExtractor(EntityExtractor):

    provides = ["entities"]

    defaults = {
        # nr：人名，ns：地名，nt：机构名, m: numbers
        "part_of_speech": ['nr']
    }

    def __init__(self, component_config=None):
        # type: (Optional[Dict[Text, Text]]) -> None

        super(JiebaPsegExtractor, self).__init__(component_config)

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None
        extracted = self.add_extractor_name(self.posseg_cut_examples(message))

        message.set("entities", extracted, add_to_output=True)

    def posseg_cut_examples(self, example):
        raw_entities = example.get("entities", [])
        example_posseg = self.posseg(example.text)

        for (item_posseg, start, end) in example_posseg:
            part_of_speech = self.component_config["part_of_speech"]
            for (word_posseg, flag_posseg) in item_posseg:
                if flag_posseg in part_of_speech:
                    raw_entities.append({
                        'start': start,
                        'end': end,
                        'value': word_posseg,
                        'entity': flag_posseg
                    })
        return raw_entities

    @staticmethod
    def posseg(text):
        # type: (Text) -> List[Token]

        import jieba
        import jieba.posseg as pseg

        result = []
        for (word, start, end) in jieba.tokenize(text):
            pseg_data = [(w, f) for (w, f) in pseg.cut(word)]
            result.append((pseg_data, start, end))

        return result

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir=None,  # type: Optional[Text]
             model_metadata=None,  # type: Optional[Metadata]
             cached_component=None,  # type: Optional[Component]
             **kwargs  # type:**Any
             ):

        return cls(meta)

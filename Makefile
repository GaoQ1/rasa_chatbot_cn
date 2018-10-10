help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run"
	@echo "        Runs the bot on the command line."
	@echo "    run-api"
	@echo "        Runs the bot as a server."

run:
	make run-actions&
	make run-core

run-api:
	make run-actions&
	make run-http

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

run-core:
	python -m rasa_core.run --nlu models/nlu/default/current --core models/dialogue --endpoints endpoints.yml

run-online:
	python -m rasa_core.train --online -o models/dialogue -d mobile_domain.yml -s data/mobile_edit_story.md --endpoints endpoints.yml

run-http:
	python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current --endpoints endpoints.yml --auth_token gaoquan

run-nlu-server:
	python -m rasa_nlu.server -c nlu_model_config.yml --path models/nlu/

evaluate:
	python -m rasa_core.evaluate -d models/dialogue -s data/mobile_edit_story.md

visualize:
	python -m rasa_core.visualize -s data/mobile_edit_story.md -d mobile_domain.yml -o story_graph.png

train-nlu:
	python bot.py train-nlu

train-core:
	python bot.py train-dialogue

train-nlu-gao:
	python bot.py train-nlu-gao

run-nlu-gao-server:
	python -m rasa_nlu_gao.server -c config_embedding_bilstm.yml --path models/nlu_gao/
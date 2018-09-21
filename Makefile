help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run"
	@echo "        Runs the bot on the command line."

run:
	make run-actions&
	make run-core


run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

run-core:
	python -m rasa_core.run --nlu models/nlu/default/current --core models/dialogue --endpoints endpoints.yml

run-online:
	python -m rasa_core.train --online -o models/dialogue -d mobile_domain.yml -s data/mobile_edit_story.md --endpoints endpoints.yml

run-http:
	python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current --endpoints endpoints.yml -o out.log --auth_token gaoquan

run-nlu-server:
	python -m rasa_nlu.server -c nlu_model_config.yml --path models/nlu/


train-nlu:
	python bot.py train-nlu

train-core:
	python bot.py train-dialogue


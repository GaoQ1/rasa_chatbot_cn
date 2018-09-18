## make command

1. run:
	make run-actions&
	make run-core

2. run-online:
	make run-actions&
	make run-online

3. run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

4. run-core:
	python -m rasa_core.run --nlu models/nlu/default/current --core models/dialogue --endpoints endpoints.yml

5. run-online:
	python -m rasa_core.train --online -o models/dialogue -d mobile_domain.yml -s data/mobile_story.md --endpoints endpoints.yml

6. train-nlu:
	python bot.py train-nlu

7. train-core:
	python bot.py train-dialogue


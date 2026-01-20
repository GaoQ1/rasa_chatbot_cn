"""
Shared pytest fixtures and configuration for all tests.
"""
import os
import tempfile
from pathlib import Path
from typing import Generator, Dict, Any
import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """Provide a mock configuration dictionary."""
    return {
        "language": "en",
        "pipeline": ["WhitespaceTokenizer", "RegexFeaturizer", "DIETClassifier"],
        "policies": ["MemoizationPolicy", "TEDPolicy"],
        "version": "1.0.0",
    }


@pytest.fixture
def mock_rasa_domain() -> Dict[str, Any]:
    """Provide a mock Rasa domain configuration."""
    return {
        "intents": ["greet", "goodbye", "affirm", "deny"],
        "entities": ["name", "location"],
        "slots": {
            "name": {"type": "text"},
            "location": {"type": "text"},
        },
        "responses": {
            "utter_greet": [{"text": "Hello! How can I help you?"}],
            "utter_goodbye": [{"text": "Goodbye!"}],
        },
        "actions": ["action_hello_world", "action_search"],
    }


@pytest.fixture
def mock_tracker():
    """Provide a mock Rasa conversation tracker."""
    tracker = Mock()
    tracker.sender_id = "test_user"
    tracker.slots = {"name": None, "location": None}
    tracker.latest_message = {
        "text": "Hello",
        "intent": {"name": "greet", "confidence": 0.9},
        "entities": [],
    }
    tracker.events = []
    tracker.active_form = None
    tracker.latest_action = {"action_name": "action_listen"}
    
    # Add methods that might be called
    tracker.get_slot = Mock(side_effect=lambda slot: tracker.slots.get(slot))
    tracker.get_latest_input_channel = Mock(return_value="rest")
    
    return tracker


@pytest.fixture
def mock_dispatcher():
    """Provide a mock Rasa dispatcher for sending messages."""
    dispatcher = Mock()
    dispatcher.messages = []
    dispatcher.utter_message = Mock(
        side_effect=lambda text=None, **kwargs: dispatcher.messages.append(
            {"text": text, **kwargs}
        )
    )
    return dispatcher


@pytest.fixture
def mock_domain():
    """Provide a mock domain object."""
    domain = Mock()
    domain.slots = ["name", "location"]
    domain.entities = ["name", "location"]
    domain.intents = ["greet", "goodbye", "affirm", "deny"]
    return domain


@pytest.fixture
def sample_nlu_data() -> Dict[str, Any]:
    """Provide sample NLU training data."""
    return {
        "version": "2.0",
        "nlu": [
            {
                "intent": "greet",
                "examples": [
                    {"text": "hello"},
                    {"text": "hi"},
                    {"text": "hey there"},
                ],
            },
            {
                "intent": "goodbye",
                "examples": [
                    {"text": "bye"},
                    {"text": "goodbye"},
                    {"text": "see you later"},
                ],
            },
        ],
    }


@pytest.fixture
def sample_stories_data() -> str:
    """Provide sample stories training data."""
    return """
## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
"""


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    # Store original environment
    original_env = os.environ.copy()
    
    # Yield control to the test
    yield
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def mock_action_server_response():
    """Mock response from Rasa action server."""
    return {
        "events": [],
        "responses": [{"text": "Action executed successfully"}],
    }


# Add markers for test categorization
def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "slow: Tests that take a long time to run")
"""Unit tests for WinCLIP's compositional prompt ensemble."""

from anomalib.models.image.winclip.prompting import create_prompt_ensemble


class TestCreatePromptEnsemble:
    """Test the create_prompt_ensemble function."""

    def test_length(self) -> None:
        """Test if the correct number of normal and anomalous prompts are created."""
        normal_prompts, anomalous_prompts = create_prompt_ensemble("object")
        assert len(normal_prompts) == 147
        assert len(anomalous_prompts) == 84

    def test_class_name_in_every_prompt(self) -> None:
        """Test prompt ensemble creation."""
        normal_prompts, anomalous_prompts = create_prompt_ensemble("item")
        assert all("item" in prompt for prompt in normal_prompts)
        assert all("item" in prompt for prompt in anomalous_prompts)

    def test_called_without_class_name(self) -> None:
        """Test prompt ensemble creation without class name."""
        normal_prompts, anomalous_prompts = create_prompt_ensemble()
        assert all("object" in prompt for prompt in normal_prompts)
        assert all("object" in prompt for prompt in anomalous_prompts)

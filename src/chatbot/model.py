import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class DialoGPTChatbot:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
        self.chat_history_ids = torch.tensor([])
        self.first_input = True

    def get_response(self, user_input: str) -> str:
        new_user_input_ids = self.tokenizer.encode(
            user_input + self.tokenizer.eos_token, return_tensors="pt"
        )

        if not self.first_input:
            bot_input_ids = torch.cat(
                [self.chat_history_ids, new_user_input_ids], dim=-1
            )
        else:
            bot_input_ids = new_user_input_ids
            self.first_input = False

        self.chat_history_ids = self.model.generate(
            bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id
        )
        response = ""
        if (
            not self.first_input
            and bot_input_ids.shape[-1] < self.chat_history_ids.shape[1]
        ):
            response = self.tokenizer.decode(
                self.chat_history_ids[:, bot_input_ids.shape[-1] :][0],
                skipt_special_tokens=True,
            )
        return response

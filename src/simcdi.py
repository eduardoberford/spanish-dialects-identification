import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer
from transformers import AdamW, get_linear_schedule_with_warmup

class SimCDI(nn.Module):
    """
    SIMple Contrastive framework for Dialect Identification
    """


    def __init__(self,
                model_name : str,
                device : str) -> None:

        # load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # load bert model
        self.model = AutoModel.from_pretrained(model_name)

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device


    def forward(self, 
                input_ids, 
                attention_mask):
        """
        Feed input to BERT and the classifier to compute logits.
        """
        # forward BERT pass
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)

        # get CLS token
        bert_cls = outputs[0][:, 0, :]

        return bert_cls


    def loss_fn(self):
        raise NotImplementedError
from rouge import Rouge


def score_func(pre, tru):
    batch_scores = []
    pre_token = pre.tolist()
    tru_token = tru.tolist()

import torch

# 모델을 로드할 경로 지정
model_path = 'path_to_your_model.pt'

# 모델을 로드 (가중치만 로드하도록 설정)
model = torch.load(model_path, weights_only=True)
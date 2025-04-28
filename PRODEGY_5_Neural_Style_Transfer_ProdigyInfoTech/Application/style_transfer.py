import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
from nst_utils import gram_matrix, get_features, image_loader, im_convert

def run_style_transfer(content_path, style_path, output_path, num_steps=300, style_weight=1e6, content_weight=1):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    content = image_loader(content_path).to(device)
    style = image_loader(style_path).to(device)
    target = content.clone().requires_grad_(True).to(device)

    vgg = models.vgg19(pretrained=True).features.to(device).eval()
    for param in vgg.parameters():
        param.requires_grad_(False)

    # Get features
    style_features = get_features(style, vgg)
    content_features = get_features(content, vgg)

    # Gram matrices for style
    style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

    optimizer = torch.optim.Adam([target], lr=0.003)
    style_loss_fn = nn.MSELoss()
    content_loss_fn = nn.MSELoss()

    for step in range(num_steps):
        target_features = get_features(target, vgg)

        content_loss = content_loss_fn(target_features['conv4_2'], content_features['conv4_2'])

        style_loss = 0
        for layer in style_grams:
            target_feature = target_features[layer]
            target_gram = gram_matrix(target_feature)
            _, d, h, w = target_feature.shape
            style_gram = style_grams[layer]
            style_loss += style_loss_fn(target_gram, style_gram) / (d * h * w)

        total_loss = content_weight * content_loss + style_weight * style_loss

        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

    final_img = im_convert(target)
    final_img.save(output_path)

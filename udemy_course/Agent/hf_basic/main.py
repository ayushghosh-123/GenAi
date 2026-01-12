from transformers import pipeline

pipe = pipeline("image-text-to-text", model='google/gemma-b-it')

message = [
    {
        'role': 'user',
        'content': [
            {'type': 'image', 'url': 'https://huggingface.co/datasets/huggingface/'},
            {'type': 'text', 'text': 'what animal is on the candy'}
        ]
    }
]

pipe(text=message)
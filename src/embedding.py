from load import model

def get_embedding(text):

    embedding = model.encode(text)

    return embedding


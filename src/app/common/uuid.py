import ulid


def new():
    id_ = ulid.new()
    return id_.uuid

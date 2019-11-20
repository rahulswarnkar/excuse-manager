_excuse_list = []

def replace_list(new_list):
    global _excuse_list
    _excuse_list = new_list

def get_all():
    return _excuse_list

def get_by_id(id):
    excuse = next((excuse for excuse in _excuse_list if excuse['id'] == id), None)
    return excuse

def add(excuse):
    id = len(_excuse_list) + 1
    excuse_to_add = {
        'id': id,
        'message': excuse['message']
    }
    _excuse_list.append(excuse_to_add)

def delete_by_id(id):
    excuse = get_by_id(id)
    if(excuse is None):
        return False
    _excuse_list.remove(excuse)
    return True

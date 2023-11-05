team = [
    {
        'id' : 'U063QS7F1LZ',
        'name' : 'Léa',
        'job' : 'Designer'
    }
]

def getMemberByID(id):
    for member in team:
        if member['id'] == id:
            selected_member = member
            return selected_member
    
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
tickets_by_type = {}
def uniq_tickets():
    tickets_list = []
    for key, value in tickets.items():
        uniq_ticket_list = []
        for elem in value:
            if elem not in tickets_list:
                uniq_ticket_list.append(elem)
        tickets[key] = uniq_ticket_list
        tickets_list.extend(value)

def link_types_tickets():
    for key, value in types.items():
        tickets_by_type[value] = tickets[key]

uniq_tickets()
link_types_tickets()
print(tickets_by_type)
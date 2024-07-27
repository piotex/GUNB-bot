import gspread

email = ""
gc = gspread.service_account(filename='../secrets/gunb-bot-project-credentials.json')

sh = gc.create('gunb-lipiec')
sh = gc.open("gunb-lipiec")
spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % sh.id

worksheet = sh.add_worksheet(title="gunb-worksheet-1", rows="100", cols="20")
worksheet.update_acell('B1', 'Bingo!')
worksheet.update([[1, 2], [3, 4]], 'A1:B2')
worksheet.batch_update([{
    'range': 'A1:B2',
    'values': [['A1', 'B1'], ['A2', 'B2']],
}, {
    'range': 'J42:K43',
    'values': [[1, 2], [3, 4]],
}])

sh.share(email, perm_type='user', role='writer')


print(sh.sheet1.get('A1'))
print(spreadsheet_url)




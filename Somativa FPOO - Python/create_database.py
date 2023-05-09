from conectar import conexao, cursor


def inserir_jogos(id, n1, n2, n3, n4, n5, n6):
    jogos = f"""INSERT INTO jogos(id, n1, n2, n3, n4, n5, n6)
    values
    ({int(id)}, {int(n1)}, {int(n2)}, {int(n3)}, {int(n4)}, {int(n5)}, {int(n6)});"""
    cursor.execute(jogos)
    conexao.commit()


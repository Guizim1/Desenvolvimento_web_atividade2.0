from flask import Flask, request, render_template, redirect
from model1 import *
from model2 import *

app = Flask(__name__)

# Função para selecionar um item da lista de dicionários pelo ID
def listagem(lista: list, id: int):
    for i in lista:
        if i['id'] == id:
            return i
    raise ValueError("O item não foi encontrado na lista!")

# Função para registrar as relações entre o personagem registrado e outras tabelas
def registro_de_relacionamentos(id_Grupo: int, id_mis: int, id_gene: int):
    try:
        # Obtém o ID do último personagem registrado
        ultimo_id = Obj_Personagem.select_person()[-1]['id']
        # Adiciona relacionamentos com Grupo, Missão e Gênero
        Obj_grupo.add_Person_Grupo(ultimo_id, id_Grupo)
        Obj_Mis.add_Person_Miss(ultimo_id, id_mis)
        Obj_Genero.add_PersonGene(ultimo_id, id_gene)
    except Exception as e:
        # Imprime erro se houver problema ao registrar relacionamentos
        print(f"Erro ao registrar relacionamentos: {e}")

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Páginas da Entidade Personagens

# Exibe a lista de Personagens
@app.route('/Personagem')
def lista_Personagens():
    All_Personagens = Obj_Personagem.select_person()
    PGrup = Obj_grupo.select_registro_PersonGrupo()
    PGene = Obj_Genero.select_registro_PersonGene()
    PMis = Obj_Mis.select_registro_PersonMiss()
    return render_template('viewPersonagens.html', Personagens=All_Personagens, PGrup=PGrup, PGene=PGene, PMis=PMis)

# Adiciona um novo Personagem
@app.route('/Personagem/novo', methods=['GET', 'POST'])
def add_person():
    grup = Obj_grupo.select_Grupo()
    miss = Obj_Mis.select_mis()
    gen = Obj_Genero.select_gen()
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona o novo personagem
        Obj_Personagem.add_person(
            data['nome_person'], data['poder_person'], data['arma_person'],
            int(data['forca']), int(data['agilidade']), int(data['nivel'])
        )
        # Registra relacionamentos do personagem com Grupo, Missão e Gênero
        registro_de_relacionamentos(
            int(data['grup']), int(data['miss']), int(data['gen'])
        )
        return redirect('/Personagem')
    return render_template('formPersonagem.html', title="Adicionar Novo Personagem", Personagem=None, Grupo=grup, Missoes=miss, Genero=gen)

# Edita um Personagem existente
@app.route('/Personagem/editar/<int:id>', methods=['GET', 'POST'])
def edit_Person(id):
    grup = Obj_grupo.select_Grupo()
    miss = Obj_Mis.select_mis()
    gen = Obj_Genero.select_gen()
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados do personagem
        Obj_Personagem.update_person(
            id, data['nome_person'], data['poder_person'], data['arma_person'],
            int(data['forca']), int(data['agilidade']), int(data['nivel'])
        )
        return redirect('/Personagem')
    person = listagem(Obj_Personagem.select_person(), id)
    return render_template('formPersonagem.html', title="Editar Personagem", Personagem=person, Grupo=grup, Missoes=miss, Genero=gen)

# Remove um Personagem da tabela
@app.route('/Personagem/remover/<int:id>', methods=['GET'])
def delete_person(id):
    Obj_Personagem.del_person(id)
    return redirect('/Personagem')

# Páginas da Entidade Grupos

# Exibe a lista de Grupos
@app.route('/Grupo')
def list_grupos():
    All_Grupos = Obj_grupo.select_Grupo()
    return render_template('viewGrupos.html', Grupos=All_Grupos)

# Adiciona um novo Grupo
@app.route('/Grupo/novo', methods=['GET', 'POST'])
def add_Grupo():
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona o novo grupo
        Obj_grupo.add_Grupo(data['nome_Grupo'])
        return redirect('/Grupo')
    return render_template('formGrupo.html', title="Adicionar Novo Grupo", Grupo=None)

# Edita um Grupo existente
@app.route('/Grupo/editar/<int:id>', methods=['GET', 'POST'])
def edit_grup(id):
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados do grupo
        Obj_grupo.update_Grupo(
            id, data['nome_Grupo'], int(data['quant_membros'])
        )
        return redirect('/Grupo')
    grup = listagem(Obj_grupo.select_Grupo(), id)
    return render_template('formGrupo.html', title="Editar Grupo", Grupo=grup)

# Remove um Grupo da tabela
@app.route('/Grupo/remover/<int:id>', methods=['GET'])
def delete_grup(id):
    Obj_grupo.del_Grupo(id)
    return redirect('/Grupo')

# Páginas da Entidade Missões

# Exibe a lista de Missões
@app.route('/Missoes')
def list_miss():
    miss = Obj_Mis.select_mis()
    return render_template('viewMissoes.html', Missoes=miss)

# Adiciona uma nova Missão
@app.route('/Missoes/novo', methods=['GET', 'POST'])
def add_mis():
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona a nova missão
        Obj_Mis.add_mis(data['objetivo'], data['descricao'], data['recompensa'])
        return redirect('/Missoes')
    return render_template('formMissoes.html', title="Adicionar Nova Missão", Missao=None)

# Edita uma Missão existente
@app.route('/Missoes/editar/<int:id>', methods=['GET', 'POST'])
def edit_miss(id):
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados da missão
        Obj_Mis.update_mis(id, data['objetivo'], data['descricao'], data['recompensa'])
        return redirect('/Missoes')
    missao = listagem(Obj_Mis.select_mis(), id)
    return render_template('formMissoes.html', title="Editar Missão", Missao=missao)

# Remove uma Missão da tabela
@app.route('/Missoes/remover/<int:id>', methods=['GET'])
def delete_mis(id):
    Obj_Mis.del_mis(id)
    return redirect('/Missoes')

# Páginas da Entidade Gêneros

# Exibe a lista de Gêneros
@app.route('/Genero')
def list_gen():
    gene = Obj_Genero.select_gen()
    return render_template('viewGeneros.html', Generos=gene)

# Adiciona um novo Gênero
@app.route('/Genero/novo', methods=['GET', 'POST'])
def add_gen():
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona o novo gênero
        Obj_Genero.add_gen(data['tipo'])
        return redirect('/Genero')
    return render_template('formGeneros.html', title="Adicionar Novo Gênero", Genero=None)

# Edita um Gênero existente
@app.route('/Genero/editar/<int:id>', methods=['GET', 'POST'])
def edit_gen(id):
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados do gênero
        Obj_Genero.update_gen(id, data['tipo'])
        return redirect('/Genero')
    gen = listagem(Obj_Genero.select_gen(), id)
    return render_template('formGeneros.html', title="Editar Gênero", Genero=gen)

# Remove um Gênero da tabela
@app.route('/Genero/remover/<int:id>', methods=['GET'])
def delete_gen(id):
    Obj_Genero.del_gen(id)
    return redirect('/Genero')

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run()

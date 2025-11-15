from django.shortcuts import render
from .models import Oficina, Livro, Contato
from .forms import ContatoForm

def home(request):
    oficinas = [
        {'nome': 'Pintura', 'descricao': 'Oficina de pintura artística para todas as idades.'},
        {'nome': 'Escultura', 'descricao': 'Aprenda técnicas de modelagem e escultura.'},
        {'nome': 'Música', 'descricao': 'Oficinas de instrumentos musicais e canto.'}
    ]

    livros = [
        {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry'},
        {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis'},
        {'titulo': '1984', 'autor': 'George Orwell'}
    ]

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            print("📩 NOVA MENSAGEM RECEBIDA:")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Mensagem: {mensagem}")

            return render(request, 'core/home.html', {
                'form': ContatoForm(),
                'oficinas': oficinas,
                'livros': livros,
                'sucesso': "Mensagem enviada com sucesso!"
            })
    else:
        form = ContatoForm()

    return render(request, 'core/home.html', {
        'form': form,
        'oficinas': oficinas,
        'livros': livros
    })

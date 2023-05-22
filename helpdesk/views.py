from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Ticket
from .forms import CommentForm


# Выводит список заявок пользователя, которые отсортированы по дате создания в обратном порядке
@login_required
def index(request):
    # tickets = Ticket.objects \
    #     .filter(user=request.user).order_by('-created_at') \
    #     .exclude(status='Closed')
    if request.user.groups.filter(name='HelpDesk').exists():
        tickets = Ticket.objects.exclude(status="Closed")
    else:
        tickets = Ticket.objects \
            .filter(user=request.user).order_by('-created_at') \
            .exclude(status='Closed')
    return render(request, 'helpdesk/index.html', {'tickets': tickets})


# Обрабатывает запрос на создание новой заявки. Если запрос был отправлен методом POST, мы создаем новую заявку на
# основе полученных данных и перенаправляем пользователя на страницу просмотра созданной заявки. В противном случае мы
# отображаем страницу с формой для создания новой заявки
@login_required
def create_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ticket = Ticket(user=request.user, title=title, description=description)
        ticket.save()
        return redirect('helpdesk:view_ticket', ticket_id=ticket.id)
    else:
        return render(request, 'helpdesk/create_ticket.html')


# Обрабатывает запрос на просмотр конкретной заявки. Мы получаем объект заявки на основе ее идентификатора и отображаем
# ее на странице просмотра
@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    comments = ticket.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.user = request.user
            comment.save()
            form = CommentForm()    # Очистить форму после сохранения комментария
    else:
        form = CommentForm()

    return render(request, 'helpdesk/view_ticket.html', {'ticket': ticket, 'comments': comments, 'form': form})

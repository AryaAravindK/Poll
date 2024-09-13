from django.shortcuts import render, redirect
from home.models import Poll, Response
from django.contrib.auth.decorators import login_required 


@login_required
def select_poll(request):
    selected_poll_id = None
    action = request.POST.get('action')

    if request.method == 'POST':
        selected_poll_id = request.POST.get('poll')
        if selected_poll_id:
            if action == 'display':
                # Set quiz_visible to False for all polls
                Poll.objects.all().update(quiz_visible=False)

                # Set quiz_visible to True for the selected poll
                selected_poll = Poll.objects.get(id=selected_poll_id)
                selected_poll.quiz_visible = True
                selected_poll.save()
            elif action == 'show_results':
                # Set quiz_complete to False for all polls
                Poll.objects.all().update(quiz_complete=False)

                # Set quiz_complete to True for the selected poll
                selected_poll = Poll.objects.get(id=selected_poll_id)
                selected_poll.quiz_complete = True
                selected_poll.save()

    polls = Poll.objects.all()

    # Filter responses by the selected poll
    if selected_poll_id:
        responses = Response.objects.filter(poll_id=selected_poll_id).order_by('-score', 'submit_time')
    else:
        responses = Response.objects.none()  # No responses if no poll is selected

    return render(request, 'select_poll.html', {
        'polls': polls,
        'selected_poll_id': selected_poll_id,
        'responses': responses
    })



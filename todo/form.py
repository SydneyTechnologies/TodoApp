from django.forms import ModelForm
from . models import Todo

class TodoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'text-title', 'placeholder':'Enter your Todo title'})
        self.fields['description'].widget.attrs.update({'class':'text-space', 'placeholder':'Enter a description'})
        #self.fields['due_date'].widget.attrs.update({'class':'text-title'})
    class Meta:
        model = Todo
        fields = "__all__"